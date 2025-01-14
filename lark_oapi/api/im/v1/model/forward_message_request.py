# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .forward_message_request_body import ForwardMessageRequestBody


class ForwardMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.receive_id_type: Optional[str] = None
        self.uuid: Optional[str] = None
        self.message_id: Optional[str] = None
        self.request_body: Optional[ForwardMessageRequestBody] = None

    @staticmethod
    def builder() -> "ForwardMessageRequestBuilder":
        return ForwardMessageRequestBuilder()


class ForwardMessageRequestBuilder(object):

    def __init__(self) -> None:
        forward_message_request = ForwardMessageRequest()
        forward_message_request.http_method = HttpMethod.POST
        forward_message_request.uri = "/open-apis/im/v1/messages/:message_id/forward"
        forward_message_request.token_types = {AccessTokenType.TENANT}
        self._forward_message_request: ForwardMessageRequest = forward_message_request

    def receive_id_type(self, receive_id_type: str) -> "ForwardMessageRequestBuilder":
        self._forward_message_request.receive_id_type = receive_id_type
        self._forward_message_request.add_query("receive_id_type", receive_id_type)
        return self

    def uuid(self, uuid: str) -> "ForwardMessageRequestBuilder":
        self._forward_message_request.uuid = uuid
        self._forward_message_request.add_query("uuid", uuid)
        return self

    def message_id(self, message_id: str) -> "ForwardMessageRequestBuilder":
        self._forward_message_request.message_id = message_id
        self._forward_message_request.paths["message_id"] = str(message_id)
        return self

    def request_body(self, request_body: ForwardMessageRequestBody) -> "ForwardMessageRequestBuilder":
        self._forward_message_request.request_body = request_body
        self._forward_message_request.body = request_body
        return self

    def build(self) -> ForwardMessageRequest:
        return self._forward_message_request
