from typing import List
from src.domain.entities.lesson_entity import LessonEntity
from src.domain.dto.admin_lesson_dto import AdminLessonCreateDTO
from src.domain.repositories.admin_lesson_repository import IAdminLessonRepository


class AdminLessonRepository(IAdminLessonRepository):

    async def create(self, dto: AdminLessonCreateDTO) -> LessonEntity:
        lesson = LessonEntity(**dto.model_dump())
        return await lesson.insert()

    async def get(self, lesson_id: str) -> LessonEntity | None:
        return await LessonEntity.get(lesson_id)

    async def list(self, module_id: str | None = None) -> List[LessonEntity]:
        if module_id:
            return await LessonEntity.find(LessonEntity.module_id == module_id).to_list()
        return await LessonEntity.find_all().to_list()

    async def save(self, lesson: LessonEntity) -> LessonEntity:
        return await lesson.save()

    async def delete(self, lesson: LessonEntity):
        return await lesson.delete()
