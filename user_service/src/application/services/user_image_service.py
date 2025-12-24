from src.application.commands.user_image.set_avatar import SetUserAvatarCommand


class UserImageService:
    def __init__(self, image_repo, profile_repo):
        self.set_avatar = SetUserAvatarCommand(image_repo, profile_repo)