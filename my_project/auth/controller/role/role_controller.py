from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import role_service


class RoleController(GeneralController):
    _service = role_service