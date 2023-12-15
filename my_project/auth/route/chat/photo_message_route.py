from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import photo_message_controller
from my_project.auth.domain.chat.photo_message import PhotoMessage

photo_message_bp = Blueprint("photo_message", __name__, url_prefix="/photoMessage/")

@photo_message_bp.route("", methods=["GET"])
def get_all_photo_messages() -> Response:
    return make_response(jsonify(photo_message_controller.find_all()), HTTPStatus.OK)

@photo_message_bp.route('/<int:photo_message_id>', methods=["GET"])
def get_photo_message(photo_message_id: int) -> Response:
    return make_response(jsonify(photo_message_controller.find_by_id(photo_message_id)), HTTPStatus.OK)

@photo_message_bp.route('/<int:photo_message_id>', methods=["PUT"])
def update_photo_message(photo_message_id: int) -> Response:
    content = request.get_json()
    photo_message = PhotoMessage.create_from_dto(content)
    photo_message_controller.update(photo_message_id, photo_message)
    return make_response("PhotoMessage Updated", HTTPStatus.OK)

@photo_message_bp.route('/<int:photo_message_id>', methods=["PATCH"])
def patch_photo_message(photo_message_id: int) -> Response:
    content = request.get_json()
    photo_message_controller.patch(photo_message_id, content)
    return make_response("PhotoMessage Updated", HTTPStatus.OK)

@photo_message_bp.route('/<int:photo_message_id>', methods=["DELETE"])
def delete_photo_message(photo_message_id: int) -> Response:
    photo_message_controller.delete(photo_message_id)
    return make_response("PhotoMessage deleted", HTTPStatus.OK)

@photo_message_bp.route('', methods=["POST"])
def create_photo_message() -> Response:
    content = request.get_json()
    photo_message = PhotoMessage.create_from_dto(content)
    photo_message_id = photo_message_controller.create(photo_message)
    return make_response(f"PhotoMessage with id {photo_message_id} created", HTTPStatus.CREATED)

@photo_message_bp.route('/bulk', methods=["POST"])
def create_all_photo_messages() -> Response:
    content = request.get_json()
    photo_messages = [PhotoMessage.create_from_dto(data) for data in content]
    photo_message_controller.create_all(photo_messages)
    return make_response(photo_message_controller.create_all(photo_messages), HTTPStatus.CREATED)

@photo_message_bp.route("/all", methods=["DELETE"])
def delete_all_photo_messages() -> Response:
    photo_message_controller.delete_all()
    return make_response("All photo messages deleted", HTTPStatus.OK)

