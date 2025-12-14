from src.application.commands.admin_module.create_module import CreateModuleCommand
from src.application.commands.admin_module.update_module import UpdateModuleCommand
from src.application.commands.admin_module.delete_module import DeleteModuleCommand
from src.application.queries.admin_module.get_module import GetModuleQuery
from src.application.queries.admin_module.list_modules import ListModulesQuery
from src.domain.repositories.admin_module_repository import IAdminModuleRepository


class AdminModuleService:
    def __init__(self, repo: IAdminModuleRepository):
        self.create = CreateModuleCommand(repo)
        self.update = UpdateModuleCommand(repo)
        self.delete = DeleteModuleCommand(repo)
        self.get = GetModuleQuery(repo)
        self.list = ListModulesQuery(repo)
