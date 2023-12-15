from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.role.role import Role


class RoleDao(GeneralDAO):
    _domain_type = Role