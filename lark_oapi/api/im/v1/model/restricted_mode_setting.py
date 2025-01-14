# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RestrictedModeSetting(object):
    _types = {
        "status": bool,
        "screenshot_has_permission_setting": str,
        "download_has_permission_setting": str,
        "message_has_permission_setting": str,
    }

    def __init__(self, d=None):
        self.status: Optional[bool] = None
        self.screenshot_has_permission_setting: Optional[str] = None
        self.download_has_permission_setting: Optional[str] = None
        self.message_has_permission_setting: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RestrictedModeSettingBuilder":
        return RestrictedModeSettingBuilder()


class RestrictedModeSettingBuilder(object):
    def __init__(self) -> None:
        self._restricted_mode_setting = RestrictedModeSetting()

    def status(self, status: bool) -> "RestrictedModeSettingBuilder":
        self._restricted_mode_setting.status = status
        return self

    def screenshot_has_permission_setting(self,
                                          screenshot_has_permission_setting: str) -> "RestrictedModeSettingBuilder":
        self._restricted_mode_setting.screenshot_has_permission_setting = screenshot_has_permission_setting
        return self

    def download_has_permission_setting(self, download_has_permission_setting: str) -> "RestrictedModeSettingBuilder":
        self._restricted_mode_setting.download_has_permission_setting = download_has_permission_setting
        return self

    def message_has_permission_setting(self, message_has_permission_setting: str) -> "RestrictedModeSettingBuilder":
        self._restricted_mode_setting.message_has_permission_setting = message_has_permission_setting
        return self

    def build(self) -> "RestrictedModeSetting":
        return self._restricted_mode_setting
