from datetime import date

from src.domain.repositories.user_lesson_progress_repository import (
    IUserLessonProgressRepository
)
from src.domain.repositories.user_daily_learning_repository import (
    IUserDailyLearningRepository
)
from src.application.commands.lesson_progress.dto import UpdateLessonProgressDTO


class UpdateLessonProgressCommand:
    def __init__(
        self,
        lesson_repo: IUserLessonProgressRepository,
        daily_repo: IUserDailyLearningRepository,
    ):
        self.lesson_repo = lesson_repo
        self.daily_repo = daily_repo

    async def execute(self, dto: UpdateLessonProgressDTO):
        is_completed = False

        if dto.lesson_type == "video":
            if (
                dto.current_time is not None
                and dto.duration_seconds
                and dto.current_time >= dto.duration_seconds * 0.9
            ):
                is_completed = True

        if dto.lesson_type == "text":
            if dto.last_scroll_percent and dto.last_scroll_percent >= 80:
                is_completed = True

        progress = await self.lesson_repo.upsert(
            user_id=dto.user_id,
            course_id=dto.course_id,
            module_id=dto.module_id,
            lesson_id=dto.lesson_id,
            lesson_type=dto.lesson_type,
            watched_seconds=dto.current_time,
            duration_seconds=dto.duration_seconds,
            last_position_seconds=dto.current_time,
            last_scroll_percent=dto.last_scroll_percent,
            is_completed=is_completed,
        )

        await self.daily_repo.mark(
            user_id=dto.user_id,
            course_id=dto.course_id,
            learning_date=date.today(),
        )

        return progress
