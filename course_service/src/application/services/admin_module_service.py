from fastapi import HTTPException

from src.domain.dto.admin_module_dto import AdminModuleCreateDTO, AdminModuleUpdateDTO
from src.infrastructure.db.mongo.repositories.admin_module_repository import AdminModuleRepository


class AdminModuleService:
    def __init__(self):
        self.repo = AdminModuleRepository()

    async def create_module(self, dto: AdminModuleCreateDTO):
        return await self.repo.create(dto)

    async def get_module(self, module_id: str):
        module = await self.repo.get(module_id)
        if not module:
            raise HTTPException(404, "Module not found")
        return module

    async def delete_module(self, module_id: str):
        module = await self.get_module(module_id)
        await self.repo.delete(module)
        return True

    async def update_module(self, module_id: str, dto: AdminModuleUpdateDTO):
        module = await self.get_module(module_id)

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(module, key, value)

        return await self.repo.save(module)

    async def list_modules(self, course_id: str | None = None):
        return await self.repo.list(course_id)
