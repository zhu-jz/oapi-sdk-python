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
	request: GetMessageResourceRequest = GetMessageResourceRequest.builder() \
		.message_id("om_dc13264520392913993dd051dba21dcf") \
		.file_key("file_456a92d6-c6ea-4de4-ac3f-7afcf44ac78g") \
		.type("image") \
		.build()

	# 发起请求
	response: GetMessageResourceResponse = client.im.v1.message_resource.get(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.message_resource.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	f = open(f"file_path/{response.file_name}", "wb")
	f.write(response.file.read())
	f.close()


if __name__ == "__main__":
	main()