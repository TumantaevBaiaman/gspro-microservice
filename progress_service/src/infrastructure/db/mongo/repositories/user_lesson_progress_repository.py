from src.domain.repositories.user_lesson_progress_repository import (
    IUserLessonProgressRepository
)
from src.infrastructure.db.mongo.models.user_lesson_progress_document import (
    UserLessonProgressDocument
)


class UserLessonProgressRepository(IUserLessonProgressRepository):

    async def get(
        self,
        *,
        user_id: str,
        lesson_id: str,
    ):
        return await UserLessonProgressDocument.find_one(
            UserLessonProgressDocument.user_id == user_id,
            UserLessonProgressDocument.lesson_id == lesson_id,
        )

    async def upsert(
        self,
        *,
        user_id: str,
        course_id: str,
        module_id: str,
        lesson_id: str,
        lesson_type: str,
        watched_seconds: int | None = None,
        duration_seconds: int | None = None,
        last_position_seconds: int | None = None,
        last_scroll_percent: int | None = None,
        is_completed: bool | None = None,
    ):
        doc = await self.get(user_id=user_id, lesson_id=lesson_id)

        if not doc:
            doc = UserLessonProgressDocument(
                user_id=user_id,
                course_id=course_id,
                module_id=module_id,
                lesson_id=lesson_id,
                lesson_type=lesson_type,
            )

        if watched_seconds is not None:
            if doc.watched_seconds is None:
                doc.watched_seconds = watched_seconds
            else:
                doc.watched_seconds = max(doc.watched_seconds, watched_seconds)

        if duration_seconds is not None:
            doc.duration_seconds = duration_seconds

        if last_position_seconds is not None:
            doc.last_position_seconds = last_position_seconds

        if last_scroll_percent is not None:
            doc.last_scroll_percent = last_scroll_percent

        if is_completed is not None:
            doc.is_completed = is_completed

        await doc.save()
        return doc

    async def count_completed_by_course(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        return await UserLessonProgressDocument.find(
            UserLessonProgressDocument.user_id == user_id,
            UserLessonProgressDocument.course_id == course_id,
            UserLessonProgressDocument.is_completed == True,
        ).count()
