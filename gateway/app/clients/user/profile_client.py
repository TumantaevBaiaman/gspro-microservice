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
            city=data.city,
            industry=data.industry,
            experience_level=data.experience_level,
        )

        try:
            response = await self.stub.UpdateUserProfile(request)
            return response
        except grpc.RpcError as e:
            print(e)
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")


user_profile_client = ProfileClient()
