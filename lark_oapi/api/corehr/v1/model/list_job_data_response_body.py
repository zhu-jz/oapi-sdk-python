# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_data import JobData


class ListJobDataResponseBody(object):
    _types = {
        "items": List[JobData],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobData]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobDataResponseBodyBuilder":
        return ListJobDataResponseBodyBuilder()


class ListJobDataResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_job_data_response_body = ListJobDataResponseBody()

    def items(self, items: List[JobData]) -> "ListJobDataResponseBodyBuilder":
        self._list_job_data_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListJobDataResponseBodyBuilder":
        self._list_job_data_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListJobDataResponseBodyBuilder":
        self._list_job_data_response_body.page_token = page_token
        return self

    def build(self) -> "ListJobDataResponseBody":
        return self._list_job_data_response_body
