# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .group_meta import GroupMeta


class SearchGroupResponseBody(object):
    _types = {
        "group_list": List[GroupMeta],
    }

    def __init__(self, d):
        self.group_list: Optional[List[GroupMeta]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchGroupResponseBodyBuilder":
        return SearchGroupResponseBodyBuilder()


class SearchGroupResponseBodyBuilder(object):
    def __init__(self, search_group_response_body: SearchGroupResponseBody = SearchGroupResponseBody({})) -> None:
        self._search_group_response_body: SearchGroupResponseBody = search_group_response_body
    
    def group_list(self, group_list: List[GroupMeta]) -> "SearchGroupResponseBodyBuilder":
        self._search_group_response_body.group_list = group_list
        return self
    
    def build(self) -> "SearchGroupResponseBody":
        return self._search_group_response_body