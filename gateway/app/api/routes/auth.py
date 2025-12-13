from fastapi import APIRouter

from google.protobuf.json_format import MessageToDict

from app.clients.user import user_client
import app.schemas.user.auth as auth_schemas

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register/email/",
    response_model=auth_schemas.RegisterEmailResponseSchema,
    summary="Register with Email and Password",
    description="Endpoint to register a new user using email and password, returning access and refresh tokens."
)
async def register_email(data: auth_schemas.RegisterEmailRequestSchema) -> auth_schemas.RegisterEmailResponseSchema:
    response = await user_client.register_email(data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return auth_schemas.RegisterEmailResponseSchema(
        **response_data
    )


@router.post(
    "/login/email/",
    response_model=auth_schemas.LoginEmailResponseSchema,
    summary="Login with Email and Password",
    description="Endpoint to login a user using email and password, returning access and refresh tokens."
)
async def login_email(data: auth_schemas.LoginEmailRequestSchema) -> auth_schemas.LoginEmailResponseSchema:
    response = await user_client.login_email(data=data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return auth_schemas.LoginEmailResponseSchema(
        **response_data
    )


@router.post(
    "/refresh/",
    response_model=auth_schemas.RefreshTokensResponseSchema,
    summary="Refresh Access and Refresh Tokens",
    description="Endpoint to refresh access and refresh tokens using a valid refresh token."
)
async def refresh(data: auth_schemas.RefreshTokensRequestSchema) -> auth_schemas.RefreshTokensResponseSchema:
    response = await user_client.refresh_tokens(data=data)
    response_data = MessageToDict(response, preserving_proto_field_name=True)
    return auth_schemas.RefreshTokensResponseSchema(
       **response_data
    )

