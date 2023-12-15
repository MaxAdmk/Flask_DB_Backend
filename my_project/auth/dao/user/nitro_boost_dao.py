from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.user.nitro_boost import NitroBoost


class NitroBoostDao(GeneralDAO):
    _domain_type = NitroBoost