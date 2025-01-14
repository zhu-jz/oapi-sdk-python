# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ClearPublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.public_mailbox_id: Optional[str] = None

    @staticmethod
    def builder() -> "ClearPublicMailboxMemberRequestBuilder":
        return ClearPublicMailboxMemberRequestBuilder()


class ClearPublicMailboxMemberRequestBuilder(object):

    def __init__(self) -> None:
        clear_public_mailbox_member_request = ClearPublicMailboxMemberRequest()
        clear_public_mailbox_member_request.http_method = HttpMethod.POST
        clear_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members/clear"
        clear_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._clear_public_mailbox_member_request: ClearPublicMailboxMemberRequest = clear_public_mailbox_member_request

    def public_mailbox_id(self, public_mailbox_id: str) -> "ClearPublicMailboxMemberRequestBuilder":
        self._clear_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._clear_public_mailbox_member_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def build(self) -> ClearPublicMailboxMemberRequest:
        return self._clear_public_mailbox_member_request
