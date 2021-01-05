#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:59
# @Author :春衫
# @File :run.py

import unittest
import HTMLTestReportCN
# from Requests_Unittest.tools.project_path import *
from Requests_Unittest.TestCases.RegisterTest import RegisterTest
from Requests_Unittest.TestCases.LoginTest import LoginTest
from Requests_Unittest.TestCases.GetUserInfoTest import GetUserInfoTest
from Requests_Unittest.TestCases.RechargeTest import RechargeTest
from Requests_Unittest.TestCases.AddLoanTest import AddLoanTest
from Requests_Unittest.TestCases.AuditLoanTest import AuditLoanTest
from Requests_Unittest.TestCases.InvestTest import InvestTest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTest))
suite.addTest(loader.loadTestsFromTestCase(LoginTest))
suite.addTest(loader.loadTestsFromTestCase(GetUserInfoTest))
suite.addTest(loader.loadTestsFromTestCase(RechargeTest))
suite.addTest(loader.loadTestsFromTestCase(AddLoanTest))
suite.addTest(loader.loadTestsFromTestCase(AuditLoanTest))
suite.addTest(loader.loadTestsFromTestCase(InvestTest))






runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# with open(test_report_path, 'wb') as file:
#     # 执行用例
#     runner = HTMLTestReportCN.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
#                                               tester="春衫")
#     runner.run(suite)
