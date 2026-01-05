from src.application.queries.category.get_category import GetCategoryQuery
from src.application.queries.category.list_categories import ListCategoriesQuery
from src.application.queries.category.list_by_ids import ListCategoriesByIdsQuery


class CategoryService:

    def __init__(self, repo):
        self.get = GetCategoryQuery(repo)
        self.list = ListCategoriesQuery(repo)
        self.list_by_ids = ListCategoriesByIdsQuery(repo)
