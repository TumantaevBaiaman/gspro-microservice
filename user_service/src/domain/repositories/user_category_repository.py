from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities import UserCategoryEntity


class IUserCategoryRepository(ABC):

        @abstractmethod
        async def add_category_to_user(self, user_id: UUID, categories: list[str]) -> None:
            pass

        @abstractmethod
        async def remove_category_from_user(self, user_id: UUID, id: UUID) -> None:
            pass

        @abstractmethod
        async def get_user_categories(self, user_id: UUID, limit: int, offset: int) -> tuple[UserCategoryEntity, int]:
            pass
