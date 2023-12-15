from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.chat.audio_message import AudioMessage


class AudioMessageDao(GeneralDAO):
    _domain_type = AudioMessage