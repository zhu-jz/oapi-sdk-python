# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .node import Node


class MoveResult(object):
    _types = {
        "node": Node,
        "status": int,
        "status_msg": str,
    }

    def __init__(self, d=None):
        self.node: Optional[Node] = None
        self.status: Optional[int] = None
        self.status_msg: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MoveResultBuilder":
        return MoveResultBuilder()


class MoveResultBuilder(object):
    def __init__(self) -> None:
        self._move_result = MoveResult()

    def node(self, node: Node) -> "MoveResultBuilder":
        self._move_result.node = node
        return self

    def status(self, status: int) -> "MoveResultBuilder":
        self._move_result.status = status
        return self

    def status_msg(self, status_msg: str) -> "MoveResultBuilder":
        self._move_result.status_msg = status_msg
        return self

    def build(self) -> "MoveResult":
        return self._move_result
