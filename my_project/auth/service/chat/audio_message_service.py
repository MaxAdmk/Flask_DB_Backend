from my_project.auth.dao import audio_message_dao
from my_project.auth.service.general_service import GeneralService


class AudioMessageService(GeneralService):
    _dao = audio_message_dao