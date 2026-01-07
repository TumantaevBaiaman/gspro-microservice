from src.application.commands.chat.dto import GetOrCreateChatDTO
from src.domain.repositories.chat_repository import IChatRepository


class GetOrCreateChatCommand:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: GetOrCreateChatDTO):
        return await self.repo.create(
            type=dto.type,
            course_id=dto.course_id,
            unique_key=dto.unique_key,
        )


