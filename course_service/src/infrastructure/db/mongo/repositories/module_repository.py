from src.domain.entities.module_entity import ModuleEntity
from src.domain.repositories.module_repository import IModuleRepository


class ModuleRepository(IModuleRepository):

    async def get_by_id(self, module_id: str) -> ModuleEntity:
        return await ModuleEntity.get(module_id)

    async def list_by_course_id(self, course_id: str) -> list[ModuleEntity]:
        return await (
            ModuleEntity.find(ModuleEntity.course_id == course_id)
            .sort("order_number")
            .to_list()
        )
