# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .comment_at_info import CommentAtInfo


class CommentReply(object):
    _types = {
        "id": int,
        "content": str,
        "create_time": int,
        "update_time": int,
        "is_delete": int,
        "at_info_list": List[CommentAtInfo],
        "commentator": str,
        "extra": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.content: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.is_delete: Optional[int] = None
        self.at_info_list: Optional[List[CommentAtInfo]] = None
        self.commentator: Optional[str] = None
        self.extra: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommentReplyBuilder":
        return CommentReplyBuilder()


class CommentReplyBuilder(object):
    def __init__(self) -> None:
        self._comment_reply = CommentReply()

    def id(self, id: int) -> "CommentReplyBuilder":
        self._comment_reply.id = id
        return self

    def content(self, content: str) -> "CommentReplyBuilder":
        self._comment_reply.content = content
        return self

    def create_time(self, create_time: int) -> "CommentReplyBuilder":
        self._comment_reply.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "CommentReplyBuilder":
        self._comment_reply.update_time = update_time
        return self

    def is_delete(self, is_delete: int) -> "CommentReplyBuilder":
        self._comment_reply.is_delete = is_delete
        return self

    def at_info_list(self, at_info_list: List[CommentAtInfo]) -> "CommentReplyBuilder":
        self._comment_reply.at_info_list = at_info_list
        return self

    def commentator(self, commentator: str) -> "CommentReplyBuilder":
        self._comment_reply.commentator = commentator
        return self

    def extra(self, extra: str) -> "CommentReplyBuilder":
        self._comment_reply.extra = extra
        return self

    def build(self) -> "CommentReply":
        return self._comment_reply
