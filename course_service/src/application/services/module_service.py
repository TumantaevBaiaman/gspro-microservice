from src.application.queries.module.get import GetModuleQuery
from src.application.queries.module.get_lessons_count import GetModuleLessonsCountQuery
from src.application.queries.module.list import (
    ListModulesByCourseQuery
)
from src.domain.repositories.module_repository import IModuleRepository


class ModuleService:
    def __init__(self, repo: IModuleRepository, lesson_service):
        self.get = GetModuleQuery(repo)
        self.list_by_course = ListModulesByCourseQuery(repo)
        self.get_lessons_count = GetModuleLessonsCountQuery(lesson_service)

