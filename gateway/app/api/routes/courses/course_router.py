from http.client import HTTPException

from fastapi import APIRouter, Query

from app.aggregators.course.enrich_courses_with_cover import enrich_courses_with_cover, enrich_course, \
    get_course_mentors
from app.clients.course import course_client, module_client, category_client, lesson_client
from app.clients.media import media_client
from app.clients.review import course_review_client
from app.clients.user import user_profile_client
from app.schemas.course.course import *
from app.schemas.course.module import *

course_router = APIRouter(prefix="/courses", tags=["Course"])


@course_router.get(
    "/{course_id}",
    response_model=CourseGetResponseSchema,
    summary="Get courses by ID",
    description="Retrieve detailed information about a specific courses using its unique identifier.",
)
async def get_course(
        course_id: str,
        include_cover: bool = True,
        include_rating: bool = True,
        include_categories: bool = True,
        include_mentors: bool = True,
        include_author: bool = True,
):
    data = course_client.get_course(course_id)

    data = enrich_course(
        course=data,
        media_client=media_client,
        review_client=course_review_client,
        category_client=category_client,
        include_cover=include_cover,
        include_rating=include_rating,
        include_categories=include_categories,
    )

    if include_mentors:
        data["mentors"] = await get_course_mentors(
            mentor_ids=data.get("mentor_ids", []),
            user_profile_client=user_profile_client,
        )
    else:
        data["mentors"] = []

    if include_author and data.get("author_id"):
        author = await user_profile_client.get_user_profile(data["author_id"])
        data["author"] = {
            "id": data["author_id"],
            "full_name": author.full_name,
            "avatar": author.avatar.thumb_medium_url if author.avatar else None,
        } if author else None

    return CourseGetResponseSchema(**data)


@course_router.get(
    "",
    response_model=CourseListResponseSchema,
    summary="List courses",
    description="Retrieve a paginated list of courses.",
)
async def list_courses(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        mode: str = "all",
        author_id: str | None = None,
):
    data = course_client.list_courses(limit=limit, offset=offset, mode=mode, author_id=author_id)
    items = enrich_courses_with_cover(
        courses=data["items"],
        media_client=media_client,
    )
    return CourseListResponseSchema(
        total=data["total"],
        items=[CourseListItemSchema(**item) for item in items],
    )


@course_router.get(
    "/{course_id}/modules",
    response_model=ModuleListResponseSchema,
    summary="List modules by courses ID",
    description="Retrieve a list of modules associated with a specific courses using the courses's unique identifier.",
)
async def list_modules_by_course(course_id: str):
    data = module_client.list_modules_by_course(course_id)

    for module in data:
        files_count = 0

        lessons = lesson_client.list_lessons_by_module(module["id"])
        for lesson in lessons:
            files_count += len(
                media_client.list_media_by_owner(
                    owner_service="course",
                    owner_id=lesson["id"],
                    kind="file",
                    usage="lesson"
                )
            )

        module["files_count"] = files_count

    return ModuleListResponseSchema(
        items=[ModuleListItemSchema(**item) for item in data]
    )

@course_router.get(
    "/{course_id}/modules/{module_id}",
    response_model=ModuleGetResponseSchema,
    summary="Get module by ID within a courses",
    description="Retrieve detailed information about a specific module within a courses using the module's unique identifier.",
)
def get_course_module(course_id: str, module_id: str):
    module = module_client.get_module(module_id)

    if module["course_id"] != course_id:
        raise HTTPException(404, "Module not found")

    return module


@course_router.get(
    "/{course_id}/lessons",
    response_model=LessonListResponseSchema,
    summary="List lessons by course ID",
    description="Retrieve a list of lessons associated with a specific course.",
)
async def list_course_lessons(course_id: str):
    lessons = course_client.get_course_lessons(course_id)

    return LessonListResponseSchema(
        items=[LessonListItemSchema(**lesson) for lesson in lessons]
    )
