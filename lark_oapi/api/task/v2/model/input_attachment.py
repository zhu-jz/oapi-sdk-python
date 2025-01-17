# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InputAttachment(object):
    _types = {
        "file_token": str,
        "resource_type": str,
        "resource_id": str,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.resource_type: Optional[str] = None
        self.resource_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InputAttachmentBuilder":
        return InputAttachmentBuilder()


class InputAttachmentBuilder(object):
    def __init__(self) -> None:
        self._input_attachment = InputAttachment()

    def file_token(self, file_token: str) -> "InputAttachmentBuilder":
        self._input_attachment.file_token = file_token
        return self

    def resource_type(self, resource_type: str) -> "InputAttachmentBuilder":
        self._input_attachment.resource_type = resource_type
        return self

    def resource_id(self, resource_id: str) -> "InputAttachmentBuilder":
        self._input_attachment.resource_id = resource_id
        return self

    def build(self) -> "InputAttachment":
        return self._input_attachment
