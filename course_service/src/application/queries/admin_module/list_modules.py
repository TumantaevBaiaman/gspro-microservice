from src.domain.repositories.admin_module_repository import IAdminModuleRepository


class ListModulesQuery:
    def __init__(self, repo: IAdminModuleRepository):
        self.repo = repo

    async def execute(self, course_id: str | None = None):
        return await self.repo.list(course_id)
