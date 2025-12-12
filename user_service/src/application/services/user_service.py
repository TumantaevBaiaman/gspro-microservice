from src.core.security.auth_jwt import create_access_token, create_refresh_token, verify_refresh_token
from src.domain.dto.auth_dto import (
    RegisterEmailRequestDTO,
    RegisterEmailResponseDTO,
    LoginEmailResponseDTO,
    LoginEmailRequestDTO,
    RefreshTokensRequestDTO,
    RefreshTokensResponseDTO
)
from src.core.security.password import hash_password
from src.domain.entities.user import User
from src.services.registration_service import verify_password


class UserService:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def register_by_email(self, dto: RegisterEmailRequestDTO):
        acc = await self.user_repo.get_auth_account_by_email(dto.email)
        if acc:
            raise ValueError("User already exists")

        user = User.create()

        await self.user_repo.create_user(user)
        await self.user_repo.create_auth_account(
            user.id,
            dto.email,
            hash_password(dto.password)
        )
        await self.user_repo.create_user_profile(user.id)

        await self.user_repo.session.commit()

        access = create_access_token(str(user.id))
        refresh = create_refresh_token(str(user.id))

        return RegisterEmailResponseDTO(
            user_id=str(user.id),
            access_token=access,
            refresh_token=refresh
        )

    async def login_by_email(self, dto: LoginEmailRequestDTO):
        acc = await self.user_repo.get_auth_account_by_email(dto.email)
        if not acc:
            raise ValueError("Invalid email or password")

        if not verify_password(dto.password, acc.password_hash):
            raise ValueError("Invalid email or password")

        user = await self.user_repo.get_user_by_id(acc.user_id)
        if not user:
            raise ValueError("User not found")

        access = create_access_token(str(user.id))
        refresh = create_refresh_token(str(user.id))

        return LoginEmailResponseDTO(
            user_id=str(user.id),
            access_token=access,
            refresh_token=refresh
        )

    async def refresh_tokens(self, dto: RefreshTokensRequestDTO):
        payload = verify_refresh_token(dto.refresh_token)
        if payload is None:
            raise ValueError("Invalid refresh token")

        user_id = payload["sub"]

        user = await self.user_repo.get_user_by_id(user_id)
        if user is None:
            raise ValueError("User not found")

        access = create_access_token(str(user_id))
        refresh = create_refresh_token(str(user_id))

        return RefreshTokensResponseDTO(
            access_token=access,
            refresh_token=refresh
        )
