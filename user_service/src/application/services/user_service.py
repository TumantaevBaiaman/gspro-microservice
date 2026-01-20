from src.application.commands.user.auth_google import AuthGoogleCommand
from src.application.commands.user.create_user_cli import CreateUserCLICommand
from src.application.commands.user.register_email import RegisterEmailCommand
from src.application.commands.user.refresh_tokens import RefreshTokensCommand
from src.application.commands.user.login_email import LoginEmailCommand
from src.application.commands.user.register_mentor import RegisterMentorCommand
from src.application.commands.user.request_password_reset import RequestPasswordResetCommand
from src.application.commands.user.confirm_password_reset import ConfirmPasswordResetCommand

from src.infrastructure.oauth.google_oauth_client import GoogleOAuthClient


class UserService:

    def __init__(self, user_repo):
        self.user_repo = user_repo
        
        self.auth_google = AuthGoogleCommand(user_repo, GoogleOAuthClient())
        self.register_by_email = RegisterEmailCommand(user_repo)
        self.refresh_tokens = RefreshTokensCommand(user_repo)
        self.login_by_email = LoginEmailCommand(user_repo)

        self.request_password_reset = RequestPasswordResetCommand(user_repo)
        self.confirm_password_reset = ConfirmPasswordResetCommand(user_repo)

        self.create_user_cli = CreateUserCLICommand(user_repo)
        self.create_mentor = RegisterMentorCommand(user_repo)


