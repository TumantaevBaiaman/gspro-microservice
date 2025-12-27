from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.user_experience_repository import (
    IUserExperienceRepository,
)
from src.infrastructure.db.models.user_experience_model import (
    UserExperienceModel,
)
from src.domain.entities.user_experience_entity import (
    UserExperienceEntity,
)


class UserExperienceRepository(IUserExperienceRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        experience: UserExperienceEntity,
    ) -> UserExperienceEntity:

        model = UserExperienceModel(
            user_id=experience.user_id,
            company=experience.company,
            position=experience.position,
            start_date=experience.start_date,
            end_date=experience.end_date,
            description=experience.description,
        )

        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

        return UserExperienceEntity(
            id=model.id,
            user_id=model.user_id,
            company=model.company,
            position=model.position,
            start_date=model.start_date,
            end_date=model.end_date,
            description=model.description,
            created_at=model.created_at,
        )

    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserExperienceModel], int]:

        stmt = (
            select(UserExperienceModel)
            .where(UserExperienceModel.user_id == user_id)
            .limit(limit)
            .offset(offset)
        )

        count_stmt = (
            select(func.count())
            .select_from(UserExperienceModel)
            .where(UserExperienceModel.user_id == user_id)
        )

        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_result = await self.session.execute(count_stmt)
        total = count_result.scalar_one()

        return items, total

    async def delete(self, experience_id: UUID) -> None:
        experience = await self.session.get(UserExperienceModel, experience_id)
        if not experience:
            raise Exception("Experience not found")

        await self.session.delete(experience)
        await self.session.commit()
