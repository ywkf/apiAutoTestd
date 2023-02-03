import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class Tool:

    # 提取token
    @classmethod
    def common_token(cls, response):
        token = response.json().get("data").get("token")
        api.headers["Authorization"] = "Bearer " + token
        log.info("正在提取token，提取后的headers为：{}".format(api.headers))
        print("headers为: ", api.headers)

    # 断言
    @classmethod
    def common_assert(cls, response, status_code=200, message="OK"):
        log.info("正在调用公共断言方法")
        # 断言状态码
        assert status_code == response.status_code
        # 断言响应信息
        assert message == response.json().get("message")

