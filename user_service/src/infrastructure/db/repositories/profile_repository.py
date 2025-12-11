from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.profile_repository import IProfileRepository
from src.infrastructure.db.models.profile_model import UserProfileModel
from src.domain.entities.profile_entity import ProfileEntity


class ProfileRepository(IProfileRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_profile(self, profile: ProfileEntity) -> ProfileEntity:
        pass

    async def get_profile_by_id(self, profile_id: UUID) -> ProfileEntity | None:
        stmt = select(UserProfileModel).where(UserProfileModel.id == profile_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()