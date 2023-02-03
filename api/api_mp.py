import api
import requests

from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.host + "/mp/v1_0/authorizations"
        log.info("正在初始化mp登录url为：{}".format(self.url_login))
        # 发布文章url
        self.url_article = api.host + "/mp/v1_0/articles"
        log.info("正在初始化mp发布文章url为：{}".format(self.url_article))

    # 登录
    def api_mp_login(self, mobile, code):
        data = {"mobile": mobile, "code": code}
        log.info("正在调用mp登录接口，请求数据为：{}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章
    def api_mp_article(self, title, content, channel_id):
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "image": []}}
        log.info("正在调用mp发布文章接口，请求数据为：{}".format(data))
        return requests.post(url=self.url_article, json=data, headers=api.headers)

