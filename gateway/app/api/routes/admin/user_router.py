from fastapi import APIRouter, Depends, Query, UploadFile, File

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client, user_category_client, user_client
from app.schemas.user.auth import RegisterEmailRequestSchema
from app.schemas.user.profile import *
from app.schemas.user.user_category import *
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.image_validation import validate_image

user_router = APIRouter(prefix="/users", tags=["User"])

@user_router.post(
    "/register/mentor",
    summary="Register mentor with Email and Password",
    description="Endpoint to register a new users using email and password, returning access and refresh tokens."
)
async def register_email(data: RegisterEmailRequestSchema):
    response = await user_client.register_mentor(data)
    return MessageToDict(response)


@user_router.patch(
    "/mentor/{user_id}/update",
    summary="Update mentor with Email and Password",
    response_model=UpdateUserProfileResponseSchema,
    description="Endpoint to update the profile information of the currently authenticated users."
)
async def update_profile(data: UpdateUserProfileRequestSchema, user_id: str):
    await user_profile_client.update_user_profile(user_id, data)

    return UpdateUserProfileResponseSchema(
        success=True,
    )


@user_router.post(
    "/mentor/{user_id}/upload/avatar",
    response_model=SetAvatarResponseSchema,
    summary="Upload Mentor Avatar",
    description="Endpoint to upload and set users avatar image."
)
async def upload_avatar( user_id: str, file: UploadFile = File(...)):
    image_bytes = await validate_image(file)

    thumbnails = create_thumbnails(image_bytes)

    image_id, urls = await upload_image(
        original=image_bytes,
        thumbnails=thumbnails,
        path_prefix="users/avatar",
    )

    response = await user_profile_client.set_user_avatar(
        user_id=user_id,
        original_url=urls["original"],
        thumb_small_url=urls.get("small"),
        thumb_medium_url=urls.get("medium"),
    )

    return SetAvatarResponseSchema(
        image_id=response.image_id,
    )
