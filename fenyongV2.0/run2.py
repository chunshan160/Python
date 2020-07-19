#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/6 18:08
# @Author :春衫
# @File :run.py

from TestCases.test_buygoods4 import TestBuyGoods
import unittest
import HTMLTestRunnerNew
from tools.project_path import *


suite = unittest.TestSuite()
loader = unittest.TestLoader()
# 购买、确认收货、写回订单、解绑、处理数据、对比
suite.addTest(loader.loadTestsFromTestCase(TestBuyGoods))

# run = unittest.TextTestRunner(verbosity=2)  # 用来执行测试用例
# run.run(suite)  # 执行被加载的测试用例

with open(test_report_path, 'wb') as file:
    # 执行用例
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="自动化测试报告", description="V2.5.9焕商分佣2.0",
                                              tester="春衫")
    runner.run(suite)
