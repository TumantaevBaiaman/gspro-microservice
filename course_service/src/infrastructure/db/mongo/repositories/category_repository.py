from src.domain.entities import CategoryEntity
from src.domain.repositories.category_repository import ICategoryRepository


class CategoryRepository(ICategoryRepository):

    async def get_category_by_id(self, category_id: str) -> CategoryEntity:
        return await CategoryEntity.get(category_id)

    async def list_categories(self, limit: int, offset: int) -> list[CategoryEntity]:
        query = CategoryEntity.find()

        total = await query.count()

        items = await (
            query
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total
