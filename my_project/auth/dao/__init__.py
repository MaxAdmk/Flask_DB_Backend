
from .channel.channel_dao import ChannelDao
from .chat.text_chat_dao import TextChatDao
from .chat.voice_chat_dao import VoiceChatDao
from .chat.audio_message_dao import AudioMessageDao
from .chat.photo_message_dao import PhotoMessageDao
from .chat.text_message_dao import TextMessageDao
from .role.role_dao import RoleDao
from .role.permission_list_dao import PermissionListDao
from .user.user_dao import UserDao
from .user.nitro_boost_dao import NitroBoostDao

channel_dao = ChannelDao()
text_chat_dao = TextChatDao()
voice_chat_dao = VoiceChatDao()
audio_message_dao = AudioMessageDao()
photo_message_dao = PhotoMessageDao()
text_message_dao = TextMessageDao()
role_dao = RoleDao()
permission_list_dao = PermissionListDao()
user_dao = UserDao()
nitro_boost_dao = NitroBoostDao()
