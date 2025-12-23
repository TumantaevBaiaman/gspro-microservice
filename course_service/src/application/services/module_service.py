from src.application.queries.module.get import GetModuleQuery
from src.application.queries.module.list import (
    ListModulesByCourseQuery
)
from src.domain.repositories.module_repository import IModuleRepository


class ModuleService:
    def __init__(self, repo: IModuleRepository):
        self.get = GetModuleQuery(repo)
        self.list_by_course = ListModulesByCourseQuery(repo)
