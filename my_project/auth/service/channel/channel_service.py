from my_project.auth.dao import channel_dao
from my_project.auth.service.general_service import GeneralService


class ChannelService(GeneralService):
    _dao = channel_dao