from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.channel.channel import Channel


class ChannelDao(GeneralDAO):
    _domain_type = Channel