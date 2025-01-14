# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .avatar import Avatar


class Tenant(object):
    _types = {
        "name": str,
        "display_id": str,
        "tenant_tag": int,
        "tenant_key": str,
        "avatar": Avatar,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.display_id: Optional[str] = None
        self.tenant_tag: Optional[int] = None
        self.tenant_key: Optional[str] = None
        self.avatar: Optional[Avatar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TenantBuilder":
        return TenantBuilder()


class TenantBuilder(object):
    def __init__(self) -> None:
        self._tenant = Tenant()

    def name(self, name: str) -> "TenantBuilder":
        self._tenant.name = name
        return self

    def display_id(self, display_id: str) -> "TenantBuilder":
        self._tenant.display_id = display_id
        return self

    def tenant_tag(self, tenant_tag: int) -> "TenantBuilder":
        self._tenant.tenant_tag = tenant_tag
        return self

    def tenant_key(self, tenant_key: str) -> "TenantBuilder":
        self._tenant.tenant_key = tenant_key
        return self

    def avatar(self, avatar: Avatar) -> "TenantBuilder":
        self._tenant.avatar = avatar
        return self

    def build(self) -> "Tenant":
        return self._tenant
