from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.chat.text_chat import TextChat


class TextChatDao(GeneralDAO):
    _domain_type = TextChat