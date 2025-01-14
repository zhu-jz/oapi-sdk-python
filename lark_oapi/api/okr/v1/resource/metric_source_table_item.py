# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_update_metric_source_table_item_request import BatchUpdateMetricSourceTableItemRequest
from ..model.batch_update_metric_source_table_item_response import BatchUpdateMetricSourceTableItemResponse
from ..model.get_metric_source_table_item_request import GetMetricSourceTableItemRequest
from ..model.get_metric_source_table_item_response import GetMetricSourceTableItemResponse
from ..model.list_metric_source_table_item_request import ListMetricSourceTableItemRequest
from ..model.list_metric_source_table_item_response import ListMetricSourceTableItemResponse
from ..model.patch_metric_source_table_item_request import PatchMetricSourceTableItemRequest
from ..model.patch_metric_source_table_item_response import PatchMetricSourceTableItemResponse


class MetricSourceTableItem(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_update(self, request: BatchUpdateMetricSourceTableItemRequest,
                     option: Optional[RequestOption] = None) -> BatchUpdateMetricSourceTableItemResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchUpdateMetricSourceTableItemResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            BatchUpdateMetricSourceTableItemResponse)
        response.raw = resp

        return response

    def get(self, request: GetMetricSourceTableItemRequest,
            option: Optional[RequestOption] = None) -> GetMetricSourceTableItemResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetMetricSourceTableItemResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    GetMetricSourceTableItemResponse)
        response.raw = resp

        return response

    def list(self, request: ListMetricSourceTableItemRequest,
             option: Optional[RequestOption] = None) -> ListMetricSourceTableItemResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMetricSourceTableItemResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     ListMetricSourceTableItemResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchMetricSourceTableItemRequest,
              option: Optional[RequestOption] = None) -> PatchMetricSourceTableItemResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchMetricSourceTableItemResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      PatchMetricSourceTableItemResponse)
        response.raw = resp

        return response
