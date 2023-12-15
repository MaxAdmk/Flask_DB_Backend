from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import audio_message_service


class AudioMessageController(GeneralController):
    _service = audio_message_service