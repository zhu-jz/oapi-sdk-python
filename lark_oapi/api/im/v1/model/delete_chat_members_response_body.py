# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DeleteChatMembersResponseBody(object):
    _types = {
        "invalid_id_list": List[str],
    }

    def __init__(self, d=None):
        self.invalid_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteChatMembersResponseBodyBuilder":
        return DeleteChatMembersResponseBodyBuilder()


class DeleteChatMembersResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_chat_members_response_body = DeleteChatMembersResponseBody()

    def invalid_id_list(self, invalid_id_list: List[str]) -> "DeleteChatMembersResponseBodyBuilder":
        self._delete_chat_members_response_body.invalid_id_list = invalid_id_list
        return self

    def build(self) -> "DeleteChatMembersResponseBody":
        return self._delete_chat_members_response_body
