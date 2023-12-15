
from my_project.auth.controller.channel.channel_controller import ChannelController
from my_project.auth.controller.chat.voice_chat_controller import VoiceChatController
from my_project.auth.controller.chat.text_chat_controller import TextChatController
from my_project.auth.controller.chat.audio_message_controller import AudioMessageController
from my_project.auth.controller.chat.text_message_controller import TextMessageController
from my_project.auth.controller.chat.photo_message_controller import PhotoMessageController
from my_project.auth.controller.role.role_controller import RoleController
from my_project.auth.controller.role.permission_list_controller import PermissionListController
from my_project.auth.controller.user.user_controller import UserController
from my_project.auth.controller.user.nitro_boost_controller import NitroBoostController

channel_controller = ChannelController()
voice_chat_controller = VoiceChatController()
text_chat_controller = TextChatController()
audio_message_controller = AudioMessageController()
text_message_controller = TextMessageController()
photo_message_controller = PhotoMessageController()
role_controller = RoleController()
permission_list_controller = PermissionListController()
user_controller = UserController()
nitro_boost_controller = NitroBoostController()
