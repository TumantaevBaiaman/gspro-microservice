import grpc.aio
from fastapi import HTTPException

from generated.user import user_certificate_pb2, user_certificate_pb2_grpc


class UserCertificateClient:

    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = user_certificate_pb2_grpc.UserCertificateServiceStub(self.channel)

    async def create(
        self,
        *,
        user_id: str,
        title: str,
        issuer: str | None,
        issued_at: str | None,
        link: str | None,
    ):
        request = user_certificate_pb2.CreateUserCertificateRequest(
            user_id=user_id,
            title=title,
            issuer=issuer or "",
            issued_at=issued_at,
            link=link or "",
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
        request = user_certificate_pb2.ListUserCertificatesRequest(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )

        try:
            return await self.stub.ListByUser(request)
        except grpc.RpcError:
            raise HTTPException(status_code=500, detail="Internal error")

    async def delete(self, certificate_id: str):
        request = user_certificate_pb2.DeleteUserCertificateRequest(
            certificate_id=certificate_id
        )

        try:
            return await self.stub.Delete(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")


user_certificate_client = UserCertificateClient()
