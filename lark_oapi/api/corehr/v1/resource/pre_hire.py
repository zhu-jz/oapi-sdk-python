# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.delete_pre_hire_request import DeletePreHireRequest
from ..model.delete_pre_hire_response import DeletePreHireResponse
from ..model.get_pre_hire_request import GetPreHireRequest
from ..model.get_pre_hire_response import GetPreHireResponse
from ..model.list_pre_hire_request import ListPreHireRequest
from ..model.list_pre_hire_response import ListPreHireResponse
from ..model.patch_pre_hire_request import PatchPreHireRequest
from ..model.patch_pre_hire_response import PatchPreHireResponse


class PreHire(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def delete(self, request: DeletePreHireRequest, option: Optional[RequestOption] = None) -> DeletePreHireResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeletePreHireResponse = JSON.unmarshal(str(resp.content, UTF_8), DeletePreHireResponse)
        response.raw = resp

        return response

    def get(self, request: GetPreHireRequest, option: Optional[RequestOption] = None) -> GetPreHireResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetPreHireResponse = JSON.unmarshal(str(resp.content, UTF_8), GetPreHireResponse)
        response.raw = resp

        return response

    def list(self, request: ListPreHireRequest, option: Optional[RequestOption] = None) -> ListPreHireResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListPreHireResponse = JSON.unmarshal(str(resp.content, UTF_8), ListPreHireResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchPreHireRequest, option: Optional[RequestOption] = None) -> PatchPreHireResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchPreHireResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchPreHireResponse)
        response.raw = resp

        return response
