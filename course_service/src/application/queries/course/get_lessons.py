from src.domain.entities.module_entity import ModuleEntity
from src.application.services.lesson_service import LessonService


class GetCourseLessonsQuery:

    def __init__(self, lesson_service):
        self.lesson_service = lesson_service

    async def execute(self, course_id: str) -> list:
        modules = await ModuleEntity.find(
            ModuleEntity.course_id == course_id
        ).to_list()

        module_ids = [m.id for m in modules]
        if not module_ids:
            return []

        res = []
        for module_id in module_ids:
            lessons = await self.lesson_service.list_by_module.execute(str(module_id))
            if lessons:
                res.extend(lessons)

        return res
