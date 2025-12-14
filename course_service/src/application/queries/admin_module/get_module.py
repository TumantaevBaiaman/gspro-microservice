from src.domain.repositories.admin_module_repository import IAdminModuleRepository
from src.domain.exceptions.admin_module import ModuleNotFoundError


class GetModuleQuery:
    def __init__(self, repo: IAdminModuleRepository):
        self.repo = repo

    async def execute(self, module_id: str):
        module = await self.repo.get(module_id)
        if not module:
            raise ModuleNotFoundError("Module not found")
        return module
