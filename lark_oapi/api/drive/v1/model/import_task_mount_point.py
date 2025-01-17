# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ImportTaskMountPoint(object):
    _types = {
        "mount_type": int,
        "mount_key": str,
    }

    def __init__(self, d=None):
        self.mount_type: Optional[int] = None
        self.mount_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ImportTaskMountPointBuilder":
        return ImportTaskMountPointBuilder()


class ImportTaskMountPointBuilder(object):
    def __init__(self) -> None:
        self._import_task_mount_point = ImportTaskMountPoint()

    def mount_type(self, mount_type: int) -> "ImportTaskMountPointBuilder":
        self._import_task_mount_point.mount_type = mount_type
        return self

    def mount_key(self, mount_key: str) -> "ImportTaskMountPointBuilder":
        self._import_task_mount_point.mount_key = mount_key
        return self

    def build(self) -> "ImportTaskMountPoint":
        return self._import_task_mount_point
