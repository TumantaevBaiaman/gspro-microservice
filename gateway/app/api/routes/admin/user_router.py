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