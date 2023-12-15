from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import nitro_boost_service


class NitroBoostController(GeneralController):
    _service = nitro_boost_service