from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import permission_list_service


class PermissionListController(GeneralController):
    _service = permission_list_service