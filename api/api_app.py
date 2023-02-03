import time

import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.host + "/app/v1_0/authorizations"
        log.info("正在初始化app登录url：{}".format(self.url_login))
        # 查询频道文章url
        self.url_article = api.host + "/app/v1_0/articles"
        log.info("正在初始化app查询频道文章url：{}".format(self.url_article))

    # 登录
    def api_app_login(self, mobile, code):
        data = {"mobile": mobile, "code": code}
        log.info("正在调用app登录接口，请求数据为：{}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询频道文章
    def api_app_article(self):
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}
        log.info("正在调用app查询频道文章接口，请求数据为：{}".format(data))
        return requests.get(url=self.url_article, params=data, headers=api.headers)

