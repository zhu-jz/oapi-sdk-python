# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .contract import Contract


class CreateContractResponseBody(object):
    _types = {
        "contract": Contract,
    }

    def __init__(self, d=None):
        self.contract: Optional[Contract] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateContractResponseBodyBuilder":
        return CreateContractResponseBodyBuilder()


class CreateContractResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_contract_response_body = CreateContractResponseBody()

    def contract(self, contract: Contract) -> "CreateContractResponseBodyBuilder":
        self._create_contract_response_body.contract = contract
        return self

    def build(self) -> "CreateContractResponseBody":
        return self._create_contract_response_body
