from pydantic import BaseModel


class GrantCourseAccessDTO(BaseModel):
    user_id: str
    course_id: str
    

class RevokeCourseAccessDTO(BaseModel):
    user_id: str
    course_id: str