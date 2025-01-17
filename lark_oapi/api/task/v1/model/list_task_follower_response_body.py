# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .follower import Follower


class ListTaskFollowerResponseBody(object):
    _types = {
        "items": List[Follower],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Follower]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTaskFollowerResponseBodyBuilder":
        return ListTaskFollowerResponseBodyBuilder()


class ListTaskFollowerResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_task_follower_response_body = ListTaskFollowerResponseBody()

    def items(self, items: List[Follower]) -> "ListTaskFollowerResponseBodyBuilder":
        self._list_task_follower_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListTaskFollowerResponseBodyBuilder":
        self._list_task_follower_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListTaskFollowerResponseBodyBuilder":
        self._list_task_follower_response_body.has_more = has_more
        return self

    def build(self) -> "ListTaskFollowerResponseBody":
        return self._list_task_follower_response_body
