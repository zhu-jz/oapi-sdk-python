# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskTransfer(object):
    _types = {
        "approval_code": str,
        "instance_code": str,
        "user_id": str,
        "comment": str,
        "transfer_user_id": str,
        "task_id": str,
    }

    def __init__(self, d=None):
        self.approval_code: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.user_id: Optional[str] = None
        self.comment: Optional[str] = None
        self.transfer_user_id: Optional[str] = None
        self.task_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskTransferBuilder":
        return TaskTransferBuilder()


class TaskTransferBuilder(object):
    def __init__(self) -> None:
        self._task_transfer = TaskTransfer()

    def approval_code(self, approval_code: str) -> "TaskTransferBuilder":
        self._task_transfer.approval_code = approval_code
        return self

    def instance_code(self, instance_code: str) -> "TaskTransferBuilder":
        self._task_transfer.instance_code = instance_code
        return self

    def user_id(self, user_id: str) -> "TaskTransferBuilder":
        self._task_transfer.user_id = user_id
        return self

    def comment(self, comment: str) -> "TaskTransferBuilder":
        self._task_transfer.comment = comment
        return self

    def transfer_user_id(self, transfer_user_id: str) -> "TaskTransferBuilder":
        self._task_transfer.transfer_user_id = transfer_user_id
        return self

    def task_id(self, task_id: str) -> "TaskTransferBuilder":
        self._task_transfer.task_id = task_id
        return self

    def build(self) -> "TaskTransfer":
        return self._task_transfer
