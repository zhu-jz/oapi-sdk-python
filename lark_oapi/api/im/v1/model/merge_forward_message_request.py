# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .merge_forward_message_request_body import MergeForwardMessageRequestBody


class MergeForwardMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.receive_id_type: Optional[str] = None
        self.uuid: Optional[str] = None
        self.request_body: Optional[MergeForwardMessageRequestBody] = None

    @staticmethod
    def builder() -> "MergeForwardMessageRequestBuilder":
        return MergeForwardMessageRequestBuilder()


class MergeForwardMessageRequestBuilder(object):

    def __init__(self) -> None:
        merge_forward_message_request = MergeForwardMessageRequest()
        merge_forward_message_request.http_method = HttpMethod.POST
        merge_forward_message_request.uri = "/open-apis/im/v1/messages/merge_forward"
        merge_forward_message_request.token_types = {AccessTokenType.TENANT}
        self._merge_forward_message_request: MergeForwardMessageRequest = merge_forward_message_request

    def receive_id_type(self, receive_id_type: str) -> "MergeForwardMessageRequestBuilder":
        self._merge_forward_message_request.receive_id_type = receive_id_type
        self._merge_forward_message_request.add_query("receive_id_type", receive_id_type)
        return self

    def uuid(self, uuid: str) -> "MergeForwardMessageRequestBuilder":
        self._merge_forward_message_request.uuid = uuid
        self._merge_forward_message_request.add_query("uuid", uuid)
        return self

    def request_body(self, request_body: MergeForwardMessageRequestBody) -> "MergeForwardMessageRequestBuilder":
        self._merge_forward_message_request.request_body = request_body
        self._merge_forward_message_request.body = request_body
        return self

    def build(self) -> MergeForwardMessageRequest:
        return self._merge_forward_message_request
