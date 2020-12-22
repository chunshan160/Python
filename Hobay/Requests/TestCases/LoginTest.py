#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:15
# @Author :春衫
# @File :LoginTest.py

import unittest
import ddt
import requests
from Requests.tools.do_excel2 import DoExcel
from Requests.tools.project_path import test_case_path
from Requests.Base.BaseCase import BaseCase

@ddt.ddt
class LoginTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path)
    caseInfoList=BaseCase().paramsReplace(caseInfoList)

    @classmethod
    def setUp(cls):
        print("=======所有测试用例执行之前，setup整个测试类只执行一次==========")
        # caseInfoList=DoRegx.do_regx(caseInfoList)

    @classmethod
    def tearDown(cls):
        print("=======所有测试用例执行之后，tearDown整个测试类只执行一次==========")

    @ddt.data(*caseInfoList)
    def testLogin(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url="http://api.lemonban.com/futureloan"+caseInfo['url']
        res =requests.post(url,json=body,headers=headers)
        print(res.json())
