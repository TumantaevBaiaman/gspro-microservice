from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.user_education_repository import (
    IUserEducationRepository,
)
from src.infrastructure.db.models.user_education_model import (
    UserEducationModel,
)
from src.domain.entities.user_education_entity import (
    UserEducationEntity,
)


class UserEducationRepository(IUserEducationRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        education: UserEducationEntity,
    ) -> UserEducationEntity:

        model = UserEducationModel(
            user_id=education.user_id,
            institution=education.institution,
            degree=education.degree,
            start_year=education.start_year,
            end_year=education.end_year,
        )

        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

        return UserEducationEntity(
            id=model.id,
            user_id=model.user_id,
            institution=model.institution,
            degree=model.degree,
            start_year=model.start_year,
            end_year=model.end_year,
            created_at=model.created_at,
        )

    async def list_by_user_id(
        self,
        user_id: UUID,
        limit: int,
        offset: int,
    ) -> tuple[list[UserEducationModel], int]:

        stmt = (
            select(UserEducationModel)
            .where(UserEducationModel.user_id == user_id)
            .limit(limit)
            .offset(offset)
        )

        count_stmt = (
            select(func.count())
            .select_from(UserEducationModel)
            .where(UserEducationModel.user_id == user_id)
        )

        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_result = await self.session.execute(count_stmt)
        total = count_result.scalar_one()

        return items, total

    async def delete(self, education_id: UUID) -> None:
        education = await self.session.get(UserEducationModel, education_id)
        if not education:
            raise Exception("Education not found")

        await self.session.delete(education)
        await self.session.commit()
