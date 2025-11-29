from fastapi import APIRouter
from app.clients.user import user_client
from app.schemas.auth import (
    RegisterEmailRequestSchema,
    LoginEmailRequestSchema,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/email")
async def register_email(data: RegisterEmailRequestSchema):
    response = await user_client.register_email(data)
    return {
        "user_id": response.user_id,
        "email": response.email
    }


@router.post("/login/email")
async def login_email(data: LoginEmailRequestSchema):
    response = await user_client.login_email(data=data)
    return {
        "user_id": response.user_id,
        "email": response.email
    }
