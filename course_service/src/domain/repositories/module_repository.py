from abc import ABC, abstractmethod

from src.domain.entities.module_entity import ModuleEntity


class IModuleRepository(ABC):

    @abstractmethod
    async def get_by_id(self, module_id: str) -> ModuleEntity:
        pass

    @abstractmethod
    async def list_by_course_id(self, course_id: str) -> list[ModuleEntity]:
        pass
