# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_mailgroup_alias_request import CreateMailgroupAliasRequest
from ..model.create_mailgroup_alias_response import CreateMailgroupAliasResponse
from ..model.delete_mailgroup_alias_request import DeleteMailgroupAliasRequest
from ..model.delete_mailgroup_alias_response import DeleteMailgroupAliasResponse
from ..model.list_mailgroup_alias_request import ListMailgroupAliasRequest
from ..model.list_mailgroup_alias_response import ListMailgroupAliasResponse


class MailgroupAlias(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateMailgroupAliasRequest,
               option: Optional[RequestOption] = None) -> CreateMailgroupAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateMailgroupAliasResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMailgroupAliasRequest,
               option: Optional[RequestOption] = None) -> DeleteMailgroupAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteMailgroupAliasResponse)
        response.raw = resp

        return response

    def list(self, request: ListMailgroupAliasRequest,
             option: Optional[RequestOption] = None) -> ListMailgroupAliasResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), ListMailgroupAliasResponse)
        response.raw = resp

        return response
