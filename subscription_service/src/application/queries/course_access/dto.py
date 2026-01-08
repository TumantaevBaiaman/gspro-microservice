from pydantic import BaseModel


class CheckCourseAccessDTO(BaseModel):
    user_id: str
    course_id: str