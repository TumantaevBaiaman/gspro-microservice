import grpc

from generated.chat import chat_message_pb2 as pb2
from generated.chat import chat_message_pb2_grpc as pb2_grpc
from src.application.commands.chat.dto import GetOrCreateChatDTO
from src.application.commands.chat_message.dto import SendMessageDTO

from src.application.services.chat_service import ChatService
from src.application.services.chat_message_service import ChatMessageService

from src.domain.enums.chat_type_enum import ChatTypeEnum
from src.domain.enums.chat_message_type_enum import ChatMessageTypeEnum

from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessagePayload,
    ChatMessageContext,
)


class ChatMessageHandler(pb2_grpc.ChatMessageServiceServicer):

    def __init__(
        self,
        chat_service: ChatService,
        chat_message_service: ChatMessageService,
    ):
        self.chat_service = chat_service
        self.chat_message_service = chat_message_service

    async def SendMessage(self, request, context):
        if request.chat_id:
            chat_id = request.chat_id
        else:
            chat = await self._get_or_create_chat(request, context)
            chat_id = str(chat.id)

        payload = ChatMessagePayload(
            type=ChatMessageTypeEnum.TEXT,
            text=request.text,
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

        return pb2.SendMessageResponse(
            chat_id=chat_id,
            message_id=str(message.id),
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

            return await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                    course_id=request.course_id,
                )
            )

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

            return await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                    course_id=request.course_id,
                )
            )

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

            return await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                )
            )

        # =======================
        # UNSUPPORTED
        # =======================
        await context.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            "Unsupported chat type",
        )
