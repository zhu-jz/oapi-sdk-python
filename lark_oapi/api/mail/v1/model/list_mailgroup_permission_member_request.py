# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMailgroupPermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.mailgroup_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMailgroupPermissionMemberRequestBuilder":
        return ListMailgroupPermissionMemberRequestBuilder()


class ListMailgroupPermissionMemberRequestBuilder(object):

    def __init__(self) -> None:
        list_mailgroup_permission_member_request = ListMailgroupPermissionMemberRequest()
        list_mailgroup_permission_member_request.http_method = HttpMethod.GET
        list_mailgroup_permission_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/permission_members"
        list_mailgroup_permission_member_request.token_types = {AccessTokenType.TENANT}
        self._list_mailgroup_permission_member_request: ListMailgroupPermissionMemberRequest = list_mailgroup_permission_member_request

    def user_id_type(self, user_id_type: str) -> "ListMailgroupPermissionMemberRequestBuilder":
        self._list_mailgroup_permission_member_request.user_id_type = user_id_type
        self._list_mailgroup_permission_member_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListMailgroupPermissionMemberRequestBuilder":
        self._list_mailgroup_permission_member_request.department_id_type = department_id_type
        self._list_mailgroup_permission_member_request.add_query("department_id_type", department_id_type)
        return self

    def page_token(self, page_token: str) -> "ListMailgroupPermissionMemberRequestBuilder":
        self._list_mailgroup_permission_member_request.page_token = page_token
        self._list_mailgroup_permission_member_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListMailgroupPermissionMemberRequestBuilder":
        self._list_mailgroup_permission_member_request.page_size = page_size
        self._list_mailgroup_permission_member_request.add_query("page_size", page_size)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "ListMailgroupPermissionMemberRequestBuilder":
        self._list_mailgroup_permission_member_request.mailgroup_id = mailgroup_id
        self._list_mailgroup_permission_member_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def build(self) -> ListMailgroupPermissionMemberRequest:
        return self._list_mailgroup_permission_member_request
