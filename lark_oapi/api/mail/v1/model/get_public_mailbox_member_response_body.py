# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class GetPublicMailboxMemberResponseBody(object):
    _types = {
        "member_id": str,
        "user_id": str,
        "type": str,
    }

    def __init__(self, d=None):
        self.member_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetPublicMailboxMemberResponseBodyBuilder":
        return GetPublicMailboxMemberResponseBodyBuilder()


class GetPublicMailboxMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_public_mailbox_member_response_body = GetPublicMailboxMemberResponseBody()

    def member_id(self, member_id: str) -> "GetPublicMailboxMemberResponseBodyBuilder":
        self._get_public_mailbox_member_response_body.member_id = member_id
        return self

    def user_id(self, user_id: str) -> "GetPublicMailboxMemberResponseBodyBuilder":
        self._get_public_mailbox_member_response_body.user_id = user_id
        return self

    def type(self, type: str) -> "GetPublicMailboxMemberResponseBodyBuilder":
        self._get_public_mailbox_member_response_body.type = type
        return self

    def build(self) -> "GetPublicMailboxMemberResponseBody":
        return self._get_public_mailbox_member_response_body
