from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Role(db.Model, IDto):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    permission_list_id = db.Column(db.Integer, db.ForeignKey('permission_list.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Role('{self.id}', '{self.name}', {self.permission_list_id}, '{self.channel_id}', '{self.user_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "permission_list_id": self.permission_list_id,
            "channel_id": self.channel_id,
            "user_id": self.user_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Role:
        return Role(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            permission_list_id=dto_dict.get("permission_list_id"),
            channel_id=dto_dict.get("channel_id"),
            user_id=dto_dict.get("user_id")
        )
