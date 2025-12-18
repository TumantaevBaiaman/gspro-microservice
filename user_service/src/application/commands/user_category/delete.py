from src.domain.repositories.user_category_repository import IUserCategoryRepository


class DeleteUserCategoryCommand:
    def __init__(self, repo: IUserCategoryRepository):
        self.repo = repo

    async def execute(self, user_id, id) -> None:
        await self.repo.remove_category_from_user(user_id, id)