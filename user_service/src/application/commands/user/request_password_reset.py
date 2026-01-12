from src.core.security.reset_code import generate_reset_code, hash_code
from src.infrastructure.email.brevo_email_sender import BrevoEmailSender


class RequestPasswordResetCommand:

    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.email_sender = BrevoEmailSender()

    async def execute(self, email: str):
        auth_acc = await self.user_repo.get_auth_account_by_email(email)

        if not auth_acc:
            return

        code = generate_reset_code()
        code_hash = hash_code(code)

        await self.user_repo.create_password_reset_code(
            user_id=auth_acc.user_id,
            code_hash=code_hash,
        )

        await self.email_sender.send_password_reset_code(
            to=email,
            code=code,
        )
