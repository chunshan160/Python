#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/5 23:06
# @Author :春衫
# @File :test_case.py

import unittest
from API_AUTO.test_request import HttpRequest
from API_AUTO.get_cookie import GetCookie


class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    #超继承
    def __init__(self, methodName, test_case,url, data, method, expected_status, expected_code, expected_msg):  # 通过初始化函数来传参
        super(TestHttpRequest, self).__init__(methodName)  # 超继承  不能直接重写父类的init  因为不完整 破坏了框架
        self.test_case=test_case
        self.url = url
        self.data = data
        self.method = method
        self.expected_status = expected_status
        self.expected_code = expected_code
        self.expected_msg = expected_msg

    # 正常登录
    def test_api(self):

        res = HttpRequest().http_request(self.url, self.data, self.method, getattr(GetCookie, "Cookie"))

        actual_status = res.json()['status']
        actual_code = res.json()['code']
        actual_msg = res.json()['msg']

        if res.cookies:  # 如果有cookies，那就res.cookies赋值给Cookie属性
            setattr(GetCookie, 'Cookie', res.cookies)  # 反射
        try:
            self.assertEqual(self.expected_msg, str(actual_msg))
            self.assertEqual(self.expected_status, str(actual_status))
            self.assertEqual(self.expected_code, str(actual_code))
            print("用例正确！",self.test_case)
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            raise e  # 异常处理完后记得抛出
        print("响应体：", "\n", res.json())

    def tearDown(self):
        pass