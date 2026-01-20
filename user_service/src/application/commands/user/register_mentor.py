from src.core.security.auth_jwt import create_access_token, create_refresh_token
from src.core.security.password import hash_password
from src.domain.entities.user import User
from src.domain.dto.auth_dto import (
    RegisterEmailRequestDTO,
    RegisterEmailResponseDTO,
)
from src.domain.exceptions.user import UserAlreadyExistsError


class RegisterMentorCommand:

    def __init__(self, repo):
        self.repo = repo

    async def execute(
        self,
        dto: RegisterEmailRequestDTO
    ):

        acc = await self.repo.get_auth_account_by_email(dto.email)
        if acc:
            raise UserAlreadyExistsError("User already exists")

        user = User.create(dto.email, dto.role)

        await self.repo.create_user(user)
        await self.repo.session.flush()

        await self.repo.create_auth_account(
            user.id,
            dto.email,
            hash_password(dto.password)
        )
        await self.repo.create_user_profile(
            user.id,
            dto.phone_number
        )

        return True
