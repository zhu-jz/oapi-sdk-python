# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_reserve_config_admin_request import GetReserveConfigAdminRequest
from ..model.get_reserve_config_admin_response import GetReserveConfigAdminResponse
from ..model.patch_reserve_config_admin_request import PatchReserveConfigAdminRequest
from ..model.patch_reserve_config_admin_response import PatchReserveConfigAdminResponse


class ReserveConfigAdmin(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetReserveConfigAdminRequest,
            option: Optional[RequestOption] = None) -> GetReserveConfigAdminResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetReserveConfigAdminResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 GetReserveConfigAdminResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchReserveConfigAdminRequest,
              option: Optional[RequestOption] = None) -> PatchReserveConfigAdminResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchReserveConfigAdminResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   PatchReserveConfigAdminResponse)
        response.raw = resp

        return response
