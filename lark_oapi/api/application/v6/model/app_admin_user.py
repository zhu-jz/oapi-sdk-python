# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppAdminUser(object):
    _types = {
        "admin_type": List[str],
        "user_id": str,
    }

    def __init__(self, d=None):
        self.admin_type: Optional[List[str]] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppAdminUserBuilder":
        return AppAdminUserBuilder()


class AppAdminUserBuilder(object):
    def __init__(self) -> None:
        self._app_admin_user = AppAdminUser()

    def admin_type(self, admin_type: List[str]) -> "AppAdminUserBuilder":
        self._app_admin_user.admin_type = admin_type
        return self

    def user_id(self, user_id: str) -> "AppAdminUserBuilder":
        self._app_admin_user.user_id = user_id
        return self

    def build(self) -> "AppAdminUser":
        return self._app_admin_user
