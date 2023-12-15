from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import channel_service


class ChannelController(GeneralController):
    _service = channel_service