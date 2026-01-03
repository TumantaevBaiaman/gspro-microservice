from bson import ObjectId

from src.domain.entities.lesson_entity import LessonEntity
from src.domain.repositories.lesson_repository import ILessonRepository


class LessonRepository(ILessonRepository):

    async def get_by_id(self, lesson_id: str) -> LessonEntity:
        return await LessonEntity.get(lesson_id)

    async def list_by_module_id(self, module_id: str) -> list[LessonEntity]:
        print(module_id)
        print(await LessonEntity.find(LessonEntity.module_id == module_id).to_list())
        return await (
            LessonEntity.find(LessonEntity.module_id == module_id)
            .sort("order_number")
            .to_list()
        )

    async def count_by_module_id(self, module_id: str) -> int:
        return await LessonEntity.find(
            LessonEntity.module_id == str(module_id)
        ).count()
