# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_space_member_request import CreateSpaceMemberRequest
from ..model.create_space_member_response import CreateSpaceMemberResponse
from ..model.delete_space_member_request import DeleteSpaceMemberRequest
from ..model.delete_space_member_response import DeleteSpaceMemberResponse


class SpaceMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSpaceMemberRequest,
               option: Optional[RequestOption] = None) -> CreateSpaceMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpaceMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpaceMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSpaceMemberRequest,
               option: Optional[RequestOption] = None) -> DeleteSpaceMemberResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteSpaceMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteSpaceMemberResponse)
        response.raw = resp

        return response
