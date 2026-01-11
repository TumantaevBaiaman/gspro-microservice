import grpc

from generated.chat import chat_pb2 as pb2
from generated.chat import chat_pb2_grpc as pb2_grpc

from src.application.commands.chat.dto import GetOrCreateChatDTO
from src.application.services import ChatMessageService
from src.application.services.chat_service import ChatService
from src.application.services.chat_participant_service import ChatParticipantService
from src.application.commands.chat_participant.dto import AddChatParticipantDTO

from src.domain.enums.chat_type_enum import ChatTypeEnum
from src.domain.enums.chat_participant_role_enum import ChatParticipantRole


class ChatHandler(pb2_grpc.ChatServiceServicer):

    def __init__(
        self,
        chat_service: ChatService,
        chat_message_service: ChatMessageService,
        chat_participant_service: ChatParticipantService,
    ):
        self.chat_service = chat_service
        self.chat_participant_service = chat_participant_service

    # =====================================================
    # GET OR CREATE CHAT
    # =====================================================
    async def GetOrCreateChat(self, request, context):
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
                    "course_id and student_id are required",
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

            return pb2.GetOrCreateChatResponse(
                chat_id=str(chat.id),
                created=False,
                chat_type=request.chat_type,
            )

        # =======================
        # COURSE_GROUP
        # =======================
        if chat_type == ChatTypeEnum.COURSE_GROUP:
            if not request.course_id:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    "course_id is required",
                )

            unique_key = f"chat:course:group:{request.course_id}"

            chat = await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                    course_id=request.course_id,
                )
            )

            return pb2.GetOrCreateChatResponse(
                chat_id=str(chat.id),
                created=False,
                chat_type=request.chat_type,
            )

        # =======================
        # DIRECT
        # =======================
        if chat_type == ChatTypeEnum.DIRECT:
            if not request.sender_id or not request.peer_id:
                await context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    "sender_id and peer_id are required",
                )

            a, b = sorted([request.sender_id, request.peer_id])
            unique_key = f"chat:direct:user:{a}:user:{b}"

            chat = await self.chat_service.get_or_create.execute(
                GetOrCreateChatDTO(
                    type=chat_type,
                    unique_key=unique_key,
                )
            )

            return pb2.GetOrCreateChatResponse(
                chat_id=str(chat.id),
                created=False,
                chat_type=request.chat_type,
            )

        await context.abort(
            grpc.StatusCode.INVALID_ARGUMENT,
            "Unsupported chat_type",
        )
