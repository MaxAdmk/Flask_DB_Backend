from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.chat.photo_message import PhotoMessage


class PhotoMessageDao(GeneralDAO):
    _domain_type = PhotoMessage