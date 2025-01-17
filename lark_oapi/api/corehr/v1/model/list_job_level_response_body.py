# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_level import JobLevel


class ListJobLevelResponseBody(object):
    _types = {
        "items": List[JobLevel],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobLevel]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobLevelResponseBodyBuilder":
        return ListJobLevelResponseBodyBuilder()


class ListJobLevelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_job_level_response_body = ListJobLevelResponseBody()

    def items(self, items: List[JobLevel]) -> "ListJobLevelResponseBodyBuilder":
        self._list_job_level_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListJobLevelResponseBodyBuilder":
        self._list_job_level_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListJobLevelResponseBodyBuilder":
        self._list_job_level_response_body.page_token = page_token
        return self

    def build(self) -> "ListJobLevelResponseBody":
        return self._list_job_level_response_body
