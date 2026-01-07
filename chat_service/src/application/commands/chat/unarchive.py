from src.application.commands.chat.dto import UnarchiveChatDTO
from src.domain.repositories import IChatRepository


class UnarchiveChatCommand:

    def __init__(self, repo: IChatRepository):
        self.repo = repo

    async def execute(self, dto: UnarchiveChatDTO):
        chat = await self.repo.get_by_id(dto.chat_id)
        if not chat:
            return None

        chat.is_archived = False
        await chat.save()
        return chat
