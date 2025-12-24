from src.domain.repositories.module_repository import IModuleRepository
from src.domain.entities.module_entity import ModuleEntity


class ListModulesByCourseQuery:
    def __init__(self, repo: IModuleRepository):
        self.repo = repo

    async def __call__(self, course_id: str) -> list[ModuleEntity]:
        return await self.repo.list_by_course_id(course_id)
