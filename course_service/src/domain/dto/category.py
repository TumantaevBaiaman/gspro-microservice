from dataclasses import dataclass

from src.domain.entities import CategoryEntity


@dataclass
class ListCategoriesResponseDTO:
    items: list[CategoryEntity]
    total: int
