from src.domain.dto.admin_category_dto import AdminCategoryCreateDTO
from src.domain.entities import CategoryEntity
from src.domain.repositories.admin_category_repository import IAdminCategoryRepository


class AdminCategoryRepository(IAdminCategoryRepository):

    async def create(self, dto: AdminCategoryCreateDTO) -> CategoryEntity:
        category = CategoryEntity(**dto.dict())
        return await category.insert()

    async def get(self, category_id: str) -> CategoryEntity | None:
        return await CategoryEntity.get(category_id)

    async def list(self):
        return await CategoryEntity.find_all().to_list()

    async def save(self, category: CategoryEntity) -> CategoryEntity:
        return await category.save()

    async def delete(self, category: CategoryEntity):
        return await category.delete()