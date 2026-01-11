from src.application.commands.user.auth_google import AuthGoogleCommand
from src.application.commands.user.create_user_cli import CreateUserCLICommand
from src.application.commands.user.register_email import RegisterEmailCommand
from src.application.commands.user.refresh_tokens import RefreshTokensCommand
from src.application.commands.user.login_email import LoginEmailCommand

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
from src.infrastructure.oauth.google_oauth_client import GoogleOAuthClient
from src.services.registration_service import verify_password


class UserService:

    def __init__(self, user_repo):
        self.user_repo = user_repo
        
        self.auth_google = AuthGoogleCommand(user_repo, GoogleOAuthClient())
        self.register_by_email = RegisterEmailCommand(user_repo)
        self.refresh_tokens = RefreshTokensCommand(user_repo)
        self.login_by_email = LoginEmailCommand(user_repo)

        self.create_user_cli = CreateUserCLICommand(user_repo)


