from typing import List
from src.domain.entities.module_entity import ModuleEntity
from src.domain.dto.admin_module_dto import AdminModuleCreateDTO, AdminModuleUpdateDTO


class AdminModuleRepository:

    async def create(self, dto: AdminModuleCreateDTO) -> ModuleEntity:
        module = ModuleEntity(**dto.model_dump())
        return await module.insert()

    async def get(self, module_id: str) -> ModuleEntity | None:
        return await ModuleEntity.get(module_id)

    async def list(self, course_id: str | None = None) -> List[ModuleEntity]:
        if course_id:
            return await ModuleEntity.find(ModuleEntity.course_id == course_id).to_list()
        return await ModuleEntity.find_all().to_list()

    async def save(self, module: ModuleEntity) -> ModuleEntity:
        return await module.save()

    async def delete(self, module: ModuleEntity):
        return await module.delete()
