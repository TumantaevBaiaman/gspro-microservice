from pydantic import BaseModel


class CourseCreateRequestSchema(BaseModel):
    title: str
    description: str
