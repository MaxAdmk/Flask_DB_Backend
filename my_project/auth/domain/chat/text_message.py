from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TextMessage(db.Model, IDto):
    __tablename__ = "text_message"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(400))
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text_chat_id = db.Column(db.Integer, db.ForeignKey('text_chat.id'), nullable=False)

    def __repr__(self) -> str:
        return f"TextMessage('{self.id}', {self.text}, '{self.sender}', '{self.text_chat_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "sender": self.sender,
            "text_chat_id": self.text_chat_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TextMessage:
        return TextMessage(
            id=dto_dict.get("id"),
            text=dto_dict.get("text"),
            sender=dto_dict.get("sender"),
            text_chat_id=dto_dict.get("text_chat_id")
        )
