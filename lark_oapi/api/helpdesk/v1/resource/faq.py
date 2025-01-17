# Code generated by Lark OpenAPI.

import io
from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.create_faq_request import CreateFaqRequest
from ..model.create_faq_response import CreateFaqResponse
from ..model.delete_faq_request import DeleteFaqRequest
from ..model.delete_faq_response import DeleteFaqResponse
from ..model.faq_image_faq_request import FaqImageFaqRequest
from ..model.faq_image_faq_response import FaqImageFaqResponse
from ..model.get_faq_request import GetFaqRequest
from ..model.get_faq_response import GetFaqResponse
from ..model.list_faq_request import ListFaqRequest
from ..model.list_faq_response import ListFaqResponse
from ..model.patch_faq_request import PatchFaqRequest
from ..model.patch_faq_response import PatchFaqResponse
from ..model.search_faq_request import SearchFaqRequest
from ..model.search_faq_response import SearchFaqResponse


class Faq(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateFaqRequest, option: Optional[RequestOption] = None) -> CreateFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateFaqResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteFaqRequest, option: Optional[RequestOption] = None) -> DeleteFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteFaqResponse)
        response.raw = resp

        return response

    def faq_image(self, request: FaqImageFaqRequest, option: Optional[RequestOption] = None) -> FaqImageFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        content_type = resp.headers.get(CONTENT_TYPE)
        response: FaqImageFaqResponse = FaqImageFaqResponse()
        if 200 <= resp.status_code < 300:
            response.code = 0
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(resp.headers)
        elif content_type is not None and content_type.startswith(APPLICATION_JSON):
            response = JSON.unmarshal(str(resp.content, UTF_8), FaqImageFaqResponse)

        response.raw = resp
        return response

    def get(self, request: GetFaqRequest, option: Optional[RequestOption] = None) -> GetFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFaqResponse)
        response.raw = resp

        return response

    def list(self, request: ListFaqRequest, option: Optional[RequestOption] = None) -> ListFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), ListFaqResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchFaqRequest, option: Optional[RequestOption] = None) -> PatchFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchFaqResponse)
        response.raw = resp

        return response

    def search(self, request: SearchFaqRequest, option: Optional[RequestOption] = None) -> SearchFaqResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchFaqResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchFaqResponse)
        response.raw = resp

        return response
