# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_id import UserId


class Operator(object):
    _types = {
        "operator_name": str,
        "operator_id": UserId,
    }

    def __init__(self, d=None):
        self.operator_name: Optional[str] = None
        self.operator_id: Optional[UserId] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OperatorBuilder":
        return OperatorBuilder()


class OperatorBuilder(object):
    def __init__(self) -> None:
        self._operator = Operator()

    def operator_name(self, operator_name: str) -> "OperatorBuilder":
        self._operator.operator_name = operator_name
        return self

    def operator_id(self, operator_id: UserId) -> "OperatorBuilder":
        self._operator.operator_id = operator_id
        return self

    def build(self) -> "Operator":
        return self._operator
