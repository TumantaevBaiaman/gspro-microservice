import grpc
from fastapi import HTTPException

from generated.user import user_pb2, user_pb2_grpc


class UserClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("user_service:50051")
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    async def register_email(self, data):
        request = user_pb2.RegisterEmailRequest(
            email=data.email,
            password=data.password,
        )
        try:
            response = await self.stub.RegisterEmail(request)
            return response
        except grpc.RpcError as e:
            status = e.code()
            message = e.details()

            if status == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=message)

            raise HTTPException(status_code=400, detail=message)


    async def login_email(self, data):
        request = user_pb2.LoginEmailRequest(
            email=data.email,
            password=data.password
        )
        try:
            return self.stub.LoginEmail(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise HTTPException(401, e.details())
            raise HTTPException(500, "Internal error")

    async def get_user(self, data):
        request = user_pb2.GetUserRequest(
            user_id=data.user_id
        )
        try:
            return await self.stub.GetUser(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(404, e.details())
            raise HTTPException(500, "Internal error")


user_client = UserClient()
