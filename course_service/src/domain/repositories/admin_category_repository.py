from src.domain.dto.admin_category_dto import AdminCategoryCreateDTO
from src.domain.entities import CategoryEntity


class AdminCategoryRepository:

    async def create_category(self, dto: AdminCategoryCreateDTO) -> CategoryEntity:
        category = CategoryEntity(**dto.dict())
        return await category.insert()
