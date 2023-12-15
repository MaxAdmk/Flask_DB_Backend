from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)

    role = relationship("Role", backref="user", lazy=True)
    photo_message = relationship("PhotoMessage", backref="user", lazy=True)
    text_message = relationship("TextMessage", backref="user", lazy=True)
    audio_message = relationship("AudioMessage", backref="user", lazy=True)
    nitro_boost = relationship("NitroBoost", backref="user", lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.id}', '{self.username}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        return User(
            id=dto_dict.get("id"),
            username=dto_dict.get("username"),
            email=dto_dict.get("email"),
        )