from src.domain.repositories import ICategoryRepository


class ListCategoriesByIdsQuery:
    def __init__(self, repo: ICategoryRepository):
        self.repo = repo

    async def execute(self, ids: list[str]):
        return await self.repo.get_categories_by_ids(ids)
