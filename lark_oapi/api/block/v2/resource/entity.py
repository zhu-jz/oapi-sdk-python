# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_entity_request import CreateEntityRequest
from ..model.create_entity_response import CreateEntityResponse
from ..model.update_entity_request import UpdateEntityRequest
from ..model.update_entity_response import UpdateEntityResponse


class Entity(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateEntityRequest, option: Optional[RequestOption] = None) -> CreateEntityResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateEntityResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateEntityResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateEntityRequest, option: Optional[RequestOption] = None) -> UpdateEntityResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateEntityResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateEntityResponse)
        response.raw = resp

        return response
