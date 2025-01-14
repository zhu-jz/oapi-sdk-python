# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .file_subscription import FileSubscription


class CreateFileSubscriptionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_token: Optional[str] = None
        self.request_body: Optional[FileSubscription] = None

    @staticmethod
    def builder() -> "CreateFileSubscriptionRequestBuilder":
        return CreateFileSubscriptionRequestBuilder()


class CreateFileSubscriptionRequestBuilder(object):

    def __init__(self) -> None:
        create_file_subscription_request = CreateFileSubscriptionRequest()
        create_file_subscription_request.http_method = HttpMethod.POST
        create_file_subscription_request.uri = "/open-apis/drive/v1/files/:file_token/subscriptions"
        create_file_subscription_request.token_types = {AccessTokenType.USER}
        self._create_file_subscription_request: CreateFileSubscriptionRequest = create_file_subscription_request

    def file_token(self, file_token: str) -> "CreateFileSubscriptionRequestBuilder":
        self._create_file_subscription_request.file_token = file_token
        self._create_file_subscription_request.paths["file_token"] = str(file_token)
        return self

    def request_body(self, request_body: FileSubscription) -> "CreateFileSubscriptionRequestBuilder":
        self._create_file_subscription_request.request_body = request_body
        self._create_file_subscription_request.body = request_body
        return self

    def build(self) -> CreateFileSubscriptionRequest:
        return self._create_file_subscription_request
