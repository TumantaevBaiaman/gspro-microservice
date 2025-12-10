from src.core.security.auth_jwt import create_access_token, create_refresh_token
from src.domain.dto.auth_dto import RegisterEmailRequestDTO, RegisterEmailResponseDTO
from src.core.security.password import hash_password
from src.domain.entities.user import User


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

        await self.user_repo.session.commit()

        access = create_access_token(str(user.id))
        refresh = create_refresh_token(str(user.id))

        return RegisterEmailResponseDTO(
            user_id=str(user.id),
            access_token=access,
            refresh_token=refresh
        )
