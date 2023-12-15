from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import nitro_boost_controller
from my_project.auth.domain.user.nitro_boost import NitroBoost

nitro_boost_bp = Blueprint("nitro_boost", __name__, url_prefix="/nitroBoost/")

@nitro_boost_bp.route("", methods=["GET"])
def get_all_nitro_boosts() -> Response:
    return make_response(jsonify(nitro_boost_controller.find_all()), HTTPStatus.OK)

@nitro_boost_bp.route('/<int:nitro_boost_id>', methods=["GET"])
def get_nitro_boost(nitro_boost_id: int) -> Response:
    return make_response(jsonify(nitro_boost_controller.find_by_id(nitro_boost_id)), HTTPStatus.OK)

@nitro_boost_bp.route('/<int:nitro_boost_id>', methods=["PUT"])
def update_nitro_boost(nitro_boost_id: int) -> Response:
    content = request.get_json()
    nitro_boost = NitroBoost.create_from_dto(content)
    nitro_boost_controller.update(nitro_boost_id, nitro_boost)
    return make_response("NitroBoost Updated", HTTPStatus.OK)

@nitro_boost_bp.route('/<int:nitro_boost_id>', methods=["PATCH"])
def patch_nitro_boost(nitro_boost_id: int) -> Response:
    content = request.get_json()
    nitro_boost_controller.patch(nitro_boost_id, content)
    return make_response("NitroBoost Updated", HTTPStatus.OK)

@nitro_boost_bp.route('/<int:nitro_boost_id>', methods=["DELETE"])
def delete_nitro_boost(nitro_boost_id: int) -> Response:
    nitro_boost_controller.delete(nitro_boost_id)
    return make_response("NitroBoost deleted", HTTPStatus.OK)

@nitro_boost_bp.route('', methods=["POST"])
def create_nitro_boost() -> Response:
    content = request.get_json()
    nitro_boost = NitroBoost.create_from_dto(content)
    nitro_boost_id = nitro_boost_controller.create(nitro_boost)
    return make_response(f"NitroBoost with id {nitro_boost_id} created", HTTPStatus.CREATED)

@nitro_boost_bp.route('/bulk', methods=["POST"])
def create_all_nitro_boosts() -> Response:
    content = request.get_json()
    nitro_boosts = [NitroBoost.create_from_dto(data) for data in content]
    nitro_boost_controller.create_all(nitro_boosts)
    return make_response(nitro_boost_controller.create_all(nitro_boosts), HTTPStatus.CREATED)

@nitro_boost_bp.route("/all", methods=["DELETE"])
def delete_all_nitro_boosts() -> Response:
    nitro_boost_controller.delete_all()
    return make_response("All nitro boosts deleted", HTTPStatus.OK)

