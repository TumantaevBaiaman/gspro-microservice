from abc import ABC, abstractmethod

from src.domain.entities.profile_entity import ProfileEntity


class IProfileRepository(ABC):

    @abstractmethod
    async def get_profile_by_user_id(self, user_id: str) -> ProfileEntity | None:
        pass
