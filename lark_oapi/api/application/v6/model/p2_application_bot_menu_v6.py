# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .operator import Operator


class P2ApplicationBotMenuV6Data(object):
    _types = {
        "operator": Operator,
        "event_key": str,
        "timestamp": int,
    }

    def __init__(self, d=None):
        self.operator: Optional[Operator] = None
        self.event_key: Optional[str] = None
        self.timestamp: Optional[int] = None
        init(self, d, self._types)


class P2ApplicationBotMenuV6(EventContext):
    _types = {
        "event": P2ApplicationBotMenuV6Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ApplicationBotMenuV6Data] = None
        init(self, d, self._types)
