

from my_project.auth.service.channel.channel_service import ChannelService
from my_project.auth.service.chat.text_chat_service import TextChatService
from my_project.auth.service.chat.voice_chat_service import VoiceChatService
from my_project.auth.service.chat.text_message_service import TextMessageService
from my_project.auth.service.chat.photo_message_service import PhotoMessageService
from my_project.auth.service.chat.audio_message_service import AudioMessageService
from my_project.auth.service.role.role_service import RoleService
from my_project.auth.service.role.permission_list_service import PermissionListService
from my_project.auth.service.user.user_service import UserService
from my_project.auth.service.user.nitro_boost_service import NitroBoostService

channel_service = ChannelService()
text_chat_service = TextChatService()
voice_chat_service = VoiceChatService()
text_message_service = TextMessageService()
photo_message_service = PhotoMessageService()
audio_message_service = AudioMessageService()
role_service = RoleService()
permission_list_service = PermissionListService()
user_service = UserService()
nitro_boost_service = NitroBoostService()
