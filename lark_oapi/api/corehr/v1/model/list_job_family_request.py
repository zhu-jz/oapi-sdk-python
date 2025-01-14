# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobFamilyRequestBuilder":
        return ListJobFamilyRequestBuilder()


class ListJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        list_job_family_request = ListJobFamilyRequest()
        list_job_family_request.http_method = HttpMethod.GET
        list_job_family_request.uri = "/open-apis/corehr/v1/job_families"
        list_job_family_request.token_types = {AccessTokenType.TENANT}
        self._list_job_family_request: ListJobFamilyRequest = list_job_family_request

    def page_token(self, page_token: str) -> "ListJobFamilyRequestBuilder":
        self._list_job_family_request.page_token = page_token
        self._list_job_family_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListJobFamilyRequestBuilder":
        self._list_job_family_request.page_size = page_size
        self._list_job_family_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListJobFamilyRequest:
        return self._list_job_family_request
