from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.repositories.user_category_repository import IUserCategoryRepository
from src.infrastructure.db.models.user_category_model import UserCategoriesModel
from src.domain.entities.user_category_entity import UserCategoryEntity


class UserCategoryRepository(IUserCategoryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_category_to_user(self, user_id: UUID, categories: list[str]) -> None:
        for category_id in categories:
            user_category = UserCategoriesModel(
                user_id=user_id,
                category_id=category_id
            )
            self.session.add(user_category)
        await self.session.commit()

    async def remove_category_from_user(self, user_id: UUID, id: UUID) -> None:
        stmt = select(UserCategoriesModel).where(
            UserCategoriesModel.user_id == user_id,
            UserCategoriesModel.id == id
        )
        result = await self.session.execute(stmt)
        user_category = result.scalar_one_or_none()
        if user_category:
            await self.session.delete(user_category)
            await self.session.commit()

    async def get_user_categories(self,
            user_id: UUID,
            limit: int,
            offset: int,
    ) -> tuple[list[UserCategoriesModel], int]:
        stmt = select(UserCategoriesModel).where(
            UserCategoriesModel.user_id == user_id
        )
        count_stmt = select(func.count()).select_from(
            UserCategoriesModel
        ).where(
            UserCategoriesModel.user_id == user_id
        )
        result = await self.session.execute(stmt.limit(limit).offset(offset))
        categories = result.scalars().all()

        count_result = await self.session.execute(count_stmt)
        total = count_result.scalar_one()

        return categories, total

