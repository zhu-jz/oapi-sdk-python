# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class InternalOrder(object):
    _types = {
        "internal_order_uid": str,
        "internal_order_code": str,
        "internal_order_name": str,
        "type": str,
        "responsible_user_union_id": str,
        "company_code": str,
        "co_area_code": str,
    }

    def __init__(self, d=None):
        self.internal_order_uid: Optional[str] = None
        self.internal_order_code: Optional[str] = None
        self.internal_order_name: Optional[str] = None
        self.type: Optional[str] = None
        self.responsible_user_union_id: Optional[str] = None
        self.company_code: Optional[str] = None
        self.co_area_code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InternalOrderBuilder":
        return InternalOrderBuilder()


class InternalOrderBuilder(object):
    def __init__(self) -> None:
        self._internal_order = InternalOrder()

    def internal_order_uid(self, internal_order_uid: str) -> "InternalOrderBuilder":
        self._internal_order.internal_order_uid = internal_order_uid
        return self

    def internal_order_code(self, internal_order_code: str) -> "InternalOrderBuilder":
        self._internal_order.internal_order_code = internal_order_code
        return self

    def internal_order_name(self, internal_order_name: str) -> "InternalOrderBuilder":
        self._internal_order.internal_order_name = internal_order_name
        return self

    def type(self, type: str) -> "InternalOrderBuilder":
        self._internal_order.type = type
        return self

    def responsible_user_union_id(self, responsible_user_union_id: str) -> "InternalOrderBuilder":
        self._internal_order.responsible_user_union_id = responsible_user_union_id
        return self

    def company_code(self, company_code: str) -> "InternalOrderBuilder":
        self._internal_order.company_code = company_code
        return self

    def co_area_code(self, co_area_code: str) -> "InternalOrderBuilder":
        self._internal_order.co_area_code = co_area_code
        return self

    def build(self) -> "InternalOrder":
        return self._internal_order
