from fastapi import APIRouter, Depends

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client
import app.schemas.user.profile as profile_schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me",
    response_model=profile_schemas.GetUserProfileResponseSchema,
    summary="Get Current User Profile",
    description="Endpoint to retrieve the profile information of the currently authenticated user."
)
async def get_profile(user=Depends(get_current_user)):
    user_id = user.get("sub")

    profile = await user_profile_client.get_user_profile(user_id)
    profile_data = MessageToDict(profile, preserving_proto_field_name=True)

    return profile_schemas.GetUserProfileResponseSchema(
        **profile_data
    )


@router.patch(
    "/me",
    response_model=profile_schemas.UpdateUserProfileRequestSchema,
    summary="Update Current User Profile",
    description="Endpoint to update the profile information of the currently authenticated user."
)
async def update_profile(data: profile_schemas.UpdateUserProfileRequestSchema, user=Depends(get_current_user)):
    user_id = user.get("sub")

    updated_profile = await user_profile_client.update_user_profile(user_id, data)
    updated_profile_data = MessageToDict(updated_profile, preserving_proto_field_name=True)

    return profile_schemas.UpdateUserProfileResponseSchema(
        **updated_profile_data
    )