# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BatchItemResult(object):
    _types = {
        "item_id": str,
        "is_success": bool,
        "err": str,
    }

    def __init__(self, d=None):
        self.item_id: Optional[str] = None
        self.is_success: Optional[bool] = None
        self.err: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchItemResultBuilder":
        return BatchItemResultBuilder()


class BatchItemResultBuilder(object):
    def __init__(self) -> None:
        self._batch_item_result = BatchItemResult()

    def item_id(self, item_id: str) -> "BatchItemResultBuilder":
        self._batch_item_result.item_id = item_id
        return self

    def is_success(self, is_success: bool) -> "BatchItemResultBuilder":
        self._batch_item_result.is_success = is_success
        return self

    def err(self, err: str) -> "BatchItemResultBuilder":
        self._batch_item_result.err = err
        return self

    def build(self) -> "BatchItemResult":
        return self._batch_item_result
