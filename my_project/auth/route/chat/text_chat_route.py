from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import text_chat_controller
from my_project.auth.domain.chat.text_chat import TextChat

text_chat_bp = Blueprint("text_chat", __name__, url_prefix="/textChat/")

@text_chat_bp.route("", methods=["GET"])
def get_all_text_chats() -> Response:
    return make_response(jsonify(text_chat_controller.find_all()), HTTPStatus.OK)

@text_chat_bp.route('/<int:text_chat_id>', methods=["GET"])
def get_text_chat(text_chat_id: int) -> Response:
    return make_response(jsonify(text_chat_controller.find_by_id(text_chat_id)), HTTPStatus.OK)

@text_chat_bp.route('/<int:text_chat_id>', methods=["PUT"])
def update_text_chat(text_chat_id: int) -> Response:
    content = request.get_json()
    text_chat = TextChat.create_from_dto(content)
    text_chat_controller.update(text_chat_id, text_chat)
    return make_response("TextChat Updated", HTTPStatus.OK)

@text_chat_bp.route('/<int:text_chat_id>', methods=["PATCH"])
def patch_text_chat(text_chat_id: int) -> Response:
    content = request.get_json()
    text_chat_controller.patch(text_chat_id, content)
    return make_response("TextChat Updated", HTTPStatus.OK)

@text_chat_bp.route('/<int:text_chat_id>', methods=["DELETE"])
def delete_text_chat(text_chat_id: int) -> Response:
    text_chat_controller.delete(text_chat_id)
    return make_response("TextChat deleted", HTTPStatus.OK)

@text_chat_bp.route('', methods=["POST"])
def create_text_chat() -> Response:
    content = request.get_json()
    text_chat = TextChat.create_from_dto(content)
    text_chat_id = text_chat_controller.create(text_chat)
    return make_response(f"TextChat with id {text_chat_id} created", HTTPStatus.CREATED)

@text_chat_bp.route('/bulk', methods=["POST"])
def create_all_text_chats() -> Response:
    content = request.get_json()
    text_chats = [TextChat.create_from_dto(data) for data in content]
    text_chat_controller.create_all(text_chats)
    return make_response(text_chat_controller.create_all(text_chats), HTTPStatus.CREATED)

@text_chat_bp.route("/all", methods=["DELETE"])
def delete_all_text_chats() -> Response:
    text_chat_controller.delete_all()
    return make_response("All text chats deleted", HTTPStatus.OK)

