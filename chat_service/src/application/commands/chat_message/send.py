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
        participant_repo: IChatParticipantRepository,
    ):
        self.message_repo = message_repo
        self.participant_repo = participant_repo

    async def execute(self, dto: SendMessageDTO):
        is_member = await self.participant_repo.exists(
            chat_id=dto.chat_id,
            user_id=dto.sender_id,
        )
        if not is_member:
            raise PermissionError("User is not chat participant")

        return await self.message_repo.create(
            chat_id=dto.chat_id,
            sender_id=dto.sender_id,
            payload=dto.payload,
            context=dto.context,
        )
