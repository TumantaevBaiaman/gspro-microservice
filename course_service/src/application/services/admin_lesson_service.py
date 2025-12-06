from fastapi import HTTPException

from src.domain.dto.admin_lesson_dto import AdminLessonCreateDTO, AdminLessonUpdateDTO
from src.domain.repositories.admin_lesson_repository import AdminLessonRepository


class AdminLessonService:
    def __init__(self):
        self.repo = AdminLessonRepository()

    async def create_lesson(self, dto: AdminLessonCreateDTO):
        return await self.repo.create(dto)

    async def get_lesson(self, lesson_id: str):
        lesson = await self.repo.get(lesson_id)
        if not lesson:
            raise HTTPException(404, "Lesson not found")
        return lesson

    async def delete_lesson(self, lesson_id: str):
        lesson = await self.get_lesson(lesson_id)
        await self.repo.delete(lesson)
        return True

    async def update_lesson(self, lesson_id: str, dto: AdminLessonUpdateDTO):
        lesson = await self.get_lesson(lesson_id)

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(lesson, key, value)

        return await self.repo.save(lesson)

    async def list_lessons(self, module_id: str | None = None):
        return await self.repo.list(module_id)
