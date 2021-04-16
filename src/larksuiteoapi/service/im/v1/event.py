# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import Callable

from ....config import Config
from ....context import Context
from ....event.event import set_event_callback

from .model import *


class MessageReceiveEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, MessageReceiveEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, MessageReceiveEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, MessageReceiveEvent], Any]) -> None
        handler = MessageReceiveEventHandler(callback)
        set_event_callback(conf, "im.message.receive_v1",
                          handler.handle, clazz=MessageReceiveEvent)


class ChatUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatUpdatedEvent], Any]) -> None
        handler = ChatUpdatedEventHandler(callback)
        set_event_callback(conf, "im.chat.updated_v1",
                          handler.handle, clazz=ChatUpdatedEvent)


class ChatDisbandedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatDisbandedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatDisbandedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatDisbandedEvent], Any]) -> None
        handler = ChatDisbandedEventHandler(callback)
        set_event_callback(conf, "im.chat.disbanded_v1",
                          handler.handle, clazz=ChatDisbandedEvent)


class ChatMemberBotAddedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatMemberBotAddedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatMemberBotAddedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatMemberBotAddedEvent], Any]) -> None
        handler = ChatMemberBotAddedEventHandler(callback)
        set_event_callback(conf, "im.chat.member.bot.added_v1",
                          handler.handle, clazz=ChatMemberBotAddedEvent)


class ChatMemberUserAddedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatMemberUserAddedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatMemberUserAddedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatMemberUserAddedEvent], Any]) -> None
        handler = ChatMemberUserAddedEventHandler(callback)
        set_event_callback(conf, "im.chat.member.user.added_v1",
                          handler.handle, clazz=ChatMemberUserAddedEvent)


class ChatMemberBotDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatMemberBotDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatMemberBotDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatMemberBotDeletedEvent], Any]) -> None
        handler = ChatMemberBotDeletedEventHandler(callback)
        set_event_callback(conf, "im.chat.member.bot.deleted_v1",
                          handler.handle, clazz=ChatMemberBotDeletedEvent)


class ChatMemberUserWithdrawnEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatMemberUserWithdrawnEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatMemberUserWithdrawnEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatMemberUserWithdrawnEvent], Any]) -> None
        handler = ChatMemberUserWithdrawnEventHandler(callback)
        set_event_callback(conf, "im.chat.member.user.withdrawn_v1",
                          handler.handle, clazz=ChatMemberUserWithdrawnEvent)


class ChatMemberUserDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ChatMemberUserDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ChatMemberUserDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ChatMemberUserDeletedEvent], Any]) -> None
        handler = ChatMemberUserDeletedEventHandler(callback)
        set_event_callback(conf, "im.chat.member.user.deleted_v1",
                          handler.handle, clazz=ChatMemberUserDeletedEvent)


class MessageAtMessageReadEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, MessageAtMessageReadEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, MessageAtMessageReadEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, MessageAtMessageReadEvent], Any]) -> None
        handler = MessageAtMessageReadEventHandler(callback)
        set_event_callback(conf, "im.message.at_message_read_v1",
                          handler.handle, clazz=MessageAtMessageReadEvent)


class MessageMessageReadEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, MessageMessageReadEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, MessageMessageReadEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, MessageMessageReadEvent], Any]) -> None
        handler = MessageMessageReadEventHandler(callback)
        set_event_callback(conf, "im.message.message_read_v1",
                          handler.handle, clazz=MessageMessageReadEvent)


class MessageUrgentMessageReadEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, MessageUrgentMessageReadEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, MessageUrgentMessageReadEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, MessageUrgentMessageReadEvent], Any]) -> None
        handler = MessageUrgentMessageReadEventHandler(callback)
        set_event_callback(conf, "im.message.urgent_message_read_v1",
                          handler.handle, clazz=MessageUrgentMessageReadEvent)