from pydantic import BaseModel, EmailStr


class RegisterEmailRequestSchema(BaseModel):
    email: EmailStr
    password: str


class RegisterEmailResponseSchema(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str


class LoginEmailRequestSchema(BaseModel):
    email: EmailStr
    password: str


class LoginEmailResponseSchema(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str


class RefreshTokensRequestSchema(BaseModel):
    refresh_token: str


class RefreshTokensResponseSchema(BaseModel):
    access_token: str
    refresh_token: str


