# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EmployeeConversionInfo(object):
    _types = {
        "actual_conversion_time": int,
    }

    def __init__(self, d=None):
        self.actual_conversion_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeConversionInfoBuilder":
        return EmployeeConversionInfoBuilder()


class EmployeeConversionInfoBuilder(object):
    def __init__(self) -> None:
        self._employee_conversion_info = EmployeeConversionInfo()

    def actual_conversion_time(self, actual_conversion_time: int) -> "EmployeeConversionInfoBuilder":
        self._employee_conversion_info.actual_conversion_time = actual_conversion_time
        return self

    def build(self) -> "EmployeeConversionInfo":
        return self._employee_conversion_info
