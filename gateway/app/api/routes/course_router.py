from http.client import HTTPException

from fastapi import APIRouter, Query

from app.clients.course import course_client,  module_client
from app.schemas.course.course import *
from app.schemas.course.module import *

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


@router.get(
    "/{course_id}/modules",
    response_model=ModuleListResponseSchema,
    summary="List modules by course ID",
    description="Retrieve a list of modules associated with a specific course using the course's unique identifier.",
)
async def list_modules_by_course(course_id: str):
    data = module_client.list_modules_by_course(course_id)
    return ModuleListResponseSchema(items=[ModuleListItemSchema(**item) for item in data])


@router.get(
    "/{course_id}/modules/{module_id}",
    response_model=ModuleGetResponseSchema,
)
def get_course_module(course_id: str, module_id: str):
    module = module_client.get_module(module_id)

    if module["course_id"] != course_id:
        raise HTTPException(404, "Module not found")

    return module