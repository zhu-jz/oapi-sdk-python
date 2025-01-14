# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Entity(object):
    _types = {
        "block_id": str,
        "title": str,
        "block_type_id": str,
        "source_data": str,
        "source_meta": str,
        "version": int,
        "source_link": str,
        "summary": str,
        "preview": str,
        "i18n_summay": str,
        "i18n_preview": str,
        "owner": str,
        "extra": str,
    }

    def __init__(self, d=None):
        self.block_id: Optional[str] = None
        self.title: Optional[str] = None
        self.block_type_id: Optional[str] = None
        self.source_data: Optional[str] = None
        self.source_meta: Optional[str] = None
        self.version: Optional[int] = None
        self.source_link: Optional[str] = None
        self.summary: Optional[str] = None
        self.preview: Optional[str] = None
        self.i18n_summay: Optional[str] = None
        self.i18n_preview: Optional[str] = None
        self.owner: Optional[str] = None
        self.extra: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EntityBuilder":
        return EntityBuilder()


class EntityBuilder(object):
    def __init__(self) -> None:
        self._entity = Entity()

    def block_id(self, block_id: str) -> "EntityBuilder":
        self._entity.block_id = block_id
        return self

    def title(self, title: str) -> "EntityBuilder":
        self._entity.title = title
        return self

    def block_type_id(self, block_type_id: str) -> "EntityBuilder":
        self._entity.block_type_id = block_type_id
        return self

    def source_data(self, source_data: str) -> "EntityBuilder":
        self._entity.source_data = source_data
        return self

    def source_meta(self, source_meta: str) -> "EntityBuilder":
        self._entity.source_meta = source_meta
        return self

    def version(self, version: int) -> "EntityBuilder":
        self._entity.version = version
        return self

    def source_link(self, source_link: str) -> "EntityBuilder":
        self._entity.source_link = source_link
        return self

    def summary(self, summary: str) -> "EntityBuilder":
        self._entity.summary = summary
        return self

    def preview(self, preview: str) -> "EntityBuilder":
        self._entity.preview = preview
        return self

    def i18n_summay(self, i18n_summay: str) -> "EntityBuilder":
        self._entity.i18n_summay = i18n_summay
        return self

    def i18n_preview(self, i18n_preview: str) -> "EntityBuilder":
        self._entity.i18n_preview = i18n_preview
        return self

    def owner(self, owner: str) -> "EntityBuilder":
        self._entity.owner = owner
        return self

    def extra(self, extra: str) -> "EntityBuilder":
        self._entity.extra = extra
        return self

    def build(self) -> "Entity":
        return self._entity
