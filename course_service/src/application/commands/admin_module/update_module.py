from src.domain.dto.admin_module_dto import AdminModuleUpdateDTO
from src.domain.repositories.admin_module_repository import IAdminModuleRepository
from src.domain.exceptions.admin_module import ModuleNotFoundError


class UpdateModuleCommand:
    def __init__(self, repo: IAdminModuleRepository):
        self.repo = repo

    async def execute(self, module_id: str, dto: AdminModuleUpdateDTO):
        module = await self.repo.get(module_id)
        if not module:
            raise ModuleNotFoundError("Module not found")

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(module, key, value)

        return await self.repo.save(module)
