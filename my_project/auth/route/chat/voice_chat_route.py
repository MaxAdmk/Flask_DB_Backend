from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import voice_chat_controller
from my_project.auth.domain.chat.voice_chat import VoiceChat

voice_chat_bp = Blueprint("voice_chat", __name__, url_prefix="/voiceChat/")

@voice_chat_bp.route("", methods=["GET"])
def get_all_voice_chats() -> Response:
    return make_response(jsonify(voice_chat_controller.find_all()), HTTPStatus.OK)

@voice_chat_bp.route('/<int:voice_chat_id>', methods=["GET"])
def get_voice_chat(voice_chat_id: int) -> Response:
    return make_response(jsonify(voice_chat_controller.find_by_id(voice_chat_id)), HTTPStatus.OK)

@voice_chat_bp.route('/<int:voice_chat_id>', methods=["PUT"])
def update_voice_chat(voice_chat_id: int) -> Response:
    content = request.get_json()
    voice_chat = VoiceChat.create_from_dto(content)
    voice_chat_controller.update(voice_chat_id, voice_chat)
    return make_response("VoiceChat Updated", HTTPStatus.OK)

@voice_chat_bp.route('/<int:voice_chat_id>', methods=["PATCH"])
def patch_voice_chat(voice_chat_id: int) -> Response:
    content = request.get_json()
    voice_chat_controller.patch(voice_chat_id, content)
    return make_response("VoiceChat Updated", HTTPStatus.OK)

@voice_chat_bp.route('/<int:voice_chat_id>', methods=["DELETE"])
def delete_voice_chat(voice_chat_id: int) -> Response:
    voice_chat_controller.delete(voice_chat_id)
    return make_response("VoiceChat deleted", HTTPStatus.OK)

@voice_chat_bp.route('', methods=["POST"])
def create_voice_chat() -> Response:
    content = request.get_json()
    voice_chat = VoiceChat.create_from_dto(content)
    voice_chat_id = voice_chat_controller.create(voice_chat)
    return make_response(f"VoiceChat with id {voice_chat_id} created", HTTPStatus.CREATED)

@voice_chat_bp.route('/bulk', methods=["POST"])
def create_all_voice_chats() -> Response:
    content = request.get_json()
    voice_chats = [VoiceChat.create_from_dto(data) for data in content]
    voice_chat_controller.create_all(voice_chats)
    return make_response(voice_chat_controller.create_all(voice_chats), HTTPStatus.CREATED)

@voice_chat_bp.route("/all", methods=["DELETE"])
def delete_all_voice_chats() -> Response:
    voice_chat_controller.delete_all()
    return make_response("All voice chats deleted", HTTPStatus.OK)

