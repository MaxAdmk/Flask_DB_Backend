from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import audio_message_controller
from my_project.auth.domain.chat.audio_message import AudioMessage

audio_message_bp = Blueprint("audio_message", __name__, url_prefix="/audioMessage/")

@audio_message_bp.route("", methods=["GET"])
def get_all_audio_messages() -> Response:
    return make_response(jsonify(audio_message_controller.find_all()), HTTPStatus.OK)

@audio_message_bp.route('/<int:audio_message_id>', methods=["GET"])
def get_audio_message(audio_message_id: int) -> Response:
    return make_response(jsonify(audio_message_controller.find_by_id(audio_message_id)), HTTPStatus.OK)

@audio_message_bp.route('/<int:audio_message_id>', methods=["PUT"])
def update_audio_message(audio_message_id: int) -> Response:
    content = request.get_json()
    audio_message = AudioMessage.create_from_dto(content)
    audio_message_controller.update(audio_message_id, audio_message)
    return make_response("AudioMessage Updated", HTTPStatus.OK)

@audio_message_bp.route('/<int:audio_message_id>', methods=["PATCH"])
def patch_audio_message(audio_message_id: int) -> Response:
    content = request.get_json()
    audio_message_controller.patch(audio_message_id, content)
    return make_response("AudioMessage Updated", HTTPStatus.OK)

@audio_message_bp.route('/<int:audio_message_id>', methods=["DELETE"])
def delete_audio_message(audio_message_id: int) -> Response:
    audio_message_controller.delete(audio_message_id)
    return make_response("AudioMessage deleted", HTTPStatus.OK)

@audio_message_bp.route('', methods=["POST"])
def create_audio_message() -> Response:
    content = request.get_json()
    audio_message = AudioMessage.create_from_dto(content)
    audio_message_id = audio_message_controller.create(audio_message)
    return make_response(f"AudioMessage with id {audio_message_id} created", HTTPStatus.CREATED)

@audio_message_bp.route('/bulk', methods=["POST"])
def create_all_audio_messages() -> Response:
    content = request.get_json()
    audio_messages = [AudioMessage.create_from_dto(data) for data in content]
    audio_message_controller.create_all(audio_messages)
    return make_response(audio_message_controller.create_all(audio_messages), HTTPStatus.CREATED)

@audio_message_bp.route("/all", methods=["DELETE"])
def delete_all_audio_messages() -> Response:
    audio_message_controller.delete_all()
    return make_response("All audio messages deleted", HTTPStatus.OK)

