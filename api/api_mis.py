import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("正在初始化mis登录url为：{}".format(self.url_login))
        # 查询文章url
        self.url_search = api.host + "/mis/v1_0/articles"
        log.info("正在初始化mis查询文章url为：{}".format(self.url_search))
        # 审核文章url
        self.url_audit = api.host + "/mis/v1_0/articles"
        log.info("正在初始化mis审核文章url为：{}".format(self.url_audit))

    # 登录
    def api_mis_login(self, account, password):
        data = {"account": account, "password": password}
        log.info("正在调用mis登录接口，请求数据为：{}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询文章
    def api_mis_search(self):
        data = {"title": api.article_title, "channel": api.channel}
        log.info("正在调用mis查询文章接口，请求数据为：{}".format(data))
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 审核文章
    def api_mis_audit(self):
        data = {"article_ids": [api.article_id], "status": 2}
        log.info("正在调用mis审核文章接口，请求数据为：{}".format(data))
        return requests.put(url=self.url_audit, json=data, headers=api.headers)

