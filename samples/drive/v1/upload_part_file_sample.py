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
	file = open("file_path", "rb")
	request: UploadPartFileRequest = UploadPartFileRequest.builder() \
		.request_body(UploadPartFileRequestBody.builder()
					  .upload_id("7111211691345512356")
					  .seq(0)
					  .size(4194304)
					  .checksum("12342388237783212356")
					  .file(file)
					  .build()) \
		.build()

	# 发起请求
	response: UploadPartFileResponse = client.drive.v1.file.upload_part(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.file.upload_part failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()