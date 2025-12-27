from src.application.commands.user_experience.create import (
    CreateUserExperienceCommand,
)
from src.application.commands.user_experience.delete import (
    DeleteUserExperienceCommand,
)
from src.application.queries.user_experience.list import (
    ListUserExperiencesQuery,
)


class UserExperienceService:

    def __init__(self, experience_repo):
        self.create = CreateUserExperienceCommand(experience_repo)
        self.list_by_user = ListUserExperiencesQuery(experience_repo)
        self.delete = DeleteUserExperienceCommand(experience_repo)
