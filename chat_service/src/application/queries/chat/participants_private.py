from src.domain.repositories import IChatParticipantRepository, IChatRepository


class ListPrivateChatPeerQuery:

    def __init__(
        self,
        chat_repo: IChatRepository,
        chat_participant_repo: IChatParticipantRepository,
    ):
        self.chat_repo = chat_repo
        self.chat_participant_repo = chat_participant_repo

    async def execute(
        self,
        *,
        course_id,
        me_id: str,
    ) -> list | None:

        chats = await self.chat_repo.list_private_by_course(course_id)
        peers: set[str] = set()
        if not chats:
            return []

        for chat in chats:
            participants = await self.chat_participant_repo.list_by_chat_ids(
                chat_ids=[str(chat.id)],
            )

            for p in participants:
                if p.user_id != me_id:
                    peers.add(p.user_id)

        return list(peers)
