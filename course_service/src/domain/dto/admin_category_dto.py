from pydantic import BaseModel
from typing import Optional


class AdminCategoryCreateDTO(BaseModel):
    title: str
    codename: str
    parent_id: Optional[str] = None


class AdminCategoryUpdateDTO(BaseModel):
    title: Optional[str] = None
    codename: Optional[str] = None
    parent_id: Optional[str] = None


class AdminCategoryGetDTO(BaseModel):
    id: str
    title: str
    codename: str
    parent_id: Optional[str] = None
