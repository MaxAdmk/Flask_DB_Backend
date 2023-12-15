from my_project.auth.dao import role_dao
from my_project.auth.service.general_service import GeneralService


class RoleService(GeneralService):
    _dao = role_dao