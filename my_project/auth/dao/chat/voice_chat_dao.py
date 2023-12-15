from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.chat.voice_chat import VoiceChat


class VoiceChatDao(GeneralDAO):
    _domain_type = VoiceChat