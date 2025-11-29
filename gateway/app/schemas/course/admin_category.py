from pydantic import BaseModel

from typing import Optional


class AdminCategoryCreateRequestSchema(BaseModel):
    title: str
    codename: str
    parent_id: Optional[str] = None