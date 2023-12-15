from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PermissionList(db.Model, IDto):
    __tablename__ = "permission_list"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    is_administrator = db.Column(db.Boolean, nullable=False)
    creating_roles_permission = db.Column(db.Boolean, nullable=False)
    voice_chat_editing_permission = db.Column(db.Boolean, nullable=False)
    text_chat_editing_permission = db.Column(db.Boolean, nullable=False)

    role = relationship("Role", backref="permission_list", lazy=True)

    def __repr__(self) -> str:
        return f"Role('{self.id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "is_administrator": self.is_administrator,
            "creating_roles_permission": self.creating_roles_permission,
            "voice_chat_editing_permission": self.voice_chat_editing_permission,
            "text_chat_editing_permission": self.text_chat_editing_permission
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PermissionList:
        return PermissionList(
            id=dto_dict.get("id"),
            is_administrator=dto_dict.get("id"),
            creating_roles_permission=dto_dict.get("creating_roles_permission"),
            voice_chat_editing_permission=dto_dict.get("voice_chat_editing_permission"),
            text_chat_editing_permission=dto_dict.get("text_chat_editing_permission")
        )
