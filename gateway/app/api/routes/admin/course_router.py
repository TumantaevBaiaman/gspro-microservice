from fastapi import APIRouter, UploadFile, File
from google.protobuf.json_format import MessageToDict

from app.clients.course import admin_course_client
from app.clients.media import media_client
from app.schemas.course.admin_course import *
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.image_validation import validate_image

admin_course_router = APIRouter(prefix="/courses", tags=["Admin Courses"])


@admin_course_router.post(
    "/upload/cover-image",
    summary="Upload courses cover image",
    description="Endpoint to upload a cover image for a courses."
)
async def create_course(file: UploadFile = File(...),):
    image_bytes = await validate_image(file)

    thumbnails = create_thumbnails(image_bytes)

    _, urls = await upload_image(
        original=image_bytes,
        thumbnails=thumbnails,
        path_prefix="courses/cover_images",
    )

    media = media_client.create_media(
        kind="image",
        usage="cover",
        original_url=urls["original"],
        metadata={
            "filename": file.filename,
            "thumb_small_url": urls.get("small"),
            "thumb_medium_url": urls.get("medium"),
        },
    )

    return {
        "id": media["id"],
        "url": media["original_url"],
        "kind": media["kind"],
        "usage": media.get("usage"),
    }


@admin_course_router.post(
    "/create",
    response_model=AdminCourseCreateResponseSchema,
    summary="Create a new courses",
    description="Endpoint to create a new courses in the courses management system."
)
def create_course(data: AdminCourseCreateRequestSchema):
    response = admin_course_client.create_course(data)
    media_client.attach_media(
        owner_service="courses",
        owner_id=response.id,
        media_id=data.cover_image_id,
    )
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCourseCreateResponseSchema(
        **response_data
    )


@admin_course_router.get(
    "/{course_id}",
    response_model=AdminCourseGetResponseSchema,
    summary="Get courses by ID",
    description="Endpoint to retrieve a courses by its ID."
)
def get_course(course_id: str):
    response = admin_course_client.get_course(course_id)
    return AdminCourseGetResponseSchema(
        **response
    )


@admin_course_router.patch(
    "/{course_id}/update",
    response_model=AdminCourseUpdateResponseSchema,
    summary="Update courses by ID",
    description="Endpoint to update a courses by its ID."
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
    summary="Delete courses by ID",
    description="Endpoint to delete a courses by its ID."
)
def delete_course(course_id: str):
    response = admin_course_client.delete_course(course_id)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AdminCourseDeleteResponseSchema(
        **response_data
    )
