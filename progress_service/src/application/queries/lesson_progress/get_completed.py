from src.domain.repositories.user_lesson_progress_repository import (
    IUserLessonProgressRepository
)


class GetCompletedLessonsCountQuery:
    def __init__(self, repo: IUserLessonProgressRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> int:
        return await self.repo.count_completed_by_course(
            user_id=user_id,
            course_id=course_id,
        )
