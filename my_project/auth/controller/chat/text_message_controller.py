from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import text_message_service


class TextMessageController(GeneralController):
    _service = text_message_service