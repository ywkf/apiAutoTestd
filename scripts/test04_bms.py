import sys
import os

print(os.getcwd())

from locust import TaskSet, task, HttpUser

import api

import pytest

from api.api_bms import ApiBms
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
from tool.tool import Tool
log = GetLog.get_logger()


class TestBms(TaskSet):

    # 初始化
    def setup_class(self):
        self.bms = ApiBms()

    # 初始化
    def on_start(self):
        self.setup_class()

    # 测试登录
    # @pytest.mark.parametrize("mobile,code", read_yaml("bms_login.yaml"))
    @task
    def test01_login(self, mobile="19933333333", code="123456"):
        response = self.bms.api_bms_login(self, mobile, code)
        try:
            Tool.common_token(response)
            Tool.common_assert(response, message="操作成功")
        except Exception as e:
            log.error(e)
            raise

    # 测试首页
    @task
    def test02_index(self):
        response = self.bms.api_bms_index(self)
        try:
            Tool.common_assert(response)
        except Exception as e:
            log.error(e)
            raise

    # 测试获取用户信息
    @task
    def test03_profile(self):
        response = self.bms.api_bms_profile(self)
        try:
            Tool.common_assert(response, message="操作成功")
        except Exception as e:
            log.error(e)
            raise

    # 测试登出
    @task
    def test04_logout(self):
        response = self.bms.api_bms_logout(self)
        try:
            Tool.common_assert(response, message="操作成功 ")
        except Exception as e:
            log.error(e)
            raise


class UserRun(HttpUser):
    tasks = [TestBms]
    host = api.host



