import grpc

from generated.chat import chat_message_pb2 as pb2
from generated.chat import chat_message_pb2_grpc as pb2_grpc
from src.application.commands.chat.dto import GetOrCreateChatDTO
from src.application.commands.chat_message.dto import SendMessageDTO
from src.application.commands.chat_participant.dto import AddChatParticipantDTO
from src.application.queries.chat_message.dto import ListMessagesByChatDTO
from src.application.queries.chat_participant.dto import ListChatParticipantsDTO

from src.application.services.chat_service import ChatService
from src.application.services.chat_message_service import ChatMessageService
from src.application.services.chat_participant_service import ChatParticipantService
from src.domain.enums.chat_participant_role_enum import ChatParticipantRole

from src.domain.enums.chat_type_enum import ChatTypeEnum
from src.domain.enums.chat_message_type_enum import ChatMessageTypeEnum

from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessagePayload,
    ChatMessageContext, ChatAttachment,
)


class ChatMessageHandler(pb2_grpc.ChatMessageServiceServicer):

    def __init__(
        self,
        chat_service: ChatService,
        chat_message_service: ChatMessageService,
        chat_participant_service: ChatParticipantService,
    ):
        self.chat_service = chat_service
        self.chat_message_service = chat_message_service
        self.chat_participant_service = chat_participant_service

    async def SendMessage(self, request, context):
        if request.chat_id:
            chat_id = request.chat_id
        else:
            chat = await self._get_or_create_chat(request, context)
            chat_id = str(chat.id)

        message_type: ChatMessageTypeEnum = ChatMessageTypeEnum.TEXT
        try:
            message_type = ChatMessageTypeEnum(request.type)
        except ValueError:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Invalid message type",
            )

        if message_type == ChatMessageTypeEnum.TEXT and not request.text:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Text message must contain text",
            )

        if message_type != ChatMessageTypeEnum.TEXT and not request.attachments:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Media message must contain attachments",
            )

        payload = ChatMessagePayload(
            type=message_type,
            text=request.text or None,
            attachments=[
                ChatAttachment(
                    file_id=a.file_id,
                    url=a.url,
                    mime_type=a.mime_type or None,
                    size=a.size or None,
                    duration=a.duration or None,
                )
                for a in request.attachments
            ]
        )

        message_context = ChatMessageContext(
            reference=None,
            reply_to_message_id=None,
        )

        message = await self.chat_message_service.send.execute(
            SendMessageDTO(
                chat_id=chat_id,
                sender_id=request.sender_id,
                payload=payload,
                context=message_context,
            )
        )
        participants = await self.chat_participant_service.list_by_chat.execute(
            ListChatParticipantsDTO(
                chat_id=chat_id,
            )
        )
        participant_ids = [str(p.user_id) for p in participants]

        return pb2.SendMessageResponse(
            chat_id=chat_id,
            message_id=str(message.id),
            participant_ids=participant_ids,
        )

    async def _get_or_create_chat(self, request, context):
        chat_type = request.chat_type
        try:
            chat_type = ChatTypeEnum(request.chat_type)
        except ValueError:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Invalid chat_type",
            )

        # =======================
        # COURSE_PRIVATE
        # =======================
        if chat_type == ChatTypeEnum.COURSE_PRIVATE:
            if not request.course_id or not request.student_id:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    "course_id and student_id are required for COURSE_PRIVATE",
                )

            unique_key = (
                f"chat:course:private:"
                f"{request.course_id}:student:{request.student_id}"
            )

            chat = await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                    course_id=request.course_id,
                )
            )
            await self.chat_participant_service.add.execute(
                AddChatParticipantDTO(
                    chat_id=str(chat.id),
                    user_id=request.student_id,
                    role=ChatParticipantRole.STUDENT
                )
            )
            return chat

        # =======================
        # COURSE_GROUP
        # =======================
        if chat_type == ChatTypeEnum.COURSE_GROUP:
            if not request.course_id:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    "course_id is required for COURSE_GROUP",
                )

            unique_key = f"chat:course:group:{request.course_id}"

            chat = await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                    course_id=request.course_id,
                )
            )
            await self.chat_participant_service.add.execute(
                AddChatParticipantDTO(
                    chat_id=str(chat.id),
                    user_id=request.sender_id,
                    role=ChatParticipantRole.MEMBER
                )
            )
            return chat

        # =======================
        # DIRECT
        # =======================
        if chat_type == ChatTypeEnum.DIRECT:
            if not request.peer_id:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    "peer_id is required for DIRECT chat",
                )

            a, b = sorted([request.sender_id, request.peer_id])

            unique_key = f"chat:direct:user:{a}:user:{b}"

            chat = await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                )
            )
            await self.chat_participant_service.add.execute(
                AddChatParticipantDTO(
                    chat_id=str(chat.id),
                    user_id=request.sender_id,
                    role=ChatParticipantRole.MEMBER
                )
            )
            await self.chat_participant_service.add.execute(
                AddChatParticipantDTO(
                    chat_id=str(chat.id),
                    user_id=request.peer_id,
                    role=ChatParticipantRole.MEMBER
                )
            )
            return chat

        # =======================
        # UNSUPPORTED
        # =======================
        await context.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            "Unsupported chat type",
        )

    async def ListMessages(self, request, context):
        if not request.chat_id:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "chat_id is required",
            )

        limit = request.limit or 10
        offset = request.offset or 0

        messages = await self.chat_message_service.list_by_chat.execute(
            ListMessagesByChatDTO(
                chat_id=request.chat_id,
                limit=limit,
                offset=offset,
            )
        )

        return pb2.ListMessagesResponse(
            messages=[
                pb2.ChatMessage(
                    id=str(m.id),
                    chat_id=m.chat_id,
                    sender_id=m.sender_id,
                    type=m.payload.type.value,
                    text=m.payload.text or "",
                    attachments=[
                        pb2.ChatAttachment(
                            file_id=a.file_id,
                            url=a.url,
                            mime_type=a.mime_type or "",
                            size=a.size or 0,
                            duration=a.duration or 0,
                        )
                        for a in m.payload.attachments
                    ],
                    created_at=m.created_at.isoformat(),
                )
                for m in reversed(messages)
            ]
        )
