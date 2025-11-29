from pydantic import BaseModel
from typing import Optional


class AdminCategoryCreateDTO(BaseModel):
    title: str
    codename: str
    parent_id: Optional[str] = None
