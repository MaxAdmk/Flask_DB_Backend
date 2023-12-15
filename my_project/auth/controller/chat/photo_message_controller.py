from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import photo_message_service


class PhotoMessageController(GeneralController):
    _service = photo_message_service