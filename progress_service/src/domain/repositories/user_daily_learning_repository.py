from abc import ABC, abstractmethod
from datetime import date

from src.infrastructure.db.mongo.models.user_daily_learning_document import (
    UserDailyLearningDocument
)


class IUserDailyLearningRepository(ABC):

    @abstractmethod
    async def mark(
        self,
        *,
        user_id: str,
        course_id: str,
        learning_date: date,
    ) -> None:
        ...

    @abstractmethod
    async def count_days(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        ...

    @abstractmethod
    async def get_learning_days(
            self,
            *,
            user_id: str,
            course_id: str,
            from_date: date | None = None,
            to_date: date | None = None,
    ) -> list[date]:
        ...
