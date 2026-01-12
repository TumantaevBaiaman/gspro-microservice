from pydantic import BaseModel, EmailStr


class RegisterEmailRequestSchema(BaseModel):
    email: EmailStr
    password: str
    phone_number: str


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


class AuthGoogleRequestSchema(BaseModel):
    token: str


class AuthGoogleResponseSchema(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str


class RequestPasswordResetRequestSchema(BaseModel):
    email: EmailStr


class ConfirmPasswordResetRequestSchema(BaseModel):
    email: EmailStr
    code: str
    new_password: str
