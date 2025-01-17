# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .bitable_table_record_action_field import BitableTableRecordActionField


class BitableTableRecordAction(object):
    _types = {
        "record_id": str,
        "action": str,
        "before_value": List[BitableTableRecordActionField],
        "after_value": List[BitableTableRecordActionField],
    }

    def __init__(self, d=None):
        self.record_id: Optional[str] = None
        self.action: Optional[str] = None
        self.before_value: Optional[List[BitableTableRecordActionField]] = None
        self.after_value: Optional[List[BitableTableRecordActionField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableRecordActionBuilder":
        return BitableTableRecordActionBuilder()


class BitableTableRecordActionBuilder(object):
    def __init__(self) -> None:
        self._bitable_table_record_action = BitableTableRecordAction()

    def record_id(self, record_id: str) -> "BitableTableRecordActionBuilder":
        self._bitable_table_record_action.record_id = record_id
        return self

    def action(self, action: str) -> "BitableTableRecordActionBuilder":
        self._bitable_table_record_action.action = action
        return self

    def before_value(self, before_value: List[BitableTableRecordActionField]) -> "BitableTableRecordActionBuilder":
        self._bitable_table_record_action.before_value = before_value
        return self

    def after_value(self, after_value: List[BitableTableRecordActionField]) -> "BitableTableRecordActionBuilder":
        self._bitable_table_record_action.after_value = after_value
        return self

    def build(self) -> "BitableTableRecordAction":
        return self._bitable_table_record_action
