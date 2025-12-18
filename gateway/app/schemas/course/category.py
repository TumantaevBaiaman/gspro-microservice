from pydantic import BaseModel, Field


class CategoryGetRequestSchema(BaseModel):
    id: str


class CategoryGetResponseSchema(BaseModel):
    id: str
    title: str
    codename: str | None = None
    parent_id: str | None = None


class CategoryListItemSchema(BaseModel):
    id: str
    title: str
    codename: str | None = None
    parent_id: str | None = None


class CategoryListResponseSchema(BaseModel):
    items: list[CategoryListItemSchema]
    total: int = Field(..., example=20)