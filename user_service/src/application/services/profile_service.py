from src.application.queries.profile.get import GetProfileQuery
from src.application.commands.profile.update import UpdateProfileCommand
from src.domain.dto.profile_dto import (
    GetProfileResponseDTO,
    GetProfileRequestDTO,
)


class ProfileService:

    def __init__(self, repo):
        self.get_profile_by_user_id = GetProfileQuery(repo)
        self.update_profile = UpdateProfileCommand(repo)