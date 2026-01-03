from fastapi import APIRouter, Depends, Query, UploadFile, File

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client, user_category_client
from app.schemas.user.profile import *
from app.schemas.user.user_category import *
from app.services.media.image_upload_service import upload_image
from app.services.media.thumbnail_service import create_thumbnails
from app.utils.image_validation import validate_image

user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get(
    "/me/profile",
    response_model=GetUserProfileResponseSchema,
    summary="Get Current User Profile",
    description="Endpoint to retrieve the profile information of the currently authenticated user."
)
async def get_profile(user=Depends(get_current_user)):
    user_id = user.get("sub")

    profile = await user_profile_client.get_user_profile(user_id)
    profile_data = MessageToDict(profile, preserving_proto_field_name=True)

    return GetUserProfileResponseSchema(
        **profile_data
    )


@user_router.patch(
    "/me/profile",
    response_model=UpdateUserProfileResponseSchema,
    summary="Update Current User Profile",
    description="Endpoint to update the profile information of the currently authenticated user."
)
async def update_profile(data: UpdateUserProfileRequestSchema, user=Depends(get_current_user)):
    user_id = user.get("sub")
    await user_profile_client.update_user_profile(user_id, data)

    return UpdateUserProfileResponseSchema(
        success=True,
    )


@user_router.post(
    "/me/profile/avatar",
    response_model=SetAvatarResponseSchema,
    summary="Upload User Avatar",
    description="Endpoint to upload and set user avatar image."
)
async def upload_avatar(file: UploadFile = File(...), user=Depends(get_current_user)):
    user_id = user.get("sub")
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


@user_router.get(
    "/me/categories",
    response_model=ListUserCategoriesResponseSchema,
    summary="List Current User Categories",
    description="Endpoint to retrieve the list of categories associated with the currently authenticated user."
)
async def list_user_categories(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    user=Depends(get_current_user)
):
    user_id = user.get("sub")

    categories = await user_category_client.list_user_categories(
        user_id=user_id,
        limit=limit,
        offset=offset
    )
    categories_data = MessageToDict(categories, preserving_proto_field_name=True)
    return ListUserCategoriesResponseSchema(
        **categories_data
    )

@user_router.put(
    "/me/categories",
    response_model=CreateUserCategoryResponseSchema,
    summary="Update Current User Categories",
    description="Endpoint to update the categories associated with the currently authenticated user."
)
async def update_user_categories(
    data: CreateUserCategoryRequestSchema,
    user=Depends(get_current_user)
):
    user_id = user.get("sub")

    updated_categories = await user_category_client.create_user_category(
        user_id=user_id,
        data=data
    )
    updated_categories_data = MessageToDict(updated_categories, preserving_proto_field_name=True)
    return CreateUserCategoryResponseSchema(
        **updated_categories_data
    )

@user_router.delete(
    "/me/categories/{id}",
    response_model=DeleteUserCategoryResponseSchema,
    summary="Delete Current User Category",
    description="Endpoint to delete a category associated with the currently authenticated user."
)
async def delete_user_category(
    id: str,
    user=Depends(get_current_user)
):
    user_id = user.get("sub")

    await user_category_client.delete_user_category(
        user_id=user_id,
        id=id
    )
    return DeleteUserCategoryResponseSchema(success=True)
