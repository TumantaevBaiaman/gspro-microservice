from pydantic import BaseModel, EmailStr


class RegisterEmailRequestSchema(BaseModel):
    email: EmailStr
    password: str


class RegisterGoogleRequestSchema(BaseModel):
    google_token: str


class LoginEmailRequestSchema(BaseModel):
    email: EmailStr
    password: str
