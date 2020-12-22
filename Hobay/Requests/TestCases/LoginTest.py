#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:15
# @Author :春衫
# @File :LoginTest.py

import unittest
import jmespath
import requests

from ddt import ddt, data, unpack
from Requests.tools.do_excel2 import DoExcel
from Requests.tools.project_path import test_case_path
from Requests.Base.BaseCase import BaseCase
from Requests.data.GlobalEnvironment import GlobalEnvironment as gl


@ddt
class LoginTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "login")

    @classmethod
    def setUpClass(cls):
        print("=======所有测试用例执行之前，setupClass整个测试类只执行一次==========")
        caseInfoList = BaseCase().paramsReplace(cls.caseInfoList)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")

    @data(*caseInfoList)
    def testLogin(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.post(url, json=body, headers=headers)

        expected = caseInfo['expected']
        for i in expected.keys():
            result = jmespath.search(i, res.json())
            self.assertEqual(expected[i], result)

        member_id = jmespath.search("data.id", res.json())
        if member_id != None:
            # 2、保存到环境变量中
            cookies = res.cookies
            # gl()._init()
            gl().set_value("cookies", cookies)
