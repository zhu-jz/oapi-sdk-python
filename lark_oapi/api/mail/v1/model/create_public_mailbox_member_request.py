# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .public_mailbox_member import PublicMailboxMember


class CreatePublicMailboxMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.public_mailbox_id: Optional[str] = None
        self.request_body: Optional[PublicMailboxMember] = None

    @staticmethod
    def builder() -> "CreatePublicMailboxMemberRequestBuilder":
        return CreatePublicMailboxMemberRequestBuilder()


class CreatePublicMailboxMemberRequestBuilder(object):

    def __init__(self) -> None:
        create_public_mailbox_member_request = CreatePublicMailboxMemberRequest()
        create_public_mailbox_member_request.http_method = HttpMethod.POST
        create_public_mailbox_member_request.uri = "/open-apis/mail/v1/public_mailboxes/:public_mailbox_id/members"
        create_public_mailbox_member_request.token_types = {AccessTokenType.TENANT}
        self._create_public_mailbox_member_request: CreatePublicMailboxMemberRequest = create_public_mailbox_member_request

    def user_id_type(self, user_id_type: str) -> "CreatePublicMailboxMemberRequestBuilder":
        self._create_public_mailbox_member_request.user_id_type = user_id_type
        self._create_public_mailbox_member_request.add_query("user_id_type", user_id_type)
        return self

    def public_mailbox_id(self, public_mailbox_id: str) -> "CreatePublicMailboxMemberRequestBuilder":
        self._create_public_mailbox_member_request.public_mailbox_id = public_mailbox_id
        self._create_public_mailbox_member_request.paths["public_mailbox_id"] = str(public_mailbox_id)
        return self

    def request_body(self, request_body: PublicMailboxMember) -> "CreatePublicMailboxMemberRequestBuilder":
        self._create_public_mailbox_member_request.request_body = request_body
        self._create_public_mailbox_member_request.body = request_body
        return self

    def build(self) -> CreatePublicMailboxMemberRequest:
        return self._create_public_mailbox_member_request
