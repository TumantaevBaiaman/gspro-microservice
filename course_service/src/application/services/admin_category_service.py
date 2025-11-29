from src.domain.dto.admin_category_dto import AdminCategoryCreateDTO
from src.domain.repositories import AdminCategoryRepository


class AdminCategoryService:
    def __init__(self):
        self.category_repository = AdminCategoryRepository()

    async def admin_create_category(self, dto: AdminCategoryCreateDTO):
        return await self.category_repository.create_category(dto)


