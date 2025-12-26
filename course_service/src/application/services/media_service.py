from src.application.commands.media.upload_image import UploadImageCommand
from src.application.commands.media.upload_file import UploadFileCommand
from src.domain.repositories.image_repository import IImageRepository
from src.domain.repositories.file_repository import IFileRepository


class MediaService:
    def __init__(
        self,
        image_repo: IImageRepository,
        file_repo: IFileRepository,
    ):
        self.upload_image = UploadImageCommand(image_repo)
        self.upload_file = UploadFileCommand(file_repo)
