import grpc

from generated.course import lesson_pb2 as pb2
from generated.course import lesson_pb2_grpc as pb2_grpc

from src.application.services.lesson_service import LessonService
from src.domain.exceptions.lesson import LessonNotFoundError


class LessonHandler(pb2_grpc.LessonServiceServicer):

    def __init__(self, service: LessonService):
        self.service = service

    async def GetLesson(self, request, context):
        try:
            lesson = await self.service.get.execute(request.id)

            return pb2.GetLessonResponse(
                lesson=self._map_full(lesson)
            )

        except LessonNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def ListLessonsByModule(self, request, context):
        lessons = await self.service.list_by_module.execute(
            request.module_id
        )

        return pb2.ListLessonsResponse(
            items=[
                self._map_short(lesson)
                for lesson in lessons
            ]
        )

    # ===== MAPPERS =====

    @staticmethod
    def _map_full(lesson):
        return pb2.Lesson(
            id=str(lesson.id),
            module_id=lesson.module_id,
            title=lesson.title,

            type=lesson.type.value,
            content=lesson.content or "",

            video_id=lesson.video_id or "",
            duration=lesson.duration or "",

            order_number=lesson.order_number or 0,
            is_active=lesson.is_active,

            access_type=lesson.access_type.value,
        )

    @staticmethod
    def _map_short(lesson):
        return pb2.LessonShort(
            id=str(lesson.id),
            title=lesson.title,

            type=lesson.type.value,
            access_type=lesson.access_type.value,
            duration=lesson.duration or "",

            order_number=lesson.order_number or 0,
            is_active=lesson.is_active,
        )
