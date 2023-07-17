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
	request: ListNationalIdTypeRequest = ListNationalIdTypeRequest.builder() \
		.page_token("1231231987") \
		.page_size("100") \
		.identification_type("regular_passport") \
		.code("MYS-ID") \
		.country_region_id("6862995749043439111") \
		.build()

	# 发起请求
	response: ListNationalIdTypeResponse = client.corehr.v1.national_id_type.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.national_id_type.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()