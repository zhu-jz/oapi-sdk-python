# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .bitable_table_record_action_field_identity_user import BitableTableRecordActionFieldIdentityUser


class BitableTableRecordActionFieldIdentity(object):
    _types = {
        "users": List[BitableTableRecordActionFieldIdentityUser],
    }

    def __init__(self, d=None):
        self.users: Optional[List[BitableTableRecordActionFieldIdentityUser]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableRecordActionFieldIdentityBuilder":
        return BitableTableRecordActionFieldIdentityBuilder()


class BitableTableRecordActionFieldIdentityBuilder(object):
    def __init__(self) -> None:
        self._bitable_table_record_action_field_identity = BitableTableRecordActionFieldIdentity()

    def users(self,
              users: List[BitableTableRecordActionFieldIdentityUser]) -> "BitableTableRecordActionFieldIdentityBuilder":
        self._bitable_table_record_action_field_identity.users = users
        return self

    def build(self) -> "BitableTableRecordActionFieldIdentity":
        return self._bitable_table_record_action_field_identity
