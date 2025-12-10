from pydantic import BaseModel, EmailStr, field_validator


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