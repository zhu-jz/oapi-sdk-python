# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetFaqRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.id: Optional[str] = None

    @staticmethod
    def builder() -> "GetFaqRequestBuilder":
        return GetFaqRequestBuilder()


class GetFaqRequestBuilder(object):

    def __init__(self) -> None:
        get_faq_request = GetFaqRequest()
        get_faq_request.http_method = HttpMethod.GET
        get_faq_request.uri = "/open-apis/helpdesk/v1/faqs/:id"
        get_faq_request.token_types = {AccessTokenType.TENANT}
        self._get_faq_request: GetFaqRequest = get_faq_request

    def id(self, id: str) -> "GetFaqRequestBuilder":
        self._get_faq_request.id = id
        self._get_faq_request.paths["id"] = str(id)
        return self

    def build(self) -> GetFaqRequest:
        return self._get_faq_request
