from src.application.commands.favorite_course.add import AddToFavoritesCommand
from src.application.commands.favorite_course.remove import RemoveFromFavoritesCommand
from src.application.queries.favorite_course.list_by_user import ListUserFavoritesQuery
from src.application.queries.favorite_course.is_favorite import IsFavoriteQuery
from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)


class FavoriteCourseService:
    def __init__(self, repo: IFavoriteCourseRepository):
        self.add = AddToFavoritesCommand(repo)
        self.remove = RemoveFromFavoritesCommand(repo)
        self.list_by_user = ListUserFavoritesQuery(repo)
        self.is_favorite = IsFavoriteQuery(repo)