# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateMessageReactionRequest = CreateMessageReactionRequest.builder() \
		.message_id("om_a8f2294b************a1a38afaac9d") \
		.request_body(CreateMessageReactionRequestBody.builder()
					  .reaction_type(Emoji.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: CreateMessageReactionResponse = client.im.v1.message_reaction.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.message_reaction.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()