from fastapi import APIRouter, Depends, Query, UploadFile, File, HTTPException

from google.protobuf.json_format import MessageToDict

from app.clients.user import user_profile_client
from app.schemas.user.profile import *

router = APIRouter(prefix="/profiles", tags=["Profile"])


@router.get(
    "",
    response_model=ListUserProfilesResponseSchema,
    summary="List User Profiles",
    description="Endpoint to list user profiles with pagination support."
)
async def list_profiles(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    profiles = await user_profile_client.list_user_profiles(limit=limit, offset=offset)
    profiles_data = MessageToDict(profiles, preserving_proto_field_name=True)

    return ListUserProfilesResponseSchema(
        **profiles_data
    )