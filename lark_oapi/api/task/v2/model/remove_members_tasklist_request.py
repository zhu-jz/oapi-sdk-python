# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .remove_members_tasklist_request_body import RemoveMembersTasklistRequestBody


class RemoveMembersTasklistRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.tasklist_guid: Optional[str] = None
        self.request_body: Optional[RemoveMembersTasklistRequestBody] = None

    @staticmethod
    def builder() -> "RemoveMembersTasklistRequestBuilder":
        return RemoveMembersTasklistRequestBuilder()


class RemoveMembersTasklistRequestBuilder(object):

    def __init__(self) -> None:
        remove_members_tasklist_request = RemoveMembersTasklistRequest()
        remove_members_tasklist_request.http_method = HttpMethod.POST
        remove_members_tasklist_request.uri = "/open-apis/task/v2/tasklists/:tasklist_guid/remove_members"
        remove_members_tasklist_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._remove_members_tasklist_request: RemoveMembersTasklistRequest = remove_members_tasklist_request

    def user_id_type(self, user_id_type: str) -> "RemoveMembersTasklistRequestBuilder":
        self._remove_members_tasklist_request.user_id_type = user_id_type
        self._remove_members_tasklist_request.add_query("user_id_type", user_id_type)
        return self

    def tasklist_guid(self, tasklist_guid: str) -> "RemoveMembersTasklistRequestBuilder":
        self._remove_members_tasklist_request.tasklist_guid = tasklist_guid
        self._remove_members_tasklist_request.paths["tasklist_guid"] = str(tasklist_guid)
        return self

    def request_body(self, request_body: RemoveMembersTasklistRequestBody) -> "RemoveMembersTasklistRequestBuilder":
        self._remove_members_tasklist_request.request_body = request_body
        self._remove_members_tasklist_request.body = request_body
        return self

    def build(self) -> RemoveMembersTasklistRequest:
        return self._remove_members_tasklist_request
