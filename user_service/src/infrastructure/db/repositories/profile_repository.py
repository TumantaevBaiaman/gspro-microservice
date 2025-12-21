from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.profile_repository import IProfileRepository
from src.infrastructure.db.models.profile_model import UserProfileModel
from src.domain.entities.profile_entity import ProfileEntity


class ProfileRepository(IProfileRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_profile_by_user_id(self, user_id: UUID):
        stmt = select(UserProfileModel).where(UserProfileModel.user_id == user_id)

        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_profile(self, profile_id: UUID, data: dict) -> ProfileEntity:
        profile: ProfileEntity | None = await self.session.get(UserProfileModel, profile_id)
        if not profile:
            raise Exception("Profile not found")

        for key, value in data.items():
            if value is None or value == "":
                continue
            setattr(profile, key, value)

        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def list_profiles(
            self,
            limit: int,
            offset: int,
    ) -> tuple[list[UserProfileModel], int]:

        stmt = (
            select(UserProfileModel)
            .limit(limit)
            .offset(offset)
        )

        count_stmt = select(func.count()).select_from(UserProfileModel)

        result = await self.session.execute(stmt)
        profiles = result.scalars().all()

        count_result = await self.session.execute(count_stmt)
        total = count_result.scalar_one()

        return profiles, total

    async def set_avatar_image(self, user_id: UUID, image_id: UUID) -> None:
        stmt = select(UserProfileModel).where(UserProfileModel.user_id == user_id)

        result = await self.session.execute(stmt)
        profile: ProfileEntity | None = result.scalar_one_or_none()
        if not profile:
            raise Exception("Profile not found")

        profile.avatar_image_id = image_id

        await self.session.commit()