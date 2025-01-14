# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class SystemStatusUserOpenResultEntity(object):
    _types = {
        "user_id": str,
        "end_time": str,
        "result": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.end_time: Optional[str] = None
        self.result: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemStatusUserOpenResultEntityBuilder":
        return SystemStatusUserOpenResultEntityBuilder()


class SystemStatusUserOpenResultEntityBuilder(object):
    def __init__(self) -> None:
        self._system_status_user_open_result_entity = SystemStatusUserOpenResultEntity()

    def user_id(self, user_id: str) -> "SystemStatusUserOpenResultEntityBuilder":
        self._system_status_user_open_result_entity.user_id = user_id
        return self

    def end_time(self, end_time: str) -> "SystemStatusUserOpenResultEntityBuilder":
        self._system_status_user_open_result_entity.end_time = end_time
        return self

    def result(self, result: str) -> "SystemStatusUserOpenResultEntityBuilder":
        self._system_status_user_open_result_entity.result = result
        return self

    def build(self) -> "SystemStatusUserOpenResultEntity":
        return self._system_status_user_open_result_entity
