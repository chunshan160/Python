#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/4 19:36
# @Author :春衫
# @File :test_result.py

import unittest
import HTMLTestRunnerNew
from home_work.request.version2.test_case import TestHttpRequest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

# 执行  打开后关闭 减少使用内存
with open("test_report.html", 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="qm")
    runner.run(suite)
