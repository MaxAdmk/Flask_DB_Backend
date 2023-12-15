from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import role_controller
from my_project.auth.domain.role.role import Role

role_bp = Blueprint("role", __name__, url_prefix="/role/")

@role_bp.route("", methods=["GET"])
def get_all_roles() -> Response:
    return make_response(jsonify(role_controller.find_all()), HTTPStatus.OK)

@role_bp.route('/<int:role_id>', methods=["GET"])
def get_roles(role_id: int) -> Response:
    return make_response(jsonify(role_controller.find_by_id(role_id)), HTTPStatus.OK)

@role_bp.route('/<int:role_id>', methods=["PUT"])
def update_role(role_id: int) -> Response:
    content = request.get_json()
    role = Role.create_from_dto(content)
    role_controller.update(role_id, role)
    return make_response("Role Updated", HTTPStatus.OK)

@role_bp.route('/<int:role_id>', methods=["PATCH"])
def patch_role(role_id: int) -> Response:
    content = request.get_json()
    role_controller.patch(role_id, content)
    return make_response("Role Updated", HTTPStatus.OK)

@role_bp.route('/<int:role_id>', methods=["DELETE"])
def delete_role(role_id: int) -> Response:
    role_controller.delete(role_id)
    return make_response("Role deleted", HTTPStatus.OK)

@role_bp.route('', methods=["POST"])
def create_role() -> Response:
    content = request.get_json()
    role = Role.create_from_dto(content)
    role_id = role_controller.create(role)
    return make_response(f"Role with id {role_id} created", HTTPStatus.CREATED)

@role_bp.route('/bulk', methods=["POST"])
def create_all_roles() -> Response:
    content = request.get_json()
    roles = [Role.create_from_dto(data) for data in content]
    role_controller.create_all(roles)
    return make_response(role_controller.create_all(roles), HTTPStatus.CREATED)

@role_bp.route("/all", methods=["DELETE"])
def delete_all_roles() -> Response:
    role_controller.delete_all()
    return make_response("All roles deleted", HTTPStatus.OK)

