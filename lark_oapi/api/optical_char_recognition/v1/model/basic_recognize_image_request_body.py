# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BasicRecognizeImageRequestBody(object):
    _types = {
        "image": str,
    }

    def __init__(self, d=None):
        self.image: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BasicRecognizeImageRequestBodyBuilder":
        return BasicRecognizeImageRequestBodyBuilder()


class BasicRecognizeImageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._basic_recognize_image_request_body = BasicRecognizeImageRequestBody()

    def image(self, image: str) -> "BasicRecognizeImageRequestBodyBuilder":
        self._basic_recognize_image_request_body.image = image
        return self

    def build(self) -> "BasicRecognizeImageRequestBody":
        return self._basic_recognize_image_request_body
