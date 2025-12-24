from src.domain.repositories.module_repository import IModuleRepository
from src.domain.entities.module_entity import ModuleEntity


class GetModuleQuery:
    def __init__(self, repo: IModuleRepository):
        self.repo = repo

    async def __call__(self, module_id: str) -> ModuleEntity:
        module = await self.repo.get_by_id(module_id)
        if not module:
            raise ValueError("Module not found")
        return module