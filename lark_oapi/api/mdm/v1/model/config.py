# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Config(object):
    _types = {
        "field_code": str,
        "field_name": str,
        "module": int,
        "field_describe": str,
        "sys": int,
        "field_type": int,
        "required": int,
        "status": int,
        "field_version": int,
    }

    def __init__(self, d=None):
        self.field_code: Optional[str] = None
        self.field_name: Optional[str] = None
        self.module: Optional[int] = None
        self.field_describe: Optional[str] = None
        self.sys: Optional[int] = None
        self.field_type: Optional[int] = None
        self.required: Optional[int] = None
        self.status: Optional[int] = None
        self.field_version: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConfigBuilder":
        return ConfigBuilder()


class ConfigBuilder(object):
    def __init__(self) -> None:
        self._config = Config()

    def field_code(self, field_code: str) -> "ConfigBuilder":
        self._config.field_code = field_code
        return self

    def field_name(self, field_name: str) -> "ConfigBuilder":
        self._config.field_name = field_name
        return self

    def module(self, module: int) -> "ConfigBuilder":
        self._config.module = module
        return self

    def field_describe(self, field_describe: str) -> "ConfigBuilder":
        self._config.field_describe = field_describe
        return self

    def sys(self, sys: int) -> "ConfigBuilder":
        self._config.sys = sys
        return self

    def field_type(self, field_type: int) -> "ConfigBuilder":
        self._config.field_type = field_type
        return self

    def required(self, required: int) -> "ConfigBuilder":
        self._config.required = required
        return self

    def status(self, status: int) -> "ConfigBuilder":
        self._config.status = status
        return self

    def field_version(self, field_version: int) -> "ConfigBuilder":
        self._config.field_version = field_version
        return self

    def build(self) -> "Config":
        return self._config
