# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class BankBranch(object):
    _types = {
        "bank_branch_id": str,
        "bank_branch_name": List[I18n],
        "bank_id": str,
        "code": str,
        "swift_code": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.bank_branch_id: Optional[str] = None
        self.bank_branch_name: Optional[List[I18n]] = None
        self.bank_id: Optional[str] = None
        self.code: Optional[str] = None
        self.swift_code: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BankBranchBuilder":
        return BankBranchBuilder()


class BankBranchBuilder(object):
    def __init__(self) -> None:
        self._bank_branch = BankBranch()

    def bank_branch_id(self, bank_branch_id: str) -> "BankBranchBuilder":
        self._bank_branch.bank_branch_id = bank_branch_id
        return self

    def bank_branch_name(self, bank_branch_name: List[I18n]) -> "BankBranchBuilder":
        self._bank_branch.bank_branch_name = bank_branch_name
        return self

    def bank_id(self, bank_id: str) -> "BankBranchBuilder":
        self._bank_branch.bank_id = bank_id
        return self

    def code(self, code: str) -> "BankBranchBuilder":
        self._bank_branch.code = code
        return self

    def swift_code(self, swift_code: str) -> "BankBranchBuilder":
        self._bank_branch.swift_code = swift_code
        return self

    def status(self, status: int) -> "BankBranchBuilder":
        self._bank_branch.status = status
        return self

    def build(self) -> "BankBranch":
        return self._bank_branch
