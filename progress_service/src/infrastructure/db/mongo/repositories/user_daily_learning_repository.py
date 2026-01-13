from datetime import date

from src.domain.repositories.user_daily_learning_repository import (
    IUserDailyLearningRepository
)
from src.infrastructure.db.mongo.models.user_daily_learning_document import (
    UserDailyLearningDocument
)


class UserDailyLearningRepository(IUserDailyLearningRepository):

    async def mark(
        self,
        *,
        user_id: str,
        course_id: str,
        learning_date: date,
    ) -> None:
        await UserDailyLearningDocument.find_one(
            UserDailyLearningDocument.user_id == user_id,
            UserDailyLearningDocument.course_id == course_id,
            UserDailyLearningDocument.learning_date == learning_date,
        ).upsert(
            on_insert=UserDailyLearningDocument(
                user_id=user_id,
                course_id=course_id,
                learning_date=learning_date,
            )
        )

    async def count_days(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        return await UserDailyLearningDocument.find(
            UserDailyLearningDocument.user_id == user_id,
            UserDailyLearningDocument.course_id == course_id,
        ).count()
