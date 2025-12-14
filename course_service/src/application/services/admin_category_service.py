from src.application.commands.admin_category.create_category import CreateCategoryCommand
from src.application.commands.admin_category.update_category import UpdateCategoryCommand
from src.application.commands.admin_category.delete_category import DeleteCategoryCommand
from src.application.queries.admin_category.get_category import GetCategoryQuery
from src.application.queries.admin_category.list_categories import ListCategoriesQuery
from src.domain.repositories import IAdminCategoryRepository


class AdminCategoryService:
    def __init__(self, repo: IAdminCategoryRepository):
        self.create = CreateCategoryCommand(repo)
        self.update = UpdateCategoryCommand(repo)   # problem update method
        self.delete = DeleteCategoryCommand(repo)
        self.get = GetCategoryQuery(repo)
        self.list = ListCategoriesQuery(repo)
