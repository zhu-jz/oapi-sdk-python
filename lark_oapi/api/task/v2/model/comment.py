# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .member import Member


class Comment(object):
    _types = {
        "id": int,
        "content": str,
        "creator": Member,
        "reply_to_comment_id": int,
        "created_at": int,
        "updated_at": int,
        "resource_type": str,
        "resource_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.content: Optional[str] = None
        self.creator: Optional[Member] = None
        self.reply_to_comment_id: Optional[int] = None
        self.created_at: Optional[int] = None
        self.updated_at: Optional[int] = None
        self.resource_type: Optional[str] = None
        self.resource_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommentBuilder":
        return CommentBuilder()


class CommentBuilder(object):
    def __init__(self) -> None:
        self._comment = Comment()

    def id(self, id: int) -> "CommentBuilder":
        self._comment.id = id
        return self

    def content(self, content: str) -> "CommentBuilder":
        self._comment.content = content
        return self

    def creator(self, creator: Member) -> "CommentBuilder":
        self._comment.creator = creator
        return self

    def reply_to_comment_id(self, reply_to_comment_id: int) -> "CommentBuilder":
        self._comment.reply_to_comment_id = reply_to_comment_id
        return self

    def created_at(self, created_at: int) -> "CommentBuilder":
        self._comment.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "CommentBuilder":
        self._comment.updated_at = updated_at
        return self

    def resource_type(self, resource_type: str) -> "CommentBuilder":
        self._comment.resource_type = resource_type
        return self

    def resource_id(self, resource_id: str) -> "CommentBuilder":
        self._comment.resource_id = resource_id
        return self

    def build(self) -> "Comment":
        return self._comment
