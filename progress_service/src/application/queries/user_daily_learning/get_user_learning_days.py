from datetime import date, timedelta

from src.domain.repositories.user_daily_learning_repository import (
    IUserDailyLearningRepository
)


class GetUserLearningDaysQuery:
    def __init__(self, repo: IUserDailyLearningRepository):
        self.repo = repo

    async def execute(
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

        return await self.repo.get_learning_days(
            user_id=user_id,
            course_id=course_id,
            from_date=from_date,
            to_date=to_date,
        )
