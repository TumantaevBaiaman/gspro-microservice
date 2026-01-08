from pymongo.errors import DuplicateKeyError

from src.application.commands.chat.dto import GetOrCreateChatDTO
from src.domain.repositories.chat_repository import IChatRepository


class GetOrCreateChatCommand:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: GetOrCreateChatDTO):
        chat = await self.repo.get_by_unique_key(dto.unique_key)
        if chat:
            return chat

        try:
            return await self.repo.create(
                type=dto.type,
                course_id=dto.course_id,
                unique_key=dto.unique_key,
            )
        except DuplicateKeyError:
            return await self.repo.get_by_unique_key(dto.unique_key)


