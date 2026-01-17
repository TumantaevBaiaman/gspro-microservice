from src.domain.repositories.user_lesson_progress_repository import (
    IUserLessonProgressRepository
)


class GetLessonProgressQuery:
    def __init__(self, repo: IUserLessonProgressRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: str,
        lesson_id: str,
    ):
        progress = await self.repo.get(
            user_id=user_id,
            lesson_id=lesson_id,
        )

        if not progress:
            return {
                "lesson_id": lesson_id,
                "last_position_seconds": 0,
                "is_completed": False,
            }

        return {
            "lesson_id": lesson_id,
            "last_position_seconds": progress.last_position_seconds,
            "last_scroll_percent": progress.last_scroll_percent,
            "is_completed": progress.is_completed,
        }
