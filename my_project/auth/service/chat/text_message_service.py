from my_project.auth.dao import text_message_dao
from my_project.auth.service.general_service import GeneralService


class TextMessageService(GeneralService):
    _dao = text_message_dao