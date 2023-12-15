from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.role.permission_list import PermissionList


class PermissionListDao(GeneralDAO):
    _domain_type = PermissionList