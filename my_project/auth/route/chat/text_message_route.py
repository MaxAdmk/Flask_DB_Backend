from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import text_message_controller
from my_project.auth.domain.chat.text_message import TextMessage

text_message_bp = Blueprint("text_message", __name__, url_prefix="/textMessage/")

@text_message_bp.route("", methods=["GET"])
def get_all_text_messages() -> Response:
    return make_response(jsonify(text_message_controller.find_all()), HTTPStatus.OK)

@text_message_bp.route('/<int:text_message_id>', methods=["GET"])
def get_text_message(text_message_id: int) -> Response:
    return make_response(jsonify(text_message_controller.find_by_id(text_message_id)), HTTPStatus.OK)

@text_message_bp.route('/<int:text_message_id>', methods=["PUT"])
def update_photo_message(text_message_id: int) -> Response:
    content = request.get_json()
    text_message = TextMessage.create_from_dto(content)
    text_message_controller.update(text_message_id, text_message)
    return make_response("TextMessage Updated", HTTPStatus.OK)

@text_message_bp.route('/<int:text_message_id>', methods=["PATCH"])
def patch_text_message(text_message_id: int) -> Response:
    content = request.get_json()
    text_message_controller.patch(text_message_id, content)
    return make_response("TextMessage Updated", HTTPStatus.OK)

@text_message_bp.route('/<int:text_message_id>', methods=["DELETE"])
def delete_text_message(text_message_id: int) -> Response:
    text_message_controller.delete(text_message_id)
    return make_response("TextMessage deleted", HTTPStatus.OK)

@text_message_bp.route('', methods=["POST"])
def create_text_message() -> Response:
    content = request.get_json()
    text_message = TextMessage.create_from_dto(content)
    text_message_id = text_message_controller.create(text_message)
    return make_response(f"TextMessage with id {text_message_id} created", HTTPStatus.CREATED)

@text_message_bp.route('/bulk', methods=["POST"])
def create_all_text_messages() -> Response:
    content = request.get_json()
    text_messages = [TextMessage.create_from_dto(data) for data in content]
    text_message_controller.create_all(text_messages)
    return make_response(text_message_controller.create_all(text_messages), HTTPStatus.CREATED)

@text_message_bp.route("/all", methods=["DELETE"])
def delete_all_text_messages() -> Response:
    text_message_controller.delete_all()
    return make_response("All text messages deleted", HTTPStatus.OK)

