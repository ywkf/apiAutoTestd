import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiBms:

    # 初始化
    def __init__(self):
        # 登录url
        self.url_login = "/bms/login"
        log.info("正在初始化bms登录url为：{}".format(self.url_login))
        # 首页url
        self.url_index = "/bms/index"
        log.info("正在初始化bms首页url为：{}".format(self.url_index))
        # 获取用户信息url
        self.url_profile = "/bms/profile"
        log.info("正在初始化bms获取用户信息url为：{}".format(self.url_profile))
        # 登出url
        self.url_logout = "/bms/logout"
        log.info("正在初始化bms登出url为：{}".format(self.url_logout))

    # 登录
    def api_bms_login(self, r, mobile, code):
        data = {"mobile": mobile, "code": code}
        log.info("正在调用bms登录接口，请求数据为：{}".format(data))
        return r.client.post(url=self.url_login, json=data, headers=api.headers)

    # 首页
    def api_bms_index(self, r):
        data = {}
        log.info("正在调用bms首页接口，请求数据为：{}".format(data))
        return r.client.get(url=self.url_index, params=data, headers=api.headers)

    # 获取用户信息
    def api_bms_profile(self, r):
        data = {"profile": 1}
        log.info("正在调用bms获取用户信息接口，请求数据为：{}".format(data))
        return r.client.get(url=self.url_profile, params=data, headers=api.headers)

    # 登出
    def api_bms_logout(self, r):
        data = {}
        log.info("正在调用bms登出接口，请求数据为：{}".format(data))
        return r.client.post(url=self.url_logout, json=data, headers=api.headers)



