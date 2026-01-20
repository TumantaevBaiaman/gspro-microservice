from pydantic import BaseModel, EmailStr, field_validator

from src.domain.enums.user_role import UserRole

class RegisterEmailRequestDTO(BaseModel):
    email: EmailStr
    password: str
    phone_number: str
    role: str = UserRole.user.value

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v


class RegisterEmailResponseDTO(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str


class LoginEmailRequestDTO(BaseModel):
    email: EmailStr
    password: str


class LoginEmailResponseDTO(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str


class RefreshTokensRequestDTO(BaseModel):
    refresh_token: str


class RefreshTokensResponseDTO(BaseModel):
    access_token: str
    refresh_token: str


class AuthGoogleRequestDTO(BaseModel):
    token: str


class AuthGoogleResponseDTO(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str