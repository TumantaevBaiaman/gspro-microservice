from pydantic import BaseModel
from typing import Optional


class AdminModuleCreateDTO(BaseModel):
    course_id: str
    title: str
    description: Optional[str] = None
    order_number: Optional[int] = None


class AdminModuleUpdateDTO(BaseModel):
    course_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    order_number: Optional[int] = None
