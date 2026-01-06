from abc import ABC, abstractmethod
from src.domain.entities.lesson_entity import LessonEntity


class ILessonRepository(ABC):

    @abstractmethod
    async def get_by_id(self, lesson_id: str) -> LessonEntity:
        pass

    @abstractmethod
    async def list_by_module_id(self, module_id: str) -> list[LessonEntity]:
        pass

    @abstractmethod
    async def count_by_module_id(self, module_id: str) -> int:
        pass

    @abstractmethod
    async def has_free_lessons(self, module_id: str) -> bool:
        pass
