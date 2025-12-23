from fastapi import APIRouter, Query

from app.clients.course import course_client
from app.schemas.course.course import *

router = APIRouter(prefix="/courses", tags=["Course"])


@router.get(
    "/{course_id}",
    response_model=CourseGetResponseSchema,
    summary="Get course by ID",
    description="Retrieve detailed information about a specific course using its unique identifier.",
)
async def get_course(course_id: str):
    data = course_client.get_course(course_id)
    return CourseGetResponseSchema(**data)


@router.get(
    "",
    response_model=CourseListResponseSchema,
    summary="List courses",
    description="Retrieve a paginated list of courses.",
)
async def list_courses(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    data = course_client.list_courses(limit=limit, offset=offset)
    return CourseListResponseSchema(**data)

