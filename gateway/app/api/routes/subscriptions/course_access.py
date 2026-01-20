from fastapi import APIRouter, Depends

from app.aggregators.course.enrich_courses_with_cover import enrich_courses_with_cover
from app.api.dependencies.auth import get_current_user
from app.clients.course import course_client
from app.clients.media import media_client
from app.clients.subscription import (
    course_access_client,
)

from app.schemas.subscription.course_access import (
    CheckCourseAccessResponseSchema,
    CheckCourseAccessSchema,
    GrantCourseAccessSchema,
    RevokeCourseAccessSchema
)

course_access_router = APIRouter(
    prefix="",
    tags=["Course Access"],
)


@course_access_router.post("/courses-access/grant")
def grant_course_access(
    body: GrantCourseAccessSchema,
):
    return {
        "success": course_access_client.grant(
            user_id=body.user_id,
            course_id=body.course_id,
        )
    }


@course_access_router.post("/courses-access/revoke")
def revoke_course_access(
    body: RevokeCourseAccessSchema,
):
    return {
        "success": course_access_client.revoke(
            user_id=body.user_id,
            course_id=body.course_id,
        )
    }


@course_access_router.post(
    "/courses-access/check",
    response_model=CheckCourseAccessResponseSchema,
)
def check_course_access(
    body: CheckCourseAccessSchema,
):
    return {
        "has_access": course_access_client.has_access(
            user_id=body.user_id,
            course_id=body.course_id,
        )
    }


@course_access_router.get(
    "/me/courses"
)
def my_courses(user=Depends(get_current_user)):
    course_ids = course_access_client.list_user_courses(
        user_id=user["sub"]
    )
    if not course_ids:
        return []

    courses = course_client.list_courses_by_ids(course_ids)
    courses_data = enrich_courses_with_cover(
        courses=courses,
        media_client=media_client,
    )
    return courses_data