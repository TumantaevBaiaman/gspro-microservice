from datetime import date

import grpc

from generated.progress import lesson_progress_pb2 as pb2
from generated.progress import lesson_progress_pb2_grpc as pb2_grpc

from src.application.services.lesson_progress_service import LessonProgressService
from src.application.commands.lesson_progress.dto import UpdateLessonProgressDTO


class LessonProgressHandler(pb2_grpc.ProgressServiceServicer):

    def __init__(self, service: LessonProgressService):
        self.service = service

    async def UpdateLessonProgress(self, request, context):
        dto = UpdateLessonProgressDTO(
            user_id=request.user_id,
            course_id=request.course_id,
            module_id=request.module_id,
            lesson_id=request.lesson_id,
            lesson_type=request.lesson_type,
            current_time=request.current_time or None,
            duration_seconds=request.duration_seconds or None,
            last_scroll_percent=request.last_scroll_percent or None,
        )

        progress = await self.service.update_lesson.execute(dto)

        return pb2.UpdateLessonProgressResponse(
            progress=self._map_progress(progress)
        )

    async def GetLessonProgress(self, request, context):
        data = await self.service.get_lesson.execute(
            user_id=request.user_id,
            lesson_id=request.lesson_id,
        )

        return pb2.GetLessonProgressResponse(
            lesson_id=data["lesson_id"],
            last_position_seconds=data.get("last_position_seconds", 0),
            last_scroll_percent=data.get("last_scroll_percent", 0),
            is_completed=data.get("is_completed", False),
        )

    async def GetCompletedLessonsCount(self, request, context):
        count = await self.service.get_completed_lessons_count.execute(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        return pb2.GetCompletedLessonsCountResponse(
            completed_lessons=count
        )

    @staticmethod
    def _map_progress(progress):
        return pb2.LessonProgress(
            user_id=progress.user_id,
            course_id=progress.course_id,
            module_id=progress.module_id,
            lesson_id=progress.lesson_id,
            lesson_type=progress.lesson_type,
            watched_seconds=progress.watched_seconds,
            duration_seconds=progress.duration_seconds or 0,
            last_position_seconds=progress.last_position_seconds,
            last_scroll_percent=progress.last_scroll_percent or 0,
            is_completed=progress.is_completed,
        )

    async def GetLearningDays(self, request, context):
        from_date = (
            date.fromisoformat(request.from_date)
            if request.HasField("from_date")
            else None
        )
        to_date = (
            date.fromisoformat(request.to_date)
            if request.HasField("to_date")
            else None
        )

        days = await self.service.get_learning_days.execute(
            user_id=request.user_id,
            course_id=request.course_id,
            from_date=from_date,
            to_date=to_date,
        )

        return pb2.GetLearningDaysResponse(
            days=[d.isoformat() for d in days],
            from_date=(
                from_date.isoformat()
                if from_date
                else (days[0].isoformat() if days else "")
            ),
            to_date=(
                to_date.isoformat()
                if to_date
                else date.today().isoformat()
            ),
            count=len(days),
        )