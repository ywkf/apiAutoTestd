import pytest

import api
from api.api_mp import ApiMp
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()


class TestMp:

    # 初始化
    def setup_class(self):
        self.mp = ApiMp()

    # 测试登录
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_login(self, mobile, code):
        response = self.mp.api_mp_login(mobile, code)
        try:
            Tool.common_token(response)
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

    # 测试发布文章
    # @pytest.mark.parametrize("title,content,channel_id", read_yaml("mp_article.yaml"))
    def test02_article(self, title=api.article_title, content=api.article_content, channel_id=api.channel_id):
        response = self.mp.api_mp_article(title, content, channel_id)
        article_id = response.json().get("data").get("id")
        log.info("发布文章id为：{}".format(article_id))
        try:
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

