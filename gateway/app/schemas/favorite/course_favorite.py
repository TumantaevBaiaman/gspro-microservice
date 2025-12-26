from pydantic import BaseModel


class FavoriteCourseSchema(BaseModel):
    id: str
    user_id: str
    course_id: str
    created_at: int


class AddToFavoritesRequestSchema(BaseModel):
    course_id: str


class RemoveFromFavoritesRequestSchema(BaseModel):
    course_id: str


class ListUserFavoritesResponseSchema(BaseModel):
    items: list[FavoriteCourseSchema]
    total: int


class IsFavoriteResponseSchema(BaseModel):
    is_favorite: bool
