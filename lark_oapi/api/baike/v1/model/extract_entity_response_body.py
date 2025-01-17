# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .entity_word import EntityWord


class ExtractEntityResponseBody(object):
    _types = {
        "entity_word": List[EntityWord],
    }

    def __init__(self, d=None):
        self.entity_word: Optional[List[EntityWord]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExtractEntityResponseBodyBuilder":
        return ExtractEntityResponseBodyBuilder()


class ExtractEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._extract_entity_response_body = ExtractEntityResponseBody()

    def entity_word(self, entity_word: List[EntityWord]) -> "ExtractEntityResponseBodyBuilder":
        self._extract_entity_response_body.entity_word = entity_word
        return self

    def build(self) -> "ExtractEntityResponseBody":
        return self._extract_entity_response_body
