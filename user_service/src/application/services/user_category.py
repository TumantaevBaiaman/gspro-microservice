from src.application.commands.user_category.create import CreateUserCategoryCommand
from src.application.commands.user_category.delete import DeleteUserCategoryCommand
from src.application.queries.user_category.list import ListUserCategoriesQuery


class UserCategoryService:

    def __init__(self, repo):
        self.create_user_category = CreateUserCategoryCommand(repo)
        self.delete_user_category = DeleteUserCategoryCommand(repo)
        self.list_user_categories = ListUserCategoriesQuery(repo)