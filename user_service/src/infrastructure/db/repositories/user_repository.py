from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.user import User
from src.domain.repositories.user_repository import IUserRepository
from src.infrastructure.db.models import UserProfileModel, PasswordResetCodeModel
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.db.models.auth_account_model import AuthAccountModel
from src.domain.enums import AuthProvider


class UserRepository(IUserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: User) -> None:
        model = UserModel(
            id=user.id,
            email=user.email,
            role=user.role,
            is_active=user.is_active,
        )
        self.session.add(model)


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

    async def create_user_profile(self, user_id: UUID, phone_number: str):
        profile = UserProfileModel(user_id=user_id, phone_number=phone_number)
        self.session.add(profile)
        return profile

    async def create_user_profile_google(self, user_id: UUID):
        profile = UserProfileModel(user_id=user_id)
        self.session.add(profile)
        return profile

    async def create_auth_account_google(self, user_id, email):
        model = AuthAccountModel(
            user_id=user_id,
            provider="google",
            identifier=email,
            verified=False,
        )
        self.session.add(model)
        await self.session.commit()

    async def update_password(
            self,
            user_id: UUID,
            new_password_hash: str,
    ):
        stmt = select(AuthAccountModel).where(
            AuthAccountModel.user_id == user_id,
            AuthAccountModel.provider == AuthProvider.email,
        )
        result = await self.session.execute(stmt)
        account = result.scalar_one()

        account.password_hash = new_password_hash
        await self.session.commit()

    async def create_password_reset_code(
            self,
            user_id: UUID,
            code_hash: str,
            ttl_minutes: int = 10,
    ):
        reset_code = PasswordResetCodeModel(
            user_id=user_id,
            code_hash=code_hash,
            expires_at=datetime.utcnow() + timedelta(minutes=ttl_minutes),
        )
        self.session.add(reset_code)
        await self.session.commit()
        return reset_code

    async def get_valid_password_reset_code(
            self,
            user_id: UUID,
            code_hash: str,
    ):
        stmt = select(PasswordResetCodeModel).where(
            PasswordResetCodeModel.user_id == user_id,
            PasswordResetCodeModel.code_hash == code_hash,
            PasswordResetCodeModel.used_at.is_(None),
            PasswordResetCodeModel.expires_at > datetime.utcnow(),
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def mark_password_reset_code_used(
            self,
            reset_code_id: UUID,
    ):
        stmt = select(PasswordResetCodeModel).where(
            PasswordResetCodeModel.id == reset_code_id
        )
        result = await self.session.execute(stmt)
        reset_code = result.scalar_one()

        reset_code.used_at = datetime.utcnow()
        await self.session.commit()