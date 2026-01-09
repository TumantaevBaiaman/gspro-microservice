from src.application.commands.chat.archive import ArchiveChatCommand
from src.application.commands.chat.get_or_create import GetOrCreateChatCommand
from src.application.commands.chat.unarchive import UnarchiveChatCommand
from src.application.queries.chat.get_by_id import GetChatByIdQuery
from src.application.queries.chat.get_by_unique_key import GetChatByUniqueKeyQuery
from src.application.queries.chat.list_by_ids import ListChatsByIdsQuery
from src.domain.repositories import IChatRepository


class ChatService:

    def __init__(self, repo: IChatRepository):
        self.get_or_create = GetOrCreateChatCommand(repo)
        self.archive = ArchiveChatCommand(repo)
        self.unarchive = UnarchiveChatCommand(repo)

        self.get = GetChatByIdQuery(repo)
        self.get_by_unique_key = GetChatByUniqueKeyQuery(repo)
        self.list_by_ids = ListChatsByIdsQuery(repo)
