from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.user_repository import IUserRepository
from src.infrastructure.db.models import UserProfileModel
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.db.models.auth_account_model import AuthAccountModel
from src.domain.enums import AuthProvider


class UserRepository(IUserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user):
        model = UserModel(id=user.id)
        self.session.add(model)
        await self.session.commit()
        return user

    async def create_auth_account(self, user_id, email, password_hash):
        model = AuthAccountModel(
            user_id=user_id,
            provider="email",
            identifier=email,
            password_hash=password_hash,
            verified=False,
        )
        self.session.add(model)
        await self.session.commit()

    async def get_auth_account_by_email(self, email: str):
        stmt = select(AuthAccountModel).where(
            AuthAccountModel.provider == AuthProvider.email,
            AuthAccountModel.identifier == email,
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id: UUID):
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create_user_profile(self, user_id: UUID):
        profile = UserProfileModel(user_id=user_id)
        self.session.add(profile)
        return profile
