from src.application.commands.profile.set_avatar import SetUserAvatarCommand
from src.application.queries.profile.get import GetProfileQuery
from src.application.commands.profile.update import UpdateProfileCommand
from src.application.queries.profile.list import ListProfilesQuery


class ProfileService:

    def __init__(self, profile_repo, image_repo):
        self.get_profile_by_user_id = GetProfileQuery(profile_repo)
        self.update_profile = UpdateProfileCommand(profile_repo)
        self.list_profiles = ListProfilesQuery(profile_repo)
        self.set_avatar = SetUserAvatarCommand(profile_repo=profile_repo, image_repo=image_repo)
