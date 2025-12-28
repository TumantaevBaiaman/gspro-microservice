from src.application.commands.app_feedback.dto import (
    CreateAppFeedbackDTO,
)


class CreateAppFeedbackCommand:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, dto: CreateAppFeedbackDTO):
        return await self.repo.create(
            user_id=dto.user_id,
            message=dto.message,
            type=dto.type,
            is_public=dto.is_public,
        )
