# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .api_audit_drawer_info import ApiAuditDrawerInfo


class ApiAuditCommonDrawers(object):
    _types = {
        "common_draw_info_list": List[ApiAuditDrawerInfo],
    }

    def __init__(self, d=None):
        self.common_draw_info_list: Optional[List[ApiAuditDrawerInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApiAuditCommonDrawersBuilder":
        return ApiAuditCommonDrawersBuilder()


class ApiAuditCommonDrawersBuilder(object):
    def __init__(self) -> None:
        self._api_audit_common_drawers = ApiAuditCommonDrawers()

    def common_draw_info_list(self, common_draw_info_list: List[ApiAuditDrawerInfo]) -> "ApiAuditCommonDrawersBuilder":
        self._api_audit_common_drawers.common_draw_info_list = common_draw_info_list
        return self

    def build(self) -> "ApiAuditCommonDrawers":
        return self._api_audit_common_drawers
