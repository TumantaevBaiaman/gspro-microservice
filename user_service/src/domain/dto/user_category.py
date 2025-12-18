from pydantic import BaseModel


class CreateUserCategoryRequestDTO(BaseModel):
    user_id: str
    category_id: str


class CreateUserCategoryResponseDTO(BaseModel):
    user_id: str
    category_id: str


class DeleteUserCategoryRequestDTO(BaseModel):
    user_id: str
    id: str


class DeleteUserCategoryResponseDTO(BaseModel):
    success: bool


class ListUserCategoriesRequestDTO(BaseModel):
    user_id: str


class ListUserCategoriesItemDTO(BaseModel):
    id: str
    user_id: str
    category_id: str


class ListUserCategoriesResponseDTO(BaseModel):
    items: list[ListUserCategoriesItemDTO]
    total: int


