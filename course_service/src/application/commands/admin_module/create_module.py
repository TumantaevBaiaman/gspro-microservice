from src.domain.dto.admin_module_dto import AdminModuleCreateDTO
from src.domain.repositories.admin_module_repository import IAdminModuleRepository


class CreateModuleCommand:
    def __init__(self, repo: IAdminModuleRepository):
        self.repo = repo

    async def execute(self, dto: AdminModuleCreateDTO):
        return await self.repo.create(dto)
