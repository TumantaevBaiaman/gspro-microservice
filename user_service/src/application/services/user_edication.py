from src.application.commands.user_education.create import (
    CreateUserEducationCommand,
)
from src.application.commands.user_education.delete import (
    DeleteUserEducationCommand,
)
from src.application.queries.user_education.list import (
    ListUserEducationsQuery,
)


class UserEducationService:

    def __init__(self, education_repo):
        self.create = CreateUserEducationCommand(education_repo)
        self.list_by_user = ListUserEducationsQuery(education_repo)
        self.delete = DeleteUserEducationCommand(education_repo)
