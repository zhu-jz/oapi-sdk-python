# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateImageResponseBody(object):
    _types = {
        "image_key": str,
    }

    def __init__(self, d=None):
        self.image_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateImageResponseBodyBuilder":
        return CreateImageResponseBodyBuilder()


class CreateImageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_image_response_body = CreateImageResponseBody()

    def image_key(self, image_key: str) -> "CreateImageResponseBodyBuilder":
        self._create_image_response_body.image_key = image_key
        return self

    def build(self) -> "CreateImageResponseBody":
        return self._create_image_response_body
