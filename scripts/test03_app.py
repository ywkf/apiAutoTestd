import pytest

from api.api_app import ApiApp
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()


class TestApp:

    # 初始化
    def setup_class(self):
        self.app = ApiApp()

    # 测试登录
    @pytest.mark.parametrize("mobile,code", read_yaml("app_login.yaml"))
    def test01_login(self, mobile, code):
        response = self.app.api_app_login(mobile, code)
        try:
            Tool.common_token(response)
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

    # 测试查询频道文章
    def test02_article(self):
        response = self.app.api_app_article()
        try:
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise




