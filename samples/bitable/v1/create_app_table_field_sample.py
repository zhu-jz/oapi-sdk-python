# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CreateAppTableFieldRequest = CreateAppTableFieldRequest.builder() \
		.app_token("appbcbWCzen6D8dezhoCH2RpMAh") \
		.table_id("tblsRc9GRRXKqhvW") \
		.client_token("fe599b60-450f-46ff-b2ef-9f6675625b97") \
		.request_body(AppTableField.builder()
					  .field_name("字段名称")
					  .type(1)
					  .property(AppTableFieldProperty.builder().build())
					  .description(AppTableFieldDescription.builder().build())
					  .ui_type("Progress")
					  .build()) \
		.build()

	# 发起请求
	response: CreateAppTableFieldResponse = client.bitable.v1.app_table_field.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.bitable.v1.app_table_field.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()