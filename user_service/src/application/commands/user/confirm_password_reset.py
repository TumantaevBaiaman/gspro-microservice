from src.core.security.password import hash_password
from src.core.security.reset_code import hash_code
from src.domain.exceptions.user import InvalidResetCodeError


class ConfirmPasswordResetCommand:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def execute(self, email: str, code: str, new_password: str):
        auth_acc = await self.user_repo.get_auth_account_by_email(email)
        if not auth_acc:
            raise InvalidResetCodeError()

        code_hash = hash_code(code)

        reset = await self.user_repo.get_valid_password_reset_code(
            user_id=auth_acc.user_id,
            code_hash=code_hash,
        )

        if not reset:
            raise InvalidResetCodeError()

        await self.user_repo.update_password(
            user_id=auth_acc.user_id,
            new_password_hash=hash_password(new_password),
        )

        await self.user_repo.mark_password_reset_code_used(reset.id)
