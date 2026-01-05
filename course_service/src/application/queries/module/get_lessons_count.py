from src.domain.entities.module_entity import ModuleEntity
from src.application.services.lesson_service import LessonService


class GetModuleLessonsCountQuery:

    def __init__(self, lesson_service):
        self.lesson_service = lesson_service

    async def execute(self, module_id: str) -> int:

        return await self.lesson_service.count_by_module.execute(module_id)
