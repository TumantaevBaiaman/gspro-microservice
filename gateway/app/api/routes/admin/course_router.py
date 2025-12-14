from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict

from app.clients.course import admin_course_client
from app.schemas.course.admin_course import *


admin_course_router = APIRouter(prefix="/courses", tags=["Admin Courses"])


@admin_course_router.post(
    "/create",
    response_model=AdminCourseCreateResponseSchema,
    summary="Create a new course",
    description="Endpoint to create a new course in the course management system."
)
def create_course(data: AdminCourseCreateRequestSchema):
    response = admin_course_client.create_course(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCourseCreateResponseSchema(
        **response_data
    )


@admin_course_router.get(
    "/{course_id}",
    response_model=AdminCourseGetResponseSchema,
    summary="Get course by ID",
    description="Endpoint to retrieve a course by its ID."
)
def get_course(course_id: str):
    response = admin_course_client.get_course(course_id)
    return AdminCourseGetResponseSchema(
        **response
    )


@admin_course_router.patch(
    "/{course_id}/update",
    response_model=AdminCourseUpdateResponseSchema,
    summary="Update course by ID",
    description="Endpoint to update a course by its ID."
)
def update_course(course_id: str, data: AdminCourseUpdateRequestSchema):
    response = admin_course_client.update_course(course_id, data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCourseUpdateResponseSchema(
        **response_data
    )


@admin_course_router.delete(
    "/{course_id}/delete",
    response_model=AdminCourseDeleteResponseSchema,
    summary="Delete course by ID",
    description="Endpoint to delete a course by its ID."
)
def delete_course(course_id: str):
    response = admin_course_client.delete_course(course_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCourseDeleteResponseSchema(
        **response_data
    )
