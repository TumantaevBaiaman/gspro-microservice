from src.core.security.password import hash_password
from src.domain.entities.user import User
from src.domain.exceptions.user import UserAlreadyExistsError


class CreateUserCLICommand:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def execute(
        self,
        *,
        email: str,
        password: str,
        role: str,
        phone_number: str | None = None,
    ):
        acc = await self.user_repo.get_auth_account_by_email(email)
        if acc:
            raise UserAlreadyExistsError("User already exists")

        user = User.create(email=email, role=role)

        await self.user_repo.create_user(user)
        await self.user_repo.session.flush()

        await self.user_repo.create_auth_account(
            user.id,
            email,
            hash_password(password),
        )

        await self.user_repo.create_user_profile(
            user.id,
            phone_number,
        )

        return user
