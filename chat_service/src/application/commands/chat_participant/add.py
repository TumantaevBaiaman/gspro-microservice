from src.application.commands.chat_participant.dto import AddChatParticipantDTO
from src.domain.repositories.chat_participant_repository import (
    IChatParticipantRepository,
)


class AddChatParticipantCommand:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: AddChatParticipantDTO) -> None:
        await self.repo.add_participant(
            chat_id=dto.chat_id,
            user_id=dto.user_id,
            role=dto.role,
        )