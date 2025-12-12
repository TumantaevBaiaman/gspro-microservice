from fastapi import APIRouter
from app.clients.user import user_client
from app.schemas.user.auth import (
    RegisterEmailRequestSchema,
    LoginEmailRequestSchema,
    RegisterEmailResponseSchema,
    LoginEmailResponseSchema,
    RefreshTokensRequestSchema,
    RefreshTokensResponseSchema
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/email/")
async def register_email(data: RegisterEmailRequestSchema) -> RegisterEmailResponseSchema:
    response = await user_client.register_email(data)
    return RegisterEmailResponseSchema(
        user_id=response.user_id,
        access_token=response.access_token,
        refresh_token=response.refresh_token,
    )


@router.post("/login/email/")
async def login_email(data: LoginEmailRequestSchema) -> LoginEmailResponseSchema:
    response = await user_client.login_email(data=data)
    return LoginEmailResponseSchema(
        user_id=response.user_id,
        access_token=response.access_token,
        refresh_token=response.refresh_token,
    )


@router.post("/refresh/")
async def refresh(data: RefreshTokensRequestSchema) -> RefreshTokensResponseSchema:
    response = await user_client.refresh_tokens(data=data)
    return RefreshTokensResponseSchema(
        access_token=response.access_token,
        refresh_token=response.refresh_token,
    )

