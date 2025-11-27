from app.domain.dto.auth_dto import RegisterEmailRequestDTO, LoginEmailRequestDTO
from app.core.security.password import hash_password, verify_password
from app.domain.entities.user import User


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
            user_id=user.id,
            email=dto.email,
            password_hash=hash_password(dto.password)
        )

        return user

    async def login_by_email(self, dto: LoginEmailRequestDTO):
        user = await self.user_repo.get_by_email(dto.email)
        if not user:
            raise ValueError("User does not exist")

        if not verify_password(dto.password, user.password_hash):
            raise ValueError("Invalid credentials")

        return user
