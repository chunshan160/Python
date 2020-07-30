#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/5 18:42
# @Author :春衫
# @File :test_case.py

import unittest
from home_work.request.version1.test_request import HttpRequest
from API_AUTO.get_cookie import GetCookie

#如何解决用例之间的依赖   第二条用例需要用到第一条用例返回的结果
#方法1：写到setUP里
#方法2: 全局变量 局部变量
#缺点就是关联性比较强  一步错 步步错
# COOKIE = None

#方法3：setattr(GetData, 'Cookie', "小黄")

class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        # 登录  +self代表可以被实例调用 被类调用
        self.login_url = 'http://8.129.65.165:8080/futureloan/mvc/api/member/login'
        self.login_data = {"mobilephone": "13724765586", "pwd": "123456"}
        self.cookies = HttpRequest().http_request(self.login_url, self.login_data, 'get').cookies
        print("获取登录后的cookies是：{0}".format(self.cookies))
        # 充值
        self.recharge_url = 'http://8.129.65.165:8080/futureloan/mvc/api//member/recharge'
        self.recharge_data = {"mobilephone": "13724765586", "amount": "10"}

    # 正常登录
    def test_1_normal_login(self):

        # global COOKIE

        res = HttpRequest().http_request(self.login_url, self.login_data, 'get')

        expected_status = "1"
        actual_status = res.json()['status']
        expected_code = "10001"
        actual_code = res.json()['code']
        expected_msg = "登录成功"
        actual_msg = res.json()['msg']
        if res.cookies:  # 如果有cookies，那就把COOKIE复制
            # COOKIE = res.cookies #方法1
            setattr(GetData, 'Cookie', res.cookies)
        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！输入正确手机号和密码，登录成功！")
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            raise e  # 异常处理完后记得抛出
        print("响应体：", "\n", res.json())

    # 不输入密码
    def test_2_no_pwd(self):
        login_data = {"mobilephone": "13724765586", "pwd": ""}
        res = HttpRequest().http_request(self.login_url, login_data, 'get')

        expected_status = "0"
        actual_status = res.json()['status']
        expected_code = "20103"
        actual_code = res.json()['code']
        expected_msg = "密码不能为空"
        actual_msg = res.json()['msg']

        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！不输入密码时，会提示：密码不能为空")
            print("响应体：", "\n", res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", res.json())
            raise e  # 异常处理完后记得抛出

    # 不输入账号
    def test_3_no_phone(self):
        login_data = {"mobilephone": "", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, login_data, 'get')

        expected_status = "0"
        actual_status = res.json()['status']
        expected_code = "20103"
        actual_code = res.json()['code']
        expected_msg = "手机号不能为空"
        actual_msg = res.json()['msg']

        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！不输入手机号时，会提示：手机号不能为空")
            print("响应体：", "\n", res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", res.json())
            raise e  # 异常处理完后记得抛出

    # 输入错误密码
    def test_4_error_pwd(self):
        login_data = {"mobilephone": "13724765586", "pwd": "12345"}
        res = HttpRequest().http_request(self.login_url, login_data, 'get')

        expected_status = "0"
        actual_status = res.json()['status']
        expected_code = "20111"
        actual_code = res.json()['code']
        expected_msg = "用户名或密码错误"
        actual_msg = res.json()['msg']

        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！输入错误密码时，会提示：用户名或密码错误！")
            print("响应体：", "\n", res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", res.json())
            raise e  # 异常处理完后记得抛出

    # 正常充值
    def test_5_normal_login(self):

        # global COOKIE

        recharge_res = HttpRequest().http_request(self.recharge_url, self.recharge_data, 'post', getattr(GetData,"Cookie"))
        expected_status = "1"
        actual_status = recharge_res.json()['status']
        expected_code = "10001"
        actual_code = recharge_res.json()['code']
        expected_msg = "充值成功"
        actual_msg = recharge_res.json()['msg']
        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！输入正确的手机号和充值金额，充值成功")
            print("响应体：", "\n", recharge_res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", recharge_res.json())
            raise e  # 异常处理完后记得抛出

    # 不输入账号、不输入金额一个、输入错误的金额负数
    def test_6_no_recharge(self):
        recharge_data = {"mobilephone": "", "amount": "10"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', getattr(GetData,"Cookie"))
        expected_status = "0"
        actual_status = recharge_res.json()['status']
        expected_code = "20103"
        actual_code = recharge_res.json()['code']
        expected_msg = "手机号不能为空"
        actual_msg = recharge_res.json()['msg']
        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！不输入手机号时会提示：手机号不能为空！")
            print("响应体：", "\n", recharge_res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", recharge_res.json())
            raise e  # 异常处理完后记得抛出

    # 不输入金额一个、输入错误的金额负数
    def test_7_no_recharge(self):
        recharge_data = {"mobilephone": "13724765586", "amount": ""}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', getattr(GetData,"Cookie"))
        expected_status = "0"
        actual_status = recharge_res.json()['status']
        expected_code = "20115"
        actual_code = recharge_res.json()['code']
        expected_msg = "请输入金额"
        actual_msg = recharge_res.json()['msg']
        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！不输入充值金额时会提示：请输入金额！")
            print("响应体：", "\n", recharge_res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", recharge_res.json())
            raise e  # 异常处理完后记得抛出

    # 输入错误的金额 负数
    def test_8_no_recharge(self):
        recharge_data = {"mobilephone": "13724765586", "amount": "-100"}
        recharge_res = HttpRequest().http_request(self.recharge_url, recharge_data, 'post', getattr(GetData,"Cookie"))
        expected_status = "0"
        actual_status = recharge_res.json()['status']
        expected_code = "20117"
        actual_code = recharge_res.json()['code']
        expected_msg = "请输入范围在0到50万之间的正数金额"
        actual_msg = recharge_res.json()['msg']
        try:
            self.assertEqual(expected_msg, str(actual_msg))
            self.assertEqual(expected_status, str(actual_status))
            self.assertEqual(expected_code, str(actual_code))
            print("用例正确！不输入充值金额时会提示：请输入范围在0到50万之间的正数金额！")
            print("响应体：", "\n", recharge_res.json())
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            print("响应体：", "\n", recharge_res.json())
            raise e  # 异常处理完后记得抛出

    def tearDown(self):
        pass
