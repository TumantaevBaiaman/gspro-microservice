from abc import ABC, abstractmethod

from src.domain.entities import CategoryEntity


class ICategoryRepository(ABC):

    @abstractmethod
    async def get_category_by_id(self, category_id: str) -> CategoryEntity:
        pass

    @abstractmethod
    async def list_categories(self, limit: int,  offset: int) -> list[CategoryEntity]:
        pass

    @abstractmethod
    async def get_categories_by_ids(
            self,
            ids: list[str],
    ) -> list[CategoryEntity]:
        pass
