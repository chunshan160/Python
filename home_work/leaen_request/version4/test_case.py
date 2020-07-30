#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/5 23:06
# @Author :春衫
# @File :test_case.py

import unittest
from ddt import ddt, data
from API_AUTO.test_request import HttpRequest
from API_AUTO.get_cookie import GetCookie
from home_work.request.version4.do_excel import DoExcel

test_data = DoExcel("test.xlsx", "python").get_data()


@ddt
class TestHttp(unittest.TestCase):

    def setUp(self):
        print("开始测试啦！")

    @data(*test_data)
    def test_api(self, item):

        res = HttpRequest().http_request(item['url'], eval(item['data']), item['method'], getattr(GetCookie, "Cookie"))
        actual_status = res.json()['status']
        actual_code = res.json()['code']
        actual_msg = res.json()['msg']

        if res.cookies:  # 如果有cookies，那就res.cookies赋值给Cookie属性
            setattr(GetCookie, 'Cookie', res.cookies)  # 反射
        try:
            self.assertEqual(item['expected_msg'], str(actual_msg))
            self.assertEqual(item['expected_status'], str(actual_status))
            self.assertEqual(item['expected_code'], str(actual_code))
            print("用例{0}正确！".format(item['case_id']), item['test_case'])
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            raise e  # 异常处理完后记得抛出
        print("响应体：", "\n", res.json())

    def tearDown(self):
        print("测试结束啦！")
