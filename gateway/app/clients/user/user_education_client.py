import grpc.aio
from fastapi import HTTPException

from generated.user import user_education_pb2, user_education_pb2_grpc


class UserEducationClient:

    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = user_education_pb2_grpc.UserEducationServiceStub(self.channel)

    async def create(
        self,
        *,
        user_id: str,
        institution: str,
        degree: str | None,
        start_year: int | None,
        end_year: int | None,
    ):
        request = user_education_pb2.CreateUserEducationRequest(
            user_id=user_id,
            institution=institution,
            degree=degree or "",
            start_year=start_year or 0,
            end_year=end_year or 0,
        )

        try:
            return await self.stub.Create(request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=500, detail="Internal error")

    async def list_by_user(
        self,
        *,
        user_id: str,
        limit: int,
        offset: int,
    ):
        request = user_education_pb2.ListUserEducationsRequest(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )

        try:
            return await self.stub.ListByUser(request)
        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")

    async def delete(self, education_id: str):
        request = user_education_pb2.DeleteUserEducationRequest(
            education_id=education_id
        )

        try:
            return await self.stub.Delete(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")


user_education_client = UserEducationClient()
