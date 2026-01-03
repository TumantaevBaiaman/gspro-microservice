from src.domain.entities.module_entity import ModuleEntity
from src.application.services.lesson_service import LessonService


class GetCourseLessonsCountQuery:

    def __init__(self, lesson_service):
        self.lesson_service = lesson_service

    async def execute(self, course_id: str) -> int:
        modules = await ModuleEntity.find(
            ModuleEntity.course_id == course_id
        ).to_list()

        module_ids = [m.id for m in modules]

        if not module_ids:
            return 0

        total = 0
        for module_id in module_ids:
            total += await self.lesson_service.count_by_module.execute(module_id)

        return total
