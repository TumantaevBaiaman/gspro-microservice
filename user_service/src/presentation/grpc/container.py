from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.uow import UnitOfWork
from src.infrastructure.db.repositories import UserRepository, ProfileRepository
from src.application.services import UserService, ProfileService


class Container:
    def __init__(self, session: AsyncSession):
        self.uow = UnitOfWork(session)

        self.user_repo = UserRepository(session)
        self.profile_repo = ProfileRepository(session)

        self.user_service = UserService(self.user_repo)
        self.profile_service = ProfileService(self.profile_repo)
