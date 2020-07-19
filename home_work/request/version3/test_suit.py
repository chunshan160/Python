#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/4 19:36
# @Author :春衫
# @File :test_result.py

import unittest
import HTMLTestRunnerNew
from home_work.request.version3.test_case import TestHttpRequest
from home_work.request.version3.do_excel import DoExcel

test_data = DoExcel("test.xlsx", "python").get_data()

suite = unittest.TestSuite()
for item in test_data:  # 创建实例
    suite.addTest(TestHttpRequest("test_api", item['test_case'],item['url'], eval(item['data']), item['method'], item['expected_status'],
                                  item['expected_code'], item['expected_msg']))  # 以实例的方式去加载用例

# 执行  打开后关闭 减少使用内存
with open("test_report.html", 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="qm")
    runner.run(suite)
