from src.domain.dto.admin_category_dto import AdminCategoryCreateDTO
from src.domain.repositories import IAdminCategoryRepository
from src.domain.exceptions.admin_category import CategoryAlreadyExistsError


class CreateCategoryCommand:
    def __init__(self, repo: IAdminCategoryRepository):
        self.repo = repo

    async def execute(self, dto: AdminCategoryCreateDTO):
        try:
            return await self.repo.create(dto)
        except Exception:
            raise CategoryAlreadyExistsError(
                "Category with this codename already exists"
            )
