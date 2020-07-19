#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:49
# @Author :春衫
# @File :test_http_request.py

import unittest
from tools.project_path import *
from ddt import ddt, data  # 列表嵌套列表  列表嵌套字典
from tools.http_request import HttpRequest
from tools.get_data import GetData
from tools.do_excel import DoExcel

test_data = DoExcel.get_data(test_case_path)


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):

        global TestResult
        res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'],
                                         getattr(GetData, "Cookie"))

        actual_code = res.json()['code']  # 实际结果

        if res.cookies:  # 如果有cookies，那就res.cookies赋值给Cookie属性
            setattr(GetData, 'Cookie', res.cookies)  # 反射
        try:
            self.assertEqual(str(item['expected_code']), actual_code)
            print("用例{0}正确！".format(item['case_id']), item['title'])
            TestResult = 'PASS'
        except AssertionError as e:
            print("用例错误！错误原因是{0}：".format(e))
            TestResult = 'Failed'
            raise e  # 异常处理完后记得抛出
        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, item['sheet_name'], item['case_id'] + 1, str(res.json()), TestResult)
            print("响应体：", "\n", res.json())

    def tearDown(self):
        pass
