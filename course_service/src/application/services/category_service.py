from src.application.queries.category.get_category import GetCategoryQuery
from src.application.queries.category.list_categories import ListCategoriesQuery


class CategoryService:

    def __init__(self, repo):
        self.get = GetCategoryQuery(repo)
        self.list = ListCategoriesQuery(repo)
