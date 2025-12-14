from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository
from src.domain.exceptions.admin_lesson import LessonNotFoundError


class DeleteLessonCommand:
    def __init__(self, repo: IAdminLessonRepository):
        self.repo = repo

    async def execute(self, lesson_id: str):
        lesson = await self.repo.get(lesson_id)
        if not lesson:
            raise LessonNotFoundError("Lesson not found")

        await self.repo.delete(lesson)
        return True
