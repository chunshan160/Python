#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:59
# @Author :春衫
# @File :run.py

import unittest
import HTMLTestReportCN
from Requests.TestCases.RegisterTest import RegisterTest
from Requests.TestCases.LoginTest import LoginTest
from tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTest))
suite.addTest(loader.loadTestsFromTestCase(LoginTest))


# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

with open(test_report_path, 'wb') as file:
    # 执行用例
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="春衫")
    runner.run(suite)
