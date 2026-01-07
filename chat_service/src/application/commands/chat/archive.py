from src.application.commands.chat.dto import ArchiveChatDTO
from src.domain.repositories import IChatRepository


class ArchiveChatCommand:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: ArchiveChatDTO):
        chat = await self.repo.get_by_id(dto.chat_id)
        if not chat:
            return None

        chat.is_archived = True
        await chat.save()
        return chat