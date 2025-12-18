from fastapi import APIRouter, Depends, Query

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client, user_category_client
from app.schemas.user.profile import *
from app.schemas.user.user_category import *

router = APIRouter(prefix="/users", tags=["User"])


@router.get(
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


@router.patch(
    "/me/profile",
    response_model=UpdateUserProfileRequestSchema,
    summary="Update Current User Profile",
    description="Endpoint to update the profile information of the currently authenticated user."
)
async def update_profile(data: UpdateUserProfileRequestSchema, user=Depends(get_current_user)):
    user_id = user.get("sub")

    updated_profile = await user_profile_client.update_user_profile(user_id, data)
    updated_profile_data = MessageToDict(updated_profile, preserving_proto_field_name=True)

    return UpdateUserProfileResponseSchema(
        **updated_profile_data
    )


@router.get(
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

@router.put(
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

@router.delete(
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
