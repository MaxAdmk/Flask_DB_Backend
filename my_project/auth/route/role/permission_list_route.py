from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import permission_list_controller
from my_project.auth.domain.role.permission_list import PermissionList

permission_list_bp = Blueprint("permission_list", __name__, url_prefix="/permissionList/")

@permission_list_bp.route("", methods=["GET"])
def get_all_permission_lists() -> Response:
    return make_response(jsonify(permission_list_controller.find_all()), HTTPStatus.OK)

@permission_list_bp.route('/<int:permission_list_id>', methods=["GET"])
def get_permission_list(permission_list_id: int) -> Response:
    return make_response(jsonify(permission_list_controller.find_by_id(permission_list_id)), HTTPStatus.OK)

@permission_list_bp.route('/<int:permission_list_id>', methods=["PUT"])
def update_permission_list(permission_list_id: int) -> Response:
    content = request.get_json()
    permission_list = PermissionList.create_from_dto(content)
    permission_list_controller.update(permission_list_id, permission_list)
    return make_response("PermissionList Updated", HTTPStatus.OK)

@permission_list_bp.route('/<int:permission_list_id>', methods=["PATCH"])
def patch_permission_list(permission_list_id: int) -> Response:
    content = request.get_json()
    permission_list_controller.patch(permission_list_id, content)
    return make_response("PermissionList Updated", HTTPStatus.OK)

@permission_list_bp.route('/<int:permission_list_id>', methods=["DELETE"])
def delete_permission_list(permission_list_id: int) -> Response:
    permission_list_controller.delete(permission_list_id)
    return make_response("Role deleted", HTTPStatus.OK)

@permission_list_bp.route('', methods=["POST"])
def create_permission_list() -> Response:
    content = request.get_json()
    permission_list = PermissionList.create_from_dto(content)
    permission_list_id = permission_list_controller.create(permission_list)
    return make_response(f"PermissionList with id {permission_list_id} created", HTTPStatus.CREATED)

@permission_list_bp.route('/bulk', methods=["POST"])
def create_all_permission_lists() -> Response:
    content = request.get_json()
    permission_lists = [PermissionList.create_from_dto(data) for data in content]
    permission_list_controller.create_all(permission_lists)
    return make_response(permission_list_controller.create_all(permission_lists), HTTPStatus.CREATED)

@permission_list_bp.route("/all", methods=["DELETE"])
def delete_all_permission_lists() -> Response:
    permission_list_controller.delete_all()
    return make_response("All permission lists deleted", HTTPStatus.OK)

