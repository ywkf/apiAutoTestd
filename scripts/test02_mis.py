import pytest

from api.api_mis import ApiMis
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()


class TestMis:

    # 初始化
    def setup_class(self):
        self.mis = ApiMis()

    # 测试登录
    @pytest.mark.parametrize("account,password", read_yaml("mis_login.yaml"))
    def test01_login(self, account, password):
        response = self.mis.api_mis_login(account, password)
        try:
            Tool.common_token(response)
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

    # 测试查询文章
    def test02_search(self):
        response = self.mis.api_mis_search()
        try:
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

    # 测试审核文章
    def test03_audit(self):
        response = self.mis.api_mis_audit()
        try:
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

