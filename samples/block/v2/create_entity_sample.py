# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.block.v2 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateEntityRequest = CreateEntityRequest.builder() \
		.request_body(CreateEntityRequestBody.builder()
					  .title("已阅block")
					  .block_type_id("blk_614c1c952f800014b27f87d6")
					  .source_data("")
					  .source_meta("")
					  .version("1")
					  .source_link("")
					  .owner("ou_fa7aa170f92d1615de63371ac425a767")
					  .extra("{}")
					  .i18n_summary("")
					  .i18n_preview("")
					  .summary("")
					  .preview("")
					  .build()) \
		.build()

	# 发起请求
	response: CreateEntityResponse = client.block.v2.entity.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.block.v2.entity.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()