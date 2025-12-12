from fastapi import APIRouter, Depends

from google.protobuf.json_format import MessageToDict

from app.api.dependencies.auth import get_current_user
from app.clients.user import user_profile_client
from app.schemas.user.profile import GetUserProfileResponseSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_profile(user=Depends(get_current_user)):
    user_id = user.get("sub")

    profile = await user_profile_client.get_user_profile(user_id)
    profile_data = MessageToDict(profile, preserving_proto_field_name=True)

    return GetUserProfileResponseSchema(
        **profile_data
    )
