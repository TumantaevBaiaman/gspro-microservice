# profile_client_sync.py
import grpc
from fastapi import HTTPException
from generated.user import profile_pb2_grpc, profile_pb2


class ProfileClientSync:

    def __init__(self):
        channel = grpc.insecure_channel("user_service:50051")
        self.stub = profile_pb2_grpc.UserProfileServiceStub(channel)

    def list_profiles_by_ids(self, user_ids: list[str]) -> list[dict]:
        if not user_ids:
            return []

        request = profile_pb2.ListProfilesByIdsRequest(user_ids=user_ids)

        try:
            response = self.stub.ListProfilesByIds(request)
            return [
                {
                    "user_id": item.user_id,
                    "full_name": item.full_name,
                    "avatar": item.avatar.thumb_medium_url if item.avatar else None,
                }
                for item in response.users
            ]
        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")

sync_profile_client = ProfileClientSync()