from src.core.security.auth_jwt import create_access_token, create_refresh_token
from src.services.registration_service import verify_password
from src.domain.dto.auth_dto import (
    LoginEmailRequestDTO,
    LoginEmailResponseDTO,
)
from src.domain.exceptions.user import (
    InvalidCredentialsError,
    UserNotFoundError,
)


class LoginEmailCommand:

    def __init__(self, repo):
        self.repo = repo

    async def execute(
        self,
        dto: LoginEmailRequestDTO
    ) -> LoginEmailResponseDTO:

        acc = await self.repo.get_auth_account_by_email(dto.email)
        if not acc:
            raise InvalidCredentialsError("Invalid email or password")
        if not verify_password(dto.password, acc.password_hash):
            raise InvalidCredentialsError("Invalid email or password 2")

        user = await self.repo.get_user_by_id(acc.user_id)
        if not user:
            raise UserNotFoundError("User not found")

        return LoginEmailResponseDTO(
            user_id=str(user.id),
            access_token=create_access_token(str(user.id), user.role),
            refresh_token=create_refresh_token(str(user.id), user.role),
            role=user.role,
        )