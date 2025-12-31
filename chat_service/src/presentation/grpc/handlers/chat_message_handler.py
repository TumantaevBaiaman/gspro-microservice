import grpc

from generated.chat import chat_message_pb2 as pb2
from generated.chat import chat_message_pb2_grpc as pb2_grpc

from src.application.services.chat_message_service import (
    ChatMessageService,
)
from src.application.commands.chat_message.dto import (
    SendMessageDTO,
)
from src.application.queries.chat_message.dto import (
    ListChatMessagesDTO,
)

from src.infrastructure.db.mongo.models.chat_document import ChatParticipant
from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessagePayload,
    ChatMessageContext,
    MessageReference,
)


class ChatMessageHandler(pb2_grpc.ChatMessageServiceServicer):

    def __init__(self, service: ChatMessageService):
        self.service = service

    async def SendMessage(self, request, context):
        dto = SendMessageDTO(
            scope=request.scope,
            sender_id=request.sender_id,
            participants=[
                ChatParticipant(
                    user_id=p.user_id,
                    role=p.role,
                )
                for p in request.participants
            ],
            course_id=request.course_id or None,
            payload=self._map_payload(request.payload),
            context=self._map_context(request.context),
        )

        try:
            chat, message = await self.service.send.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.SendMessageResponse(
            chat=self._map_chat(chat),
            message=self._map_message(message),
        )

    async def ListMessages(self, request, context):
        dto = ListChatMessagesDTO(
            chat_id=request.chat_id,
            limit=request.limit,
            offset=request.offset,
        )

        try:
            items, total = await self.service.list_by_chat.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.ListMessagesResponse(
            items=[self._map_message(item) for item in items],
            total=total,
        )

    @staticmethod
    def _map_payload(payload: pb2.ChatMessagePayload) -> ChatMessagePayload:
        return ChatMessagePayload(
            type=payload.type,
            text=payload.text or None,
        )

    @staticmethod
    def _map_context(context: pb2.ChatMessageContext) -> ChatMessageContext:
        if not context.reference.type:
            return ChatMessageContext()

        return ChatMessageContext(
            reference=MessageReference(
                type=context.reference.type,
                id=context.reference.id,
            ),
            reply_to_message_id=context.reply_to_message_id or None,
        )

    @staticmethod
    def _map_chat(chat):
        return pb2.Chat(
            id=str(chat.id),
            scope=chat.scope,
            course_id=chat.course_id or "",
            participant_ids=chat.participant_ids,
            last_message_at=int(chat.last_message_at.timestamp())
            if chat.last_message_at
            else 0,
        )

    @staticmethod
    def _map_message(message):
        return pb2.ChatMessage(
            id=str(message.id),
            chat_id=message.chat_id,
            sender_id=message.sender_id,
            payload=pb2.ChatMessagePayload(
                type=message.payload.type,
                text=message.payload.text or "",
            ),
            context=pb2.ChatMessageContext(
                reply_to_message_id=(
                    message.context.reply_to_message_id or ""
                ),
                reference=pb2.MessageReference(
                    type=(
                        message.context.reference.type
                        if message.context.reference
                        else 0
                    ),
                    id=(
                        message.context.reference.id
                        if message.context.reference
                        else ""
                    ),
                ),
            ),
            created_at=int(
                message.meta.created_at.timestamp()
            ),
        )
