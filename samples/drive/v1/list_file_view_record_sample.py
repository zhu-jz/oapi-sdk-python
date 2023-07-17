# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListFileViewRecordRequest = ListFileViewRecordRequest.builder() \
		.file_token("XIHSdYSI7oMEU1xrsnxc8fabcef") \
		.page_size(10) \
		.page_token("1674037112--7189934631754563585") \
		.file_type("docx") \
		.viewer_id_type("open_id") \
		.build()

	# 发起请求
	response: ListFileViewRecordResponse = client.drive.v1.file_view_record.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.file_view_record.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()