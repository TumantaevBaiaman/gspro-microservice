from src.application.commands.chat_message.dto import SendMessageDTO
from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)
from src.domain.repositories.chat_participant_repository import (
    IChatParticipantRepository,
)


class SendMessageCommand:

    def __init__(
        self,
        message_repo: IChatMessageRepository,
    ):
        self.message_repo = message_repo

    async def execute(self, dto: SendMessageDTO):

        message = await self.message_repo.create(
            chat_id=dto.chat_id,
            sender_id=dto.sender_id,
            payload=dto.payload,
            context=dto.context,
        )

        return message
