# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .file_comment import FileComment


class CreateFileCommentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.file_token: Optional[str] = None
        self.request_body: Optional[FileComment] = None

    @staticmethod
    def builder() -> "CreateFileCommentRequestBuilder":
        return CreateFileCommentRequestBuilder()


class CreateFileCommentRequestBuilder(object):

    def __init__(self) -> None:
        create_file_comment_request = CreateFileCommentRequest()
        create_file_comment_request.http_method = HttpMethod.POST
        create_file_comment_request.uri = "/open-apis/drive/v1/files/:file_token/comments"
        create_file_comment_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_file_comment_request: CreateFileCommentRequest = create_file_comment_request

    def file_type(self, file_type: str) -> "CreateFileCommentRequestBuilder":
        self._create_file_comment_request.file_type = file_type
        self._create_file_comment_request.add_query("file_type", file_type)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateFileCommentRequestBuilder":
        self._create_file_comment_request.user_id_type = user_id_type
        self._create_file_comment_request.add_query("user_id_type", user_id_type)
        return self

    def file_token(self, file_token: str) -> "CreateFileCommentRequestBuilder":
        self._create_file_comment_request.file_token = file_token
        self._create_file_comment_request.paths["file_token"] = str(file_token)
        return self

    def request_body(self, request_body: FileComment) -> "CreateFileCommentRequestBuilder":
        self._create_file_comment_request.request_body = request_body
        self._create_file_comment_request.body = request_body
        return self

    def build(self) -> CreateFileCommentRequest:
        return self._create_file_comment_request
