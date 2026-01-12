from fastapi import APIRouter

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
    prefix="/courses-access",
    tags=["Course Access"],
)


@course_access_router.post("/grant")
def grant_course_access(
    body: GrantCourseAccessSchema,
):
    return {
        "success": course_access_client.grant(
            user_id=body.user_id,
            course_id=body.course_id,
        )
    }


@course_access_router.post("/revoke")
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
    "/check",
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
