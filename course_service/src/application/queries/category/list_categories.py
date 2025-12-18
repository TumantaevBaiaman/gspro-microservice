from src.domain.dto.category import ListCategoriesResponseDTO
from src.domain.repositories.category_repository import ICategoryRepository


class ListCategoriesQuery:
    def __init__(self, repo: ICategoryRepository):
        self.repo = repo

    async def execute(self, limit: int, offset: int) -> ListCategoriesResponseDTO:
        items, total = await self.repo.list_categories(limit, offset)
        return ListCategoriesResponseDTO(items=items, total=total)
