from my_project.auth.dao import nitro_boost_dao
from my_project.auth.service.general_service import GeneralService


class NitroBoostService(GeneralService):
    _dao = nitro_boost_dao