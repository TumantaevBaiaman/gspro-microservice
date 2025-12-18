from fastapi import APIRouter, Depends, Query

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client
from app.schemas.user.profile import *

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
