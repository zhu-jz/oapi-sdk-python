# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BackgroundCheckOrderCreator(object):
    _types = {
        "user_id": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckOrderCreatorBuilder":
        return BackgroundCheckOrderCreatorBuilder()


class BackgroundCheckOrderCreatorBuilder(object):
    def __init__(self) -> None:
        self._background_check_order_creator = BackgroundCheckOrderCreator()

    def user_id(self, user_id: str) -> "BackgroundCheckOrderCreatorBuilder":
        self._background_check_order_creator.user_id = user_id
        return self

    def build(self) -> "BackgroundCheckOrderCreator":
        return self._background_check_order_creator
