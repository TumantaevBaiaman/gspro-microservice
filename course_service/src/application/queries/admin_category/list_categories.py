from src.domain.repositories import IAdminCategoryRepository


class ListCategoriesQuery:
    def __init__(self, repo: IAdminCategoryRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.list()
