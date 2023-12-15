from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import user_service


class UserController(GeneralController):
    _service = user_service