# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_file_comment_reply_request_body import UpdateFileCommentReplyRequestBody


class UpdateFileCommentReplyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.file_token: Optional[str] = None
        self.comment_id: Optional[int] = None
        self.reply_id: Optional[int] = None
        self.request_body: Optional[UpdateFileCommentReplyRequestBody] = None

    @staticmethod
    def builder() -> "UpdateFileCommentReplyRequestBuilder":
        return UpdateFileCommentReplyRequestBuilder()


class UpdateFileCommentReplyRequestBuilder(object):

    def __init__(self) -> None:
        update_file_comment_reply_request = UpdateFileCommentReplyRequest()
        update_file_comment_reply_request.http_method = HttpMethod.PUT
        update_file_comment_reply_request.uri = "/open-apis/drive/v1/files/:file_token/comments/:comment_id/replies/:reply_id"
        update_file_comment_reply_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._update_file_comment_reply_request: UpdateFileCommentReplyRequest = update_file_comment_reply_request

    def file_type(self, file_type: str) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.file_type = file_type
        self._update_file_comment_reply_request.add_query("file_type", file_type)
        return self

    def user_id_type(self, user_id_type: str) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.user_id_type = user_id_type
        self._update_file_comment_reply_request.add_query("user_id_type", user_id_type)
        return self

    def file_token(self, file_token: str) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.file_token = file_token
        self._update_file_comment_reply_request.paths["file_token"] = str(file_token)
        return self

    def comment_id(self, comment_id: int) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.comment_id = comment_id
        self._update_file_comment_reply_request.paths["comment_id"] = str(comment_id)
        return self

    def reply_id(self, reply_id: int) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.reply_id = reply_id
        self._update_file_comment_reply_request.paths["reply_id"] = str(reply_id)
        return self

    def request_body(self, request_body: UpdateFileCommentReplyRequestBody) -> "UpdateFileCommentReplyRequestBuilder":
        self._update_file_comment_reply_request.request_body = request_body
        self._update_file_comment_reply_request.body = request_body
        return self

    def build(self) -> UpdateFileCommentReplyRequest:
        return self._update_file_comment_reply_request
