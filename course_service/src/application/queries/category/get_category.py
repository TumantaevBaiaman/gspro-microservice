from src.domain.repositories.category_repository import ICategoryRepository


class GetCategoryQuery:
    def __init__(self, repo: ICategoryRepository):
        self.repo = repo

    async def execute(self, category_id: str):
        return await self.repo.get_category_by_id(category_id)