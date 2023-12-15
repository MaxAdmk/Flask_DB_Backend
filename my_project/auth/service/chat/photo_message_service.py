from my_project.auth.dao import photo_message_dao
from my_project.auth.service.general_service import GeneralService


class PhotoMessageService(GeneralService):
    _dao = photo_message_dao