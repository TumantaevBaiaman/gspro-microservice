from fastapi import APIRouter

from google.protobuf.json_format import MessageToDict

from app.clients.user import user_client
from app.schemas.user.auth import *

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register/email",
    response_model=RegisterEmailResponseSchema,
    summary="Register with Email and Password",
    description="Endpoint to register a new user using email and password, returning access and refresh tokens."
)
async def register_email(data: RegisterEmailRequestSchema) -> RegisterEmailResponseSchema:
    response = await user_client.register_email(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return RegisterEmailResponseSchema(
        **response_data
    )


@router.post(
    "/login/email",
    response_model=LoginEmailResponseSchema,
    summary="Login with Email and Password",
    description="Endpoint to login a user using email and password, returning access and refresh tokens."
)
async def login_email(data: LoginEmailRequestSchema) -> LoginEmailResponseSchema:
    response = await user_client.login_email(data=data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return LoginEmailResponseSchema(
        **response_data
    )


@router.post(
    "/google",
    response_model=AuthGoogleResponseSchema,
    summary="Authenticate with Google OAuth",
    description="Endpoint to authenticate a user using Google OAuth token, returning access and refresh tokens."
)
async def auth_google(data: AuthGoogleRequestSchema) -> AuthGoogleResponseSchema:
    response = await user_client.auth_google(data=data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return AuthGoogleResponseSchema(
        **response_data
    )


@router.post(
    "/refresh",
    response_model=RefreshTokensResponseSchema,
    summary="Refresh Access and Refresh Tokens",
    description="Endpoint to refresh access and refresh tokens using a valid refresh token."
)
async def refresh(data: RefreshTokensRequestSchema) -> RefreshTokensResponseSchema:
    response = await user_client.refresh_tokens(data=data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return RefreshTokensResponseSchema(
       **response_data
    )

