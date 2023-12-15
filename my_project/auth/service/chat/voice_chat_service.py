from my_project.auth.dao import voice_chat_dao
from my_project.auth.service.general_service import GeneralService


class VoiceChatService(GeneralService):
    _dao = voice_chat_dao