# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .member import Member
from .resource import Resource


class Attachment(object):
    _types = {
        "guid": str,
        "file_token": str,
        "name": str,
        "size": int,
        "resource": Resource,
        "uploader": Member,
        "is_cover": bool,
        "uploaded_at": int,
    }

    def __init__(self, d=None):
        self.guid: Optional[str] = None
        self.file_token: Optional[str] = None
        self.name: Optional[str] = None
        self.size: Optional[int] = None
        self.resource: Optional[Resource] = None
        self.uploader: Optional[Member] = None
        self.is_cover: Optional[bool] = None
        self.uploaded_at: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentBuilder":
        return AttachmentBuilder()


class AttachmentBuilder(object):
    def __init__(self) -> None:
        self._attachment = Attachment()

    def guid(self, guid: str) -> "AttachmentBuilder":
        self._attachment.guid = guid
        return self

    def file_token(self, file_token: str) -> "AttachmentBuilder":
        self._attachment.file_token = file_token
        return self

    def name(self, name: str) -> "AttachmentBuilder":
        self._attachment.name = name
        return self

    def size(self, size: int) -> "AttachmentBuilder":
        self._attachment.size = size
        return self

    def resource(self, resource: Resource) -> "AttachmentBuilder":
        self._attachment.resource = resource
        return self

    def uploader(self, uploader: Member) -> "AttachmentBuilder":
        self._attachment.uploader = uploader
        return self

    def is_cover(self, is_cover: bool) -> "AttachmentBuilder":
        self._attachment.is_cover = is_cover
        return self

    def uploaded_at(self, uploaded_at: int) -> "AttachmentBuilder":
        self._attachment.uploaded_at = uploaded_at
        return self

    def build(self) -> "Attachment":
        return self._attachment
