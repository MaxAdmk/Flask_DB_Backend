from flask import Flask

def register_routes(app: Flask) -> None:

    from .user.user_route import user_bp
    from .channel.channel_route import channel_bp
    from .chat.text_chat_route import text_chat_bp
    from .chat.voice_chat_route import voice_chat_bp
    from .chat.photo_message_route import photo_message_bp
    from .chat.text_message_route import text_message_bp
    from .chat.audio_message_route import audio_message_bp
    from .user.nitro_boost_route import nitro_boost_bp
    from .role.role_route import role_bp
    from .role.permission_list_route import permission_list_bp

    app.register_blueprint(text_chat_bp)
    app.register_blueprint(voice_chat_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(channel_bp)
    app.register_blueprint(photo_message_bp)
    app.register_blueprint(text_message_bp)
    app.register_blueprint(audio_message_bp)
    app.register_blueprint(nitro_boost_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(permission_list_bp)
