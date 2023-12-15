from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import channel_controller
from my_project.auth.domain.channel.channel import Channel

channel_bp = Blueprint("channel", __name__, url_prefix="/channel/")

@channel_bp.route("", methods=["GET"])
def get_all_channels() -> Response:
    return make_response(jsonify(channel_controller.find_all()), HTTPStatus.OK)

@channel_bp.route('/<int:channel_id>', methods=["GET"])
def get_channel(channel_id: int) -> Response:
    return make_response(jsonify(channel_controller.find_by_id(channel_id)), HTTPStatus.OK)

@channel_bp.route('/<int:channel_id>', methods=["PUT"])
def update_channel(channel_id: int) -> Response:
    content = request.get_json()
    channel = Channel.create_from_dto(content)
    channel_controller.update(channel_id, channel)
    return make_response("Channel Updated", HTTPStatus.OK)

@channel_bp.route('/<int:channel_id>', methods=["PATCH"])
def patch_channel(channel_id: int) -> Response:
    content = request.get_json()
    channel_controller.patch(channel_id, content)
    return make_response("Channel Updated", HTTPStatus.OK)

@channel_bp.route('/<int:channel_id>', methods=["DELETE"])
def delete_channel(channel_id: int) -> Response:
    channel_controller.delete(channel_id)
    return make_response("Channel deleted", HTTPStatus.OK)

@channel_bp.route('', methods=["POST"])
def create_channel() -> Response:
    content = request.get_json()
    channel = Channel.create_from_dto(content)
    channel_id = channel_controller.create(channel)
    return make_response(f"Channel with id {channel_id} created", HTTPStatus.CREATED)

@channel_bp.route('/bulk', methods=["POST"])
def create_all_channels() -> Response:
    content = request.get_json()
    channel = [Channel.create_from_dto(data) for data in content]
    channel_controller.create_all(channel)
    return make_response(channel_controller.create_all(channel), HTTPStatus.CREATED)

@channel_bp.route("/all", methods=["DELETE"])
def delete_all_channels() -> Response:
    channel_controller.delete_all()
    return make_response("All channels deleted", HTTPStatus.OK)

