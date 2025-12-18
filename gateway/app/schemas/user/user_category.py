from pydantic import BaseModel


class CreateUserCategoryRequestSchema(BaseModel):
    categories: list[str]


class CreateUserCategoryResponseSchema(BaseModel):
    success: bool


class DeleteUserCategoryResponseSchema(BaseModel):
    success: bool


class UserCategoryListItemSchema(BaseModel):
    id: str
    category_id: str


class ListUserCategoriesResponseSchema(BaseModel):
    items: list[UserCategoryListItemSchema] = []
    total: int = 0



