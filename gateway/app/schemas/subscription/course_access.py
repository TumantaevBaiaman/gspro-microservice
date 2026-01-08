from pydantic import BaseModel


class GrantCourseAccessSchema(BaseModel):
    user_id: str
    course_id: str


class RevokeCourseAccessSchema(BaseModel):
    user_id: str
    course_id: str


class CheckCourseAccessSchema(BaseModel):
    user_id: str
    course_id: str


class CheckCourseAccessResponseSchema(BaseModel):
    has_access: bool
