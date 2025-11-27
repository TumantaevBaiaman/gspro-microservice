from pydantic import BaseModel, EmailStr, field_validator
from app.domain.enums.auth_provider_enum import AuthProvider


class RegisterEmailRequestDTO(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class RegisterEmailResponseDTO(BaseModel):
    user_id: str
    email: str
    provider: str = AuthProvider.email.value
    verified: bool = False


class LoginEmailRequestDTO(BaseModel):
    email: EmailStr
    password: str


class LoginEmailResponseDTO(BaseModel):
    user_id: str
    email: str


class GetUserByEmailRequestDTO(BaseModel):
    user_id: str


class GetUserByEmailResponseDTO(BaseModel):
    user_id: str
