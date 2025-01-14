# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Bot(object):
    _types = {
        "card_request_url": str,
    }

    def __init__(self, d=None):
        self.card_request_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BotBuilder":
        return BotBuilder()


class BotBuilder(object):
    def __init__(self) -> None:
        self._bot = Bot()

    def card_request_url(self, card_request_url: str) -> "BotBuilder":
        self._bot.card_request_url = card_request_url
        return self

    def build(self) -> "Bot":
        return self._bot
