# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mail.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: DeletePublicMailboxAliasRequest = DeletePublicMailboxAliasRequest.builder() \
		.public_mailbox_id("xxxxxx 或 xxx@xx.xxx") \
		.alias_id("xxx@xx.xxx") \
		.build()

	# 发起请求
	response: DeletePublicMailboxAliasResponse = client.mail.v1.public_mailbox_alias.delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.mail.v1.public_mailbox_alias.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()