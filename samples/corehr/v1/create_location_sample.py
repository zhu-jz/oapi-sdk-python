# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateLocationRequest = CreateLocationRequest.builder() \
		.client_token("12454646") \
		.request_body(Location.builder()
					  .hiberarchy_common(HiberarchyCommon.builder().build())
					  .location_usage_list([])
					  .address([])
					  .working_hours_type_id("4690238309151997779")
					  .effective_time("2020-05-01 00:00:00")
					  .locale(Enum.builder().build())
					  .time_zone_id("123456789")
					  .display_language_id("123456789")
					  .build()) \
		.build()

	# 发起请求
	response: CreateLocationResponse = client.corehr.v1.location.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.location.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()