from my_project.auth.dao import permission_list_dao
from my_project.auth.service.general_service import GeneralService


class PermissionListService(GeneralService):
    _dao = permission_list_dao