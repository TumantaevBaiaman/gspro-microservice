from src.domain.dto.admin_lesson_dto import AdminLessonUpdateDTO
from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository
from src.domain.exceptions.admin_lesson import LessonNotFoundError


class UpdateLessonCommand:
    def __init__(self, repo: IAdminLessonRepository):
        self.repo = repo

    async def execute(self, lesson_id: str, dto: AdminLessonUpdateDTO):
        lesson = await self.repo.get(lesson_id)
        if not lesson:
            raise LessonNotFoundError("Lesson not found")

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(lesson, key, value)

        return await self.repo.save(lesson)
