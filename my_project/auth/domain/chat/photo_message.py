from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PhotoMessage(db.Model, IDto):
    __tablename__ = "photo_message"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_message_path = db.Column(db.String(400))
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text_chat_id = db.Column(db.Integer, db.ForeignKey('text_chat.id'), nullable=False)


    def __repr__(self) -> str:
        return f"PhotoMessage('{self.id}', {self.photo_message_path}, '{self.sender}', '{self.text_chat_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "photo_message_path": self.photo_message_path,
            "sender": self.sender,
            "text_chat_id": self.text_chat_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PhotoMessage:
        return PhotoMessage(
            id=dto_dict.get("id"),
            photo_message_path=dto_dict.get("photo_message_url"),
            sender=dto_dict.get("sender"),
            text_chat_id=dto_dict.get("text_chat_id")
        )
