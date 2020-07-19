#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:59
# @Author :春衫
# @File :run.py

import unittest
import HTMLTestRunnerNew
from tools.test_http_request import TestHttpRequest
from tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path, 'wb') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="春衫")
    runner.run(suite)
