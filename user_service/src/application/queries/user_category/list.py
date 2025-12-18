from src.domain.entities.user_category_entity import UserCategoryEntity
from src.domain.repositories.user_category_repository import IUserCategoryRepository


class ListUserCategoriesQuery:
    def __init__(self, repo: IUserCategoryRepository):
        self.repo = repo

    async def execute(self, user_id, limit, offset) -> tuple[UserCategoryEntity, int]:
        return await self.repo.get_user_categories(user_id, limit, offset)
