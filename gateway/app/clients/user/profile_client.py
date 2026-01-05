import grpc.aio
from fastapi import HTTPException

from generated.user import profile_pb2_grpc, profile_pb2
from google.protobuf.json_format import MessageToDict


class ProfileClient:

    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = profile_pb2_grpc.UserProfileServiceStub(self.channel)

    async def get_user_profile(self, user_id: str):
        request = profile_pb2.GetUserProfileRequest(user_id=user_id)
        try:
            response = await self.stub.GetUserProfile(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def update_user_profile(self, user_id, data):
        request = profile_pb2.UpdateUserProfileRequest(
            user_id=user_id,
            full_name=data.full_name,
            bio=data.bio,
            date_of_birth=str(data.date_of_birth) if data.date_of_birth else "",
            city=data.city,
            industry=data.industry,
            experience_level=data.experience_level,
        )

        try:
            response = await self.stub.UpdateUserProfile(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def list_user_profiles(self, limit: int = 10, offset: int = 0):
        request = profile_pb2.ListUserProfilesRequest(limit=limit, offset=offset)
        try:
            response = await self.stub.ListUserProfiles(request)
            return response
        except grpc.RpcError as e:
            raise HTTPException(status_code=500, detail="Internal error")

    async def set_user_avatar(
            self,
            *,
            user_id: str,
            original_url: str,
            thumb_small_url: str | None,
            thumb_medium_url: str | None,
    ):
        request = profile_pb2.SetUserAvatarRequest(
            user_id=user_id,
            original_url=original_url,
            thumb_small_url=thumb_small_url or "",
            thumb_medium_url=thumb_medium_url or "",
        )
        try:
            return await self.stub.SetUserAvatar(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def list_profiles_by_ids(self, user_ids: list[str]) -> list[dict]:
        request = profile_pb2.ListProfilesByIdsRequest(user_ids=user_ids)

        try:
            response = await self.stub.ListProfilesByIds(request)

            return [
                {
                    "full_name": item.full_name,
                    "experience_level": item.experience_level,
                    "avatar": item.avatar.thumb_medium_url if item.avatar else None,
                }
                for item in response.users
            ]

        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")


user_profile_client = ProfileClient()
