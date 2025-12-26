import grpc.aio
from fastapi import HTTPException

from generated.user import user_experience_pb2, user_experience_pb2_grpc


class UserExperienceClient:

    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = user_experience_pb2_grpc.UserExperienceServiceStub(self.channel)

    async def create(
        self,
        *,
        user_id: str,
        company: str,
        position: str,
        start_date: str,
        end_date: str | None,
        description: str | None,
    ):
        request = user_experience_pb2.CreateUserExperienceRequest(
            user_id=user_id,
            company=company,
            position=position,
            start_date=start_date,
            end_date=end_date or "",
            description=description or "",
        )

        try:
            return await self.stub.Create(request)
        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")

    async def list_by_user(
        self,
        *,
        user_id: str,
        limit: int,
        offset: int,
    ):
        request = user_experience_pb2.ListUserExperiencesRequest(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )

        try:
            return await self.stub.ListByUser(request)
        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")

    async def delete(self, experience_id: str):
        request = user_experience_pb2.DeleteUserExperienceRequest(
            experience_id=experience_id
        )

        try:
            return await self.stub.Delete(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")


user_experience_client = UserExperienceClient()
