from src.application.commands.media.create import CreateMediaCommand
from src.application.commands.media.attach import AttachMediaCommand
from src.application.commands.media.delete import SoftDeleteMediaCommand

from src.application.queries.media.get import GetMediaQuery
from src.application.queries.media.list_by_owner import ListMediaByOwnerQuery
from src.application.queries.media.get_batch import GetMediaBatchQuery

from src.domain.repositories.media_repository import IMediaRepository


class MediaService:
    def __init__(self, repo: IMediaRepository):
        self.create = CreateMediaCommand(repo)
        self.attach = AttachMediaCommand(repo)
        self.delete = SoftDeleteMediaCommand(repo)

        self.get = GetMediaQuery(repo)
        self.list_by_owner = ListMediaByOwnerQuery(repo)
        self.get_batch = GetMediaBatchQuery(repo)
