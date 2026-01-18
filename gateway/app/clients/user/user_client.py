import grpc.aio
from fastapi import HTTPException

from generated.user import user_pb2, user_pb2_grpc


class UserClient:
    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    async def register_email(self, data):
        request = user_pb2.RegisterEmailRequest(
            email=data.email,
            password=data.password,
            phone_number=data.phone_number,
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
            response = await self.stub.LoginEmail(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise HTTPException(401, e.details())
            raise HTTPException(500, "Internal error")

    async def auth_google(self, data):
        request = user_pb2.AuthGoogleRequest(token=data.token)
        try:
            response = await self.stub.AuthGoogle(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise HTTPException(status_code=401, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def refresh_tokens(self, data):
        request = user_pb2.RefreshTokenRequest(
            refresh_token=data.refresh_token
        )
        try:
            response = await self.stub.RefreshToken(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise HTTPException(401, e.details())
            raise HTTPException(500, "Internal error")

    async def request_password_reset(self, data):
        request = user_pb2.RequestPasswordResetRequest(
            email=data.email
        )
        try:
            response = await self.stub.RequestPasswordReset(request)
            return response
        except grpc.RpcError as e:
            raise HTTPException(status_code=400, detail=e.details())

    async def confirm_password_reset(self, data):
        request = user_pb2.ConfirmPasswordResetRequest(
            email=data.email,
            code=data.code,
            new_password=data.new_password,
        )
        try:
            response = await self.stub.ConfirmPasswordReset(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                raise HTTPException(status_code=400, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def register_mentor(self, data):
        request = user_pb2.RegisterMentorRequest(
            email=data.email,
            password=data.password,
            phone_number=data.phone_number,
            role="mentor",
        )

        try:
            response = await self.stub.RegisterMentor(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=e.details())
            raise HTTPException(status_code=400, detail=e.details())


user_client = UserClient()
