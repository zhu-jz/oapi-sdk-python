# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .job_family import JobFamily


class ListJobFamilyResponseBody(object):
    _types = {
        "items": List[JobFamily],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[JobFamily]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobFamilyResponseBodyBuilder":
        return ListJobFamilyResponseBodyBuilder()


class ListJobFamilyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_job_family_response_body = ListJobFamilyResponseBody()

    def items(self, items: List[JobFamily]) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.has_more = has_more
        return self

    def build(self) -> "ListJobFamilyResponseBody":
        return self._list_job_family_response_body
