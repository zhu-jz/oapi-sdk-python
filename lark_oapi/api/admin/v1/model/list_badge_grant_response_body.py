# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .grant import Grant


class ListBadgeGrantResponseBody(object):
    _types = {
        "grants": List[Grant],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.grants: Optional[List[Grant]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListBadgeGrantResponseBodyBuilder":
        return ListBadgeGrantResponseBodyBuilder()


class ListBadgeGrantResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_badge_grant_response_body = ListBadgeGrantResponseBody()

    def grants(self, grants: List[Grant]) -> "ListBadgeGrantResponseBodyBuilder":
        self._list_badge_grant_response_body.grants = grants
        return self

    def page_token(self, page_token: str) -> "ListBadgeGrantResponseBodyBuilder":
        self._list_badge_grant_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListBadgeGrantResponseBodyBuilder":
        self._list_badge_grant_response_body.has_more = has_more
        return self

    def build(self) -> "ListBadgeGrantResponseBody":
        return self._list_badge_grant_response_body
