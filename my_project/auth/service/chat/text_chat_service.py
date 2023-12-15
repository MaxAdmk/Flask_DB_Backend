from my_project.auth.dao import text_chat_dao
from my_project.auth.service.general_service import GeneralService


class TextChatService(GeneralService):
    _dao = text_chat_dao