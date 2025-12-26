from dataclasses import dataclass


@dataclass(frozen=True)
class AddToFavoritesDTO:
    user_id: str
    course_id: str


@dataclass(frozen=True)
class RemoveFromFavoritesDTO:
    user_id: str
    course_id: str
