# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.okr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListMetricSourceTableItemRequest = ListMetricSourceTableItemRequest.builder() \
        .metric_source_id("7041857032248410131") \
        .metric_table_id("7041857032248410131") \
        .user_id_type("open_id") \
        .page_token("6969864184272078374") \
        .page_size("10") \
        .build()

    # 发起请求
    response: ListMetricSourceTableItemResponse = client.okr.v1.metric_source_table_item.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.okr.v1.metric_source_table_item.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
