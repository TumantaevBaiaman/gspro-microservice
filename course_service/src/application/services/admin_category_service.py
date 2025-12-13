from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

from src.domain.dto.admin_category_dto import AdminCategoryCreateDTO, AdminCategoryUpdateDTO
from src.domain.repositories import IAdminCategoryRepository


class AdminCategoryService:
    def __init__(self, repo: IAdminCategoryRepository):
        self.repo = repo

    async def create_category(self, dto: AdminCategoryCreateDTO):
        try:
            return await self.repo.create(dto)
        except DuplicateKeyError:
            raise HTTPException(409, "Category with this codename already exists")

    async def get_category(self, category_id: str):
        category = await self.repo.get(category_id)
        if not category:
            raise HTTPException(404, "Category not found")
        return category

    async def delete_category(self, category_id: str):
        category = await self.get_category(category_id)
        await self.repo.delete(category)
        return True

    async def update_category(self, category_id: str, dto: AdminCategoryUpdateDTO):
        category = await self.get_category(category_id)

        for key, value in dto.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        try:
            return await self.repo.save(category)
        except DuplicateKeyError:
            raise HTTPException(409, "Codename already exists")

    async def list_categories(self):
        return await self.repo.list()



