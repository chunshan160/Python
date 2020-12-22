#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:46
# @Author :春衫
# @File :RegisterTest.py

import unittest

import ddt
import jmespath
import requests
from Requests.data.GlobalEnvironment import GlobalEnvironment as gl

from Requests.tools.do_excel2 import DoExcel
from Requests.tools.project_path import test_case_path


@ddt.ddt
class RegisterTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path,"register")

    # @classmethod
    # def setUp(cls):
    #     print("=======所有测试用例执行之前，setup整个测试类只执行一次==========")
    #     # caseInfoList=DoRegx.do_regx(caseInfoList)
    #
    # @classmethod
    # def tearDown(cls):
    #     print("=======所有测试用例执行之后，tearDown整个测试类只执行一次==========")

    @ddt.data(*caseInfoList)
    def testRegister(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.post(url, json=body, headers=headers)
        # print(res.json())
        expected = caseInfo['expected']
        for i in expected.keys():
            result = jmespath.search(i, res.json())
            self.assertEqual(expected[i], result)

        memberId = jmespath.search("data.id", res.json())
        if memberId != None:
            # 2、保存到环境变量中
            mobilephone = jmespath.search("data.mobile_phone", res.json())
            # print("保存到环境变量中mobile_phone：：" + mobilephone)
            gl()._init()
            gl().set_value("mobile_phone", mobilephone)
            # 3、注册成功的密码--从用例数据里面
            pwd = caseInfo['inputParams']['pwd']
            # print("保存到环境变量中pwd：：" + pwd)
            gl().set_value("pwd", pwd)

