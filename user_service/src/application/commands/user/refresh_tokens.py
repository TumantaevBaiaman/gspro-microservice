from src.core.security.auth_jwt import (
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
)
from src.domain.dto.auth_dto import (
    RefreshTokensRequestDTO,
    RefreshTokensResponseDTO,
)
from src.domain.exceptions.user import (
    InvalidRefreshTokenError,
    UserNotFoundError,
)


class RefreshTokensCommand:

    def __init__(self, repo):
        self.repo = repo

    async def execute(
        self,
        dto: RefreshTokensRequestDTO
    ) -> RefreshTokensResponseDTO:

        payload = verify_refresh_token(dto.refresh_token)
        if payload is None:
            raise InvalidRefreshTokenError("Invalid refresh token")

        user_id = payload["sub"]

        user = await self.repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")

        return RefreshTokensResponseDTO(
            access_token=create_access_token(str(user_id), user.role),
            refresh_token=create_refresh_token(str(user_id), user.role),
        )
