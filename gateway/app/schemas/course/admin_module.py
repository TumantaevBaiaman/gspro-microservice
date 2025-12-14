from typing import Optional, List
from pydantic import BaseModel


class AdminModuleCreateRequestSchema(BaseModel):
    course_id: str
    title: str
    description: Optional[str] = None
    order_number: int


class AdminModuleCreateResponseSchema(BaseModel):
    id: str


class AdminModuleGetRequestSchema(BaseModel):
    id: str


class AdminModuleGetResponseSchema(BaseModel):
    id: str
    course_id: str
    title: str
    description: Optional[str] = None
    order_number: int


class AdminModuleUpdateRequestSchema(BaseModel):
    id: str
    course_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    order_number: Optional[int] = None


class AdminModuleUpdateResponseSchema(BaseModel):
    id: str


class AdminModuleDeleteRequestSchema(BaseModel):
    id: str


class AdminModuleDeleteResponseSchema(BaseModel):
    success: bool


class AdminModuleListRequestSchema(BaseModel):
    course_id: Optional[str] = None


class AdminModuleListResponseSchema(BaseModel):
    items: List[AdminModuleGetResponseSchema]
