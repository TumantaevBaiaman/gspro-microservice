from src.application.commands.chat.archive import ArchiveChatCommand
from src.application.commands.chat.get_or_create import GetOrCreateChatCommand
from src.application.commands.chat.unarchive import UnarchiveChatCommand
from src.application.queries.chat.get_by_id import GetChatByIdQuery
from src.application.queries.chat.get_by_unique_key import GetChatByUniqueKeyQuery
from src.application.queries.chat.list_by_ids import ListChatsByIdsQuery
from src.application.queries.chat.list_user_chats import ListUserChatsQuery
from src.application.queries.chat.participants_by_chat_id import ListChatParticipantsByChatIdQuery
from src.application.queries.chat.participants_private import ListPrivateChatPeerQuery
from src.domain.repositories import IChatRepository, IChatParticipantRepository


class ChatService:

    def __init__(self, repo: IChatRepository, chat_participant_repo: IChatParticipantRepository):
        self.get_or_create = GetOrCreateChatCommand(repo)
        self.archive = ArchiveChatCommand(repo)
        self.unarchive = UnarchiveChatCommand(repo)

        self.get = GetChatByIdQuery(repo)
        self.get_by_unique_key = GetChatByUniqueKeyQuery(repo)
        self.list_by_ids = ListChatsByIdsQuery(repo)
        self.list_user_chats = ListUserChatsQuery(repo, chat_participant_repo)
        self.list_participants = ListChatParticipantsByChatIdQuery(chat_participant_repo)
        self.list_participants_private = ListPrivateChatPeerQuery(repo, chat_participant_repo)
