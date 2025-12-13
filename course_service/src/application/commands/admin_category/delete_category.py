from src.domain.repositories import IAdminCategoryRepository
from src.domain.exceptions.admin_category import CategoryNotFoundError


class DeleteCategoryCommand:
    def __init__(self, repo: IAdminCategoryRepository):
        self.repo = repo

    async def execute(self, category_id: str):
        category = await self.repo.get(category_id)
        if not category:
            raise CategoryNotFoundError("Category not found")

        await self.repo.delete(category)
        return True
