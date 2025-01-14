# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer_schema_name import OfferSchemaName


class OfferSchemaDetailOption(object):
    _types = {
        "name": OfferSchemaName,
        "index": int,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.name: Optional[OfferSchemaName] = None
        self.index: Optional[int] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferSchemaDetailOptionBuilder":
        return OfferSchemaDetailOptionBuilder()


class OfferSchemaDetailOptionBuilder(object):
    def __init__(self) -> None:
        self._offer_schema_detail_option = OfferSchemaDetailOption()

    def name(self, name: OfferSchemaName) -> "OfferSchemaDetailOptionBuilder":
        self._offer_schema_detail_option.name = name
        return self

    def index(self, index: int) -> "OfferSchemaDetailOptionBuilder":
        self._offer_schema_detail_option.index = index
        return self

    def active_status(self, active_status: int) -> "OfferSchemaDetailOptionBuilder":
        self._offer_schema_detail_option.active_status = active_status
        return self

    def build(self) -> "OfferSchemaDetailOption":
        return self._offer_schema_detail_option
