# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_app_request_body import UpdateAppRequestBody


class UpdateAppRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.request_body: Optional[UpdateAppRequestBody] = None

    @staticmethod
    def builder() -> "UpdateAppRequestBuilder":
        return UpdateAppRequestBuilder()


class UpdateAppRequestBuilder(object):

    def __init__(self) -> None:
        update_app_request = UpdateAppRequest()
        update_app_request.http_method = HttpMethod.PUT
        update_app_request.uri = "/open-apis/bitable/v1/apps/:app_token"
        update_app_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._update_app_request: UpdateAppRequest = update_app_request

    def app_token(self, app_token: str) -> "UpdateAppRequestBuilder":
        self._update_app_request.app_token = app_token
        self._update_app_request.paths["app_token"] = str(app_token)
        return self

    def request_body(self, request_body: UpdateAppRequestBody) -> "UpdateAppRequestBuilder":
        self._update_app_request.request_body = request_body
        self._update_app_request.body = request_body
        return self

    def build(self) -> UpdateAppRequest:
        return self._update_app_request
