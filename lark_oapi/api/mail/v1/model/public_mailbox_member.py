# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class PublicMailboxMember(object):
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
    def builder() -> "PublicMailboxMemberBuilder":
        return PublicMailboxMemberBuilder()


class PublicMailboxMemberBuilder(object):
    def __init__(self) -> None:
        self._public_mailbox_member = PublicMailboxMember()

    def member_id(self, member_id: str) -> "PublicMailboxMemberBuilder":
        self._public_mailbox_member.member_id = member_id
        return self

    def user_id(self, user_id: str) -> "PublicMailboxMemberBuilder":
        self._public_mailbox_member.user_id = user_id
        return self

    def type(self, type: str) -> "PublicMailboxMemberBuilder":
        self._public_mailbox_member.type = type
        return self

    def build(self) -> "PublicMailboxMember":
        return self._public_mailbox_member
