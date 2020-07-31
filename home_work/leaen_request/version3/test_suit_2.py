#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/4 19:36
# @Author :春衫
# @File :test_result.py

import unittest
import HTMLTestRunnerNew
from home_work.request.version3.test_case import TestHttpRequest
from home_work.request.version3.do_excel_2 import DoExcel

t = DoExcel("test.xlsx", "python")

suite = unittest.TestSuite()
for i in range(2,t.max_row+1):  # 创建实例
    suite.addTest(TestHttpRequest("test_api", t.get_data(i,1),t.get_data(i,2),eval(t.get_data(i,3)),t.get_data(i,4),str(t.get_data(i,5)),str(t.get_data(i,6)),t.get_data(i,7)))  # 以实例的方式去加载用例

# 执行  打开后关闭 减少使用内存
with open("test_report.html", 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="qm")
    runner.run(suite)
