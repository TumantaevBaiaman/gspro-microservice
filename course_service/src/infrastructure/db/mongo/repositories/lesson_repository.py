from bson import ObjectId

from src.domain.entities.lesson_entity import LessonEntity
from src.domain.repositories.lesson_repository import ILessonRepository


class LessonRepository(ILessonRepository):

    async def get_by_id(self, lesson_id: str) -> LessonEntity:
        return await LessonEntity.get(lesson_id)

    async def list_by_module_id(self, module_id: str) -> list[LessonEntity]:
        return await (
            LessonEntity.find(LessonEntity.module_id == module_id)
            .sort("order_number")
            .to_list()
        )

    async def count_by_module_id(self, module_id: str) -> int:
        return await LessonEntity.find(
            LessonEntity.module_id == str(module_id)
        ).count()

    async def has_free_lessons(self, module_id: str) -> bool:
        return await LessonEntity.find_one(
            {
                "module_id": str(module_id),
                "access_type": "free",
            }
        ) is not None

