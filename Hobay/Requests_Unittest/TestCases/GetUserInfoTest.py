#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/23 11:20
# @Author :春衫
# @File :test__get_user_info.py

import unittest

import jmespath
import requests
from ddt import ddt, data

<<<<<<< HEAD:Hobay/Requests_Unittest/TestCases/GetUserInfoTest.py
from Requests_Unittest.Base.BaseCase import BaseCase
from Requests_Unittest.tools.do_excel import DoExcel
from Requests_Unittest.tools.project_path import test_case_path
=======
from Requests.Base.BaseCase import BaseCase
from Requests.tools.do_excel import DoExcel
from Requests.tools.project_path import test_case_path
>>>>>>> fa779a6d0b1dea49d1cf17bbd4d8db0c1dc7f8af:Hobay/Requests/TestCases/GetUserInfoTest.py


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
    def test_get_user_info(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.get(url, json=body, headers=headers)

        # 断言
        # 1、响应结果断言
        BaseCase().assert_expected(caseInfo, res)
