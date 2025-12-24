from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.profile_entity import ProfileEntity
from src.infrastructure.db.models import UserProfileModel


class IProfileRepository(ABC):

    @abstractmethod
    async def get_profile_by_user_id(self, user_id: UUID) -> UserProfileModel | None:
        pass

    @abstractmethod
    async def update_profile(self, profile_id: UUID, data: dict) -> ProfileEntity:
        pass

    @abstractmethod
    async def list_profiles(self, limit: int, offset: int) -> tuple[list[ProfileEntity], int]:
        pass

    @abstractmethod
    async def set_avatar_image(self, user_id: UUID, image_id: UUID) -> None:
        pass
