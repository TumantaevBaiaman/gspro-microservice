from pydantic import BaseModel

from typing import Optional


class AdminCategoryCreateRequestSchema(BaseModel):
    title: str
    codename: str
    parent_id: Optional[str] = None


class AdminCategoryCreateResponseSchema(BaseModel):
    id: str


class AdminCategoryGetRequestSchema(BaseModel):
    id: str


class AdminCategoryGetResponseSchema(BaseModel):
    id: str
    title: str
    codename: str
    parent_id: Optional[str] = None


class AdminCategoryUpdateRequestSchema(BaseModel):
    title: Optional[str] = None
    codename: Optional[str] = None
    parent_id: Optional[str] = None


class AdminCategoryUpdateResponseSchema(BaseModel):
    id: str
    title: str
    codename: str
    parent_id: Optional[str] = None


class AdminCategoryDeleteRequestSchema(BaseModel):
    id: str


class AdminCategoryDeleteResponseSchema(BaseModel):
    success: bool


