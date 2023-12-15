from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TextChat(db.Model, IDto):
    __tablename__ = "text_chat"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    photo_message = relationship("PhotoMessage", backref="text_chat", lazy=True)
    text_message = relationship("TextMessage", backref="text_chat", lazy=True)
    audio_message = relationship("AudioMessage", backref="text_chat", lazy=True)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)

    def __repr__(self) -> str:
        return f"TextChat('{self.id}', '{self.name}', '{self.channel_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "channel_id": self.channel_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TextChat:
        return TextChat(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            channel_id=dto_dict.get("channel_id")
        )
