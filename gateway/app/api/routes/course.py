from fastapi import APIRouter

from app.clients.course import course_client
from app.schemas.course.course import CourseCreateRequestSchema

router = APIRouter(prefix="/courses", tags=["Course"])


@router.post("/create")
def create_course(data: CourseCreateRequestSchema):
    response = course_client.create_course(data)
    return {
        "id": response.id
    }
