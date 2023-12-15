from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import voice_chat_service


class VoiceChatController(GeneralController):
    _service = voice_chat_service