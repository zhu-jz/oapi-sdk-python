# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 创建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: PatchEmployeeRequest = PatchEmployeeRequest.builder() \
		.employee_id("123") \
		.user_id_type("open_id") \
		.department_id_type("people_admin_department_id") \
		.request_body(ChangeEmployeeStage.builder()
					  .operation(1)
					  .conversion_info(EmployeeConversionInfo.builder().build())
					  .overboard_info(EmployeeOverboardInfo.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: PatchEmployeeResponse = client.hire.v1.employee.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.employee.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()