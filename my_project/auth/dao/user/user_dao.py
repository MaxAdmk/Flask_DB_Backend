from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.user.user import User


class UserDao(GeneralDAO):
    _domain_type = User