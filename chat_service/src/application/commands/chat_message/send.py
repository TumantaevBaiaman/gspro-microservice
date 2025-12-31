from src.application.commands.chat_message.dto import (
    SendMessageDTO,
)
from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)


class SendMessageCommand:
    def __init__(self, repo: IChatMessageRepository):
        self.repo = repo

    async def execute(self, dto: SendMessageDTO):
        return await self.repo.send_message(
            scope=dto.scope,
            sender_id=dto.sender_id,
            participants=dto.participants,
            payload=dto.payload,
            course_id=dto.course_id,
            context=dto.context,
        )