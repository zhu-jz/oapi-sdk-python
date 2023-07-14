# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ImageInfo(object):
    _types = {
        "file_token": str,
        "url": str,
    }

    def __init__(self, d):
        self.file_token: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImageInfoBuilder":
        return ImageInfoBuilder()


class ImageInfoBuilder(object):
    def __init__(self, image_info: ImageInfo = ImageInfo({})) -> None:
        self._image_info: ImageInfo = image_info
    
    def file_token(self, file_token: str) -> "ImageInfoBuilder":
        self._image_info.file_token = file_token
        return self
    
    def url(self, url: str) -> "ImageInfoBuilder":
        self._image_info.url = url
        return self
    
    def build(self) -> "ImageInfo":
        return self._image_info