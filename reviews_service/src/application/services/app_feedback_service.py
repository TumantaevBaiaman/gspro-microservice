from src.application.commands.app_feedback.create import (
    CreateAppFeedbackCommand,
)
from src.application.queries.app_feedback.list import (
    ListAppFeedbackQuery,
)
from src.domain.repositories.app_feedback_repository import (
    IAppFeedbackRepository,
)


class AppFeedbackService:
    def __init__(self, repo: IAppFeedbackRepository):
        self.create = CreateAppFeedbackCommand(repo)
        self.list = ListAppFeedbackQuery(repo)
