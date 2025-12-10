from pydantic import BaseModel, EmailStr, field_validator
from src.domain.enums.auth_provider_enum import AuthProvider


class RegisterEmailRequestDTO(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password too long: bcrypt supports only 72 bytes")
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v


class RegisterEmailResponseDTO(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str