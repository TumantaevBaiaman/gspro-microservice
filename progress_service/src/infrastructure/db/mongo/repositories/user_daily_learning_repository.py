from datetime import date, timedelta

from beanie.odm.operators.update.general import SetOnInsert

from src.core import logging
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
        await UserDailyLearningDocument.find(
            UserDailyLearningDocument.user_id == user_id,
            UserDailyLearningDocument.course_id == course_id,
            UserDailyLearningDocument.learning_date == learning_date,
        ).update(
            SetOnInsert({
                "user_id": user_id,
                "course_id": course_id,
                "learning_date": learning_date,
            }),
            upsert=True,
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

    async def get_learning_days(
            self,
            *,
            user_id: str,
            course_id: str,
            from_date: date | None = None,
            to_date: date | None = None,
    ) -> list[date]:
        if to_date is None:
            to_date = date.today()

        if from_date is None:
            from_date = to_date - timedelta(days=6)

        docs = await UserDailyLearningDocument.find(
            UserDailyLearningDocument.user_id == user_id,
            UserDailyLearningDocument.course_id == course_id,
            UserDailyLearningDocument.learning_date >= from_date,
            UserDailyLearningDocument.learning_date <= to_date,
        ).sort(
            UserDailyLearningDocument.learning_date
        ).to_list()

        return [doc.learning_date for doc in docs]
