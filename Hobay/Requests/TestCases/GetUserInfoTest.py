#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/23 11:20
# @Author :春衫
# @File :GetUserInfoTest.py

import unittest

import jmespath
import requests
from ddt import ddt, data

from Requests.Base.BaseCase import BaseCase
from Requests.tools.do_excel import DoExcel
from Requests.tools.project_path import test_case_path


@ddt
class GetUserInfoTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "getUserInfo")

    @classmethod
    def setUpClass(cls):
        print("=======所有测试用例执行之前，setupClass整个测试类只执行一次==========")
        caseInfoList = BaseCase().params_replace_all_case_info(cls.caseInfoList)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")

    @data(*caseInfoList)
    def testGetUserInfo(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.get(url, json=body, headers=headers)

        # 断言
        # 1、响应结果断言
        BaseCase().assert_expected(caseInfo, res)
