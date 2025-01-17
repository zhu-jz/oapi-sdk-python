# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .comment_request import CommentRequest


class CreateInstanceCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.user_id: Optional[int] = None
        self.instance_id: Optional[str] = None
        self.request_body: Optional[CommentRequest] = None

    @staticmethod
    def builder() -> "CreateInstanceCommentRequestBuilder":
        return CreateInstanceCommentRequestBuilder()


class CreateInstanceCommentRequestBuilder(object):

    def __init__(self) -> None:
        create_instance_comment_request = CreateInstanceCommentRequest()
        create_instance_comment_request.http_method = HttpMethod.POST
        create_instance_comment_request.uri = "/open-apis/approval/v4/instances/:instance_id/comments"
        create_instance_comment_request.token_types = {AccessTokenType.TENANT}
        self._create_instance_comment_request: CreateInstanceCommentRequest = create_instance_comment_request

    def user_id_type(self, user_id_type: str) -> "CreateInstanceCommentRequestBuilder":
        self._create_instance_comment_request.user_id_type = user_id_type
        self._create_instance_comment_request.add_query("user_id_type", user_id_type)
        return self

    def user_id(self, user_id: int) -> "CreateInstanceCommentRequestBuilder":
        self._create_instance_comment_request.user_id = user_id
        self._create_instance_comment_request.add_query("user_id", user_id)
        return self

    def instance_id(self, instance_id: str) -> "CreateInstanceCommentRequestBuilder":
        self._create_instance_comment_request.instance_id = instance_id
        self._create_instance_comment_request.paths["instance_id"] = str(instance_id)
        return self

    def request_body(self, request_body: CommentRequest) -> "CreateInstanceCommentRequestBuilder":
        self._create_instance_comment_request.request_body = request_body
        self._create_instance_comment_request.body = request_body
        return self

    def build(self) -> CreateInstanceCommentRequest:
        return self._create_instance_comment_request
