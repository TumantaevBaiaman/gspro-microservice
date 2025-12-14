from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict

from app.clients.course import admin_lesson_client
from app.schemas.course.admin_lesson import *


admin_lesson_router = APIRouter(prefix="/lessons", tags=["Admin Lessons"])


@admin_lesson_router.post(
    "/create",
    response_model=AdminLessonCreateResponseSchema,
    summary="Create a new lesson",
    description="Endpoint to create a new lesson inside a module."
)
def create_lesson(data: AdminLessonCreateRequestSchema):
    response = admin_lesson_client.create_lesson(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminLessonCreateResponseSchema(**response_data)


@admin_lesson_router.get(
    "/{lesson_id}",
    response_model=AdminLessonGetResponseSchema,
    summary="Get lesson by ID",
    description="Endpoint to retrieve a lesson by its ID."
)
def get_lesson(lesson_id: str):
    response = admin_lesson_client.get_lesson(lesson_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminLessonGetResponseSchema(**response_data)


@admin_lesson_router.patch(
    "/{lesson_id}/update",
    response_model=AdminLessonUpdateResponseSchema,
    summary="Update lesson by ID",
    description="Endpoint to update a lesson by its ID."
)
def update_lesson(lesson_id: str, data: AdminLessonUpdateRequestSchema):
    response = admin_lesson_client.update_lesson(lesson_id, data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminLessonUpdateResponseSchema(**response_data)


@admin_lesson_router.delete(
    "/{lesson_id}/delete",
    response_model=AdminLessonDeleteResponseSchema,
    summary="Delete lesson by ID",
    description="Endpoint to delete a lesson by its ID."
)
def delete_lesson(lesson_id: str):
    response = admin_lesson_client.delete_lesson(lesson_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminLessonDeleteResponseSchema(**response_data)


@admin_lesson_router.get(
    "",
    response_model=AdminLessonListResponseSchema,
    summary="List lessons",
    description="Endpoint to retrieve lessons (optionally filtered by module)."
)
def list_lessons(module_id: str | None = None):
    response = admin_lesson_client.list_lessons(module_id=module_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminLessonListResponseSchema(**response_data)
