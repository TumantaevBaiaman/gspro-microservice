from abc import ABC, abstractmethod
from src.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def create_auth_account(self, user_id, email, password_hash):
        pass

    @abstractmethod
    async def get_auth_account_by_email(self, email: str):
        pass

    #
    # @abstractmethod
    # async def get_by_email(self, email: str):
    #     pass
    #
    # @abstractmethod
    # async def get_by_id(self, email: str):
    #     pass


