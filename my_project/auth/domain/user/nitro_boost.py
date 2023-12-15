from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class NitroBoost(db.Model, IDto):
    __tablename__ = "nitro_boost"

    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"NitroBoost('{self.id}', '{self.duration}', '{self.user_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "duration": self.duration,
            "user_id": self.user_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> NitroBoost:
        return NitroBoost(
            id=dto_dict.get("id"),
            duration=dto_dict.get("duration"),
            user_id=dto_dict.get("user_id")
        )
