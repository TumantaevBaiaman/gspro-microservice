from src.domain.entities.user_category_entity import UserCategoryEntity
from src.domain.repositories.user_category_repository import IUserCategoryRepository


class CreateUserCategoryCommand:

    def __init__(self, repo: IUserCategoryRepository):
        self.repo = repo

    async def execute(self, user_id, categories) -> None:
        return await self.repo.add_category_to_user(user_id, categories)
