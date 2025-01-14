# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.search_workplace_access_data_request import SearchWorkplaceAccessDataRequest
from ..model.search_workplace_access_data_response import SearchWorkplaceAccessDataResponse


class WorkplaceAccessData(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def search(self, request: SearchWorkplaceAccessDataRequest,
               option: Optional[RequestOption] = None) -> SearchWorkplaceAccessDataResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchWorkplaceAccessDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     SearchWorkplaceAccessDataResponse)
        response.raw = resp

        return response
