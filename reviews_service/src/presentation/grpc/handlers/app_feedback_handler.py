import grpc

from generated.reviews import app_feedback_pb2 as pb2
from generated.reviews import app_feedback_pb2_grpc as pb2_grpc

from src.application.commands.app_feedback.dto import (
    CreateAppFeedbackDTO,
)
from src.application.services.app_feedback_service import (
    AppFeedbackService,
)


class AppFeedbackHandler(pb2_grpc.AppFeedbackServiceServicer):

    def __init__(self, service: AppFeedbackService):
        self.service = service

    async def CreateFeedback(self, request, context):
        dto = CreateAppFeedbackDTO(
            user_id=request.user_id,
            message=request.message,
            type=request.type or "feedback",
            is_public=request.is_public,
        )

        feedback = await self.service.create.execute(dto)

        return pb2.CreateFeedbackResponse(
            feedback=self._map_feedback(feedback)
        )

    async def ListFeedback(self, request, context):
        items, total = await self.service.list.execute(
            limit=request.limit,
            offset=request.offset,
        )

        return pb2.ListFeedbackResponse(
            items=[self._map_feedback(item) for item in items],
            total=total,
        )


    @staticmethod
    def _map_feedback(feedback):
        return pb2.AppFeedback(
            id=str(feedback.id),
            user_id=feedback.user_id,
            message=feedback.message,
            type=feedback.type,
            is_public=feedback.is_public,
            created_at=feedback.created_at.isoformat(),
        )
