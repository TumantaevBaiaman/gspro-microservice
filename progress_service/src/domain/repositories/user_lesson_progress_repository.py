from abc import ABC, abstractmethod
from typing import Optional

from src.infrastructure.db.mongo.models.user_lesson_progress_document import (
    UserLessonProgressDocument
)


class IUserLessonProgressRepository(ABC):

    @abstractmethod
    async def get(
        self,
        *,
        user_id: str,
        lesson_id: str,
    ) -> Optional[UserLessonProgressDocument]:
        ...

    @abstractmethod
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
    ) -> UserLessonProgressDocument:
        ...

    @abstractmethod
    async def count_completed_by_course(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        ...
