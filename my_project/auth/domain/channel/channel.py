from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Channel(db.Model, IDto):
    __tablename__ = "channel"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(45), nullable=False)
    members = db.Column(db.Integer, nullable=False)
    voice_chats = relationship("VoiceChat", backref="channel", lazy=True)
    text_chats = relationship("TextChat", backref="channel", lazy=True)
    roles = relationship("Role", backref="channel", lazy=True)

    def __repr__(self) -> str:
        return f"Channel('{self.name}', '{self.id}', '{self.members}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "members": self.members,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Channel:
        return Channel(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            members=dto_dict.get("members"),
        )
