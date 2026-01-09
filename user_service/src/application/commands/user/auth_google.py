from src.application.ports.google_oauth_port import GoogleOAuthPort
from src.core.security.auth_jwt import create_access_token, create_refresh_token
from src.domain.dto.auth_dto import AuthGoogleResponseDTO, AuthGoogleRequestDTO
from src.domain.entities.user import User


class AuthGoogleCommand:

    def __init__(self, repo, google_oauth: GoogleOAuthPort):
        self.repo = repo
        self.google_oauth = google_oauth

    async def execute(self, dto: AuthGoogleRequestDTO):
        google_user = await self.google_oauth.get_user_info(dto.code)

        email = google_user.get("email")

        user = User.create(email)
        await self.repo.create_user(user)
        await self.repo.session.flush()
        await self.repo.create_auth_account_google(user.id, email)
        await self.repo.create_user_profile_google(user.id)
        await self.repo.session.commit()

        access = create_access_token(str(user.id), user.role)
        refresh = create_refresh_token(str(user.id), user.role)

        return AuthGoogleResponseDTO(
            user_id=str(user.id),
            access_token=access,
            refresh_token=refresh
        )