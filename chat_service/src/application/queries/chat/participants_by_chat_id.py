from src.domain.repositories import IChatParticipantRepository


class ListChatParticipantsByChatIdQuery:

    def __init__(
        self,
        chat_participant_repo: IChatParticipantRepository,
    ):
        self.chat_participant_repo = chat_participant_repo

    async def execute(
        self,
        chat_id: str,
    ) -> list[str]:

        if not chat_id:
            return []

        participants = await self.chat_participant_repo.list_by_chat_ids(
            chat_ids=[chat_id],
        )

        return [p.user_id for p in participants]
