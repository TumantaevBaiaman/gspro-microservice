from dataclasses import dataclass


@dataclass(frozen=True)
class ListUserFavoritesDTO:
    user_id: str
    limit: int
    offset: int


@dataclass(frozen=True)
class IsFavoriteDTO:
    user_id: str
    course_id: str
