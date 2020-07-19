#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/4 19:36
# @Author :春衫
# @File :test_result.py

import unittest
import HTMLTestRunnerNew
from home_work.request.version2.test_case import TestHttpRequest

# 列表里面嵌套的字典
test_data = [
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api/member/login",
     "data": {"mobilephone": "13724765586", "pwd": "123456"}, 'method': "get", "expected_status": "1",
     "expected_code": "10001",
     "expected_msg": "登录成功"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api/member/login",
     "data": {"mobilephone": "13724765586", "pwd": ""}, 'method': "get", "expected_status": "0",
     "expected_code": "20103",
     "expected_msg": "密码不能为空"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api/member/login", "data": {"mobilephone": "", "pwd": "123456"},
     'method': "get",
     "expected_status": "0", "expected_code": "20103",
     "expected_msg": "手机号不能为空"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api/member/login",
     "data": {"mobilephone": "13724765586", "pwd": "123"}, 'method': "get", "expected_status": "0",
     "expected_code": "20111",
     "expected_msg": "用户名或密码错误"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api//member/recharge",
     "data": {"mobilephone": "13724765586", "amount": "10"}, 'method': "post", "expected_status": "1",
     "expected_code": "10001",
     "expected_msg": "充值成功"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api//member/recharge", "data": {"mobilephone": "", "amount": "10"},
     'method': "post",
     "expected_status": "0", "expected_code": "20103",
     "expected_msg": "手机号不能为空"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api//member/recharge",
     "data": {"mobilephone": "13724765586", "amount": ""}, 'method': "post", "expected_status": "0",
     "expected_code": "20115",
     "expected_msg": "请输入金额"},
    {"url": "http://8.129.65.165:8080/futureloan/mvc/api//member/recharge",
     "data": {"mobilephone": "13724765586", "amount": "-10"}, 'method': "post", "expected_status": "0",
     "expected_code": "20117",
     "expected_msg": "请输入范围在0到50万之间的正数金额"}]

suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
for item in test_data:  # 创建实例
    suite.addTest(TestHttpRequest("test_request", item['url'], item['data'], item['method'], item['expected_status'],
                                  item['expected_code'], item['expected_msg']))  # 以实例的方式去加载用例

# 执行  打开后关闭 减少使用内存
with open("../test_report.html", 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="接口自动化测试报告", description="这里填描述",
                                              tester="qm")
    runner.run(suite)
