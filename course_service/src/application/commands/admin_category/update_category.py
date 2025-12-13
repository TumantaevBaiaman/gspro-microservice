from src.domain.dto.admin_category_dto import AdminCategoryUpdateDTO
from src.domain.repositories import IAdminCategoryRepository
from src.domain.exceptions.admin_category import (
    CategoryAlreadyExistsError,
    CategoryNotFoundError,
)


class UpdateCategoryCommand:
    def __init__(self, repo: IAdminCategoryRepository):
        self.repo = repo

    async def execute(self, category_id: str, dto: AdminCategoryUpdateDTO):
        category = await self.repo.get(category_id)
        if not category:
            raise CategoryNotFoundError("Category not found")

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        try:
            return await self.repo.save(category)
        except Exception:
            raise CategoryAlreadyExistsError("Codename already exists")
