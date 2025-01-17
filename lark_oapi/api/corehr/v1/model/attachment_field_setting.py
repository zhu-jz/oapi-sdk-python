# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AttachmentFieldSetting(object):
    _types = {
        "is_multiple": bool,
        "file_type": int,
    }

    def __init__(self, d=None):
        self.is_multiple: Optional[bool] = None
        self.file_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentFieldSettingBuilder":
        return AttachmentFieldSettingBuilder()


class AttachmentFieldSettingBuilder(object):
    def __init__(self) -> None:
        self._attachment_field_setting = AttachmentFieldSetting()

    def is_multiple(self, is_multiple: bool) -> "AttachmentFieldSettingBuilder":
        self._attachment_field_setting.is_multiple = is_multiple
        return self

    def file_type(self, file_type: int) -> "AttachmentFieldSettingBuilder":
        self._attachment_field_setting.file_type = file_type
        return self

    def build(self) -> "AttachmentFieldSetting":
        return self._attachment_field_setting
