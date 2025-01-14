# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .management_scope import ManagementScope


class P2CorehrOrgRoleAuthorizationUpdatedV1Data(object):
    _types = {
        "role_id": str,
        "management_scope_list": List[ManagementScope],
        "employment_id_list": List[str],
    }

    def __init__(self, d=None):
        self.role_id: Optional[str] = None
        self.management_scope_list: Optional[List[ManagementScope]] = None
        self.employment_id_list: Optional[List[str]] = None
        init(self, d, self._types)


class P2CorehrOrgRoleAuthorizationUpdatedV1(EventContext):
    _types = {
        "event": P2CorehrOrgRoleAuthorizationUpdatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrOrgRoleAuthorizationUpdatedV1Data] = None
        init(self, d, self._types)
