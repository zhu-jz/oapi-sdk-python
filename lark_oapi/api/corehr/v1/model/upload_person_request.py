# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .upload_person_request_body import UploadPersonRequestBody


class UploadPersonRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[UploadPersonRequestBody] = None

    @staticmethod
    def builder() -> "UploadPersonRequestBuilder":
        return UploadPersonRequestBuilder()


class UploadPersonRequestBuilder(object):

    def __init__(self) -> None:
        upload_person_request = UploadPersonRequest()
        upload_person_request.http_method = HttpMethod.POST
        upload_person_request.uri = "/open-apis/corehr/v1/persons/upload"
        upload_person_request.token_types = {AccessTokenType.TENANT}
        self._upload_person_request: UploadPersonRequest = upload_person_request

    def request_body(self, request_body: UploadPersonRequestBody) -> "UploadPersonRequestBuilder":
        self._upload_person_request.request_body = request_body
        self._upload_person_request.body = request_body
        return self

    def build(self) -> UploadPersonRequest:
        return self._upload_person_request
