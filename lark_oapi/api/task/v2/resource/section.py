# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_section_request import CreateSectionRequest
from ..model.create_section_response import CreateSectionResponse
from ..model.delete_section_request import DeleteSectionRequest
from ..model.delete_section_response import DeleteSectionResponse
from ..model.get_section_request import GetSectionRequest
from ..model.get_section_response import GetSectionResponse
from ..model.list_section_request import ListSectionRequest
from ..model.list_section_response import ListSectionResponse
from ..model.patch_section_request import PatchSectionRequest
from ..model.patch_section_response import PatchSectionResponse
from ..model.tasks_section_request import TasksSectionRequest
from ..model.tasks_section_response import TasksSectionResponse


class Section(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSectionRequest, option: Optional[RequestOption] = None) -> CreateSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSectionResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSectionRequest, option: Optional[RequestOption] = None) -> DeleteSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteSectionResponse)
        response.raw = resp

        return response

    def get(self, request: GetSectionRequest, option: Optional[RequestOption] = None) -> GetSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSectionResponse)
        response.raw = resp

        return response

    def list(self, request: ListSectionRequest, option: Optional[RequestOption] = None) -> ListSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSectionResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchSectionRequest, option: Optional[RequestOption] = None) -> PatchSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchSectionResponse)
        response.raw = resp

        return response

    def tasks(self, request: TasksSectionRequest, option: Optional[RequestOption] = None) -> TasksSectionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: TasksSectionResponse = JSON.unmarshal(str(resp.content, UTF_8), TasksSectionResponse)
        response.raw = resp

        return response
