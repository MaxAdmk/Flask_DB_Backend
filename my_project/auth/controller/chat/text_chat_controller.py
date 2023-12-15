from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import text_chat_service


class TextChatController(GeneralController):
    _service = text_chat_service