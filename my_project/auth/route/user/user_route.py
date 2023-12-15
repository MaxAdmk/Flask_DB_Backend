from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import user_controller
from my_project.auth.domain.user.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user/")

@user_bp.route("", methods=["GET"])
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=["GET"])
def get_users(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=["PUT"])
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User Updated", HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=["PATCH"])
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User Updated", HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=["DELETE"])
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)

@user_bp.route('', methods=["POST"])
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_id = user_controller.create(user)
    return make_response(f"User with id {user_id} created", HTTPStatus.CREATED)

@user_bp.route('/bulk', methods=["POST"])
def create_all_users() -> Response:
    content = request.get_json()
    users = [User.create_from_dto(data) for data in content]
    user_controller.create_all(users)
    return make_response(user_controller.create_all(users), HTTPStatus.CREATED)

@user_bp.route("/all", methods=["DELETE"])
def delete_all_people() -> Response:
    user_controller.delete_all()
    return make_response("All users deleted", HTTPStatus.OK)

