# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListResumeSourceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListResumeSourceRequestBuilder":
        return ListResumeSourceRequestBuilder()


class ListResumeSourceRequestBuilder(object):

    def __init__(self) -> None:
        list_resume_source_request = ListResumeSourceRequest()
        list_resume_source_request.http_method = HttpMethod.GET
        list_resume_source_request.uri = "/open-apis/hire/v1/resume_sources"
        list_resume_source_request.token_types = {AccessTokenType.TENANT}
        self._list_resume_source_request: ListResumeSourceRequest = list_resume_source_request

    def page_size(self, page_size: int) -> "ListResumeSourceRequestBuilder":
        self._list_resume_source_request.page_size = page_size
        self._list_resume_source_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListResumeSourceRequestBuilder":
        self._list_resume_source_request.page_token = page_token
        self._list_resume_source_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListResumeSourceRequest:
        return self._list_resume_source_request
