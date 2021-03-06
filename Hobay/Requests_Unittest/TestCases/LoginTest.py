#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:15
# @Author :春衫
# @File :test__login.py

import unittest
import jmespath
import requests

from ddt import ddt, data
<<<<<<< HEAD:Hobay/Requests_Unittest/TestCases/LoginTest.py
from Requests_Unittest.tools.do_excel import DoExcel
from Requests_Unittest.tools.project_path import test_case_path
from Requests_Unittest.Base.BaseCase import BaseCase
from Requests_Unittest.Base.GlobalEnvironment import GlobalEnvironment
=======
from Requests.tools.do_excel import DoExcel
from Requests.tools.project_path import test_case_path
from Requests.Base.BaseCase import BaseCase
from Requests.Base.GlobalEnvironment import GlobalEnvironment
>>>>>>> fa779a6d0b1dea49d1cf17bbd4d8db0c1dc7f8af:Hobay/Requests/TestCases/LoginTest.py


@ddt
class LoginTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "login")

    @classmethod
    def setUpClass(cls):
        print("=======所有测试用例执行之前，setupClass整个测试类只执行一次==========")
        caseInfoList = BaseCase().params_replace_all_case_info(cls.caseInfoList)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")

    @data(*caseInfoList)
    def test_login(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.post(url, json=body, headers=headers)

        # 断言
        # 1、响应结果断言
        BaseCase().assert_expected(caseInfo, res)

        member_id = jmespath.search("data.id", res.json())
        if member_id != None:
            token = jmespath.search("data.token_info.token", res.json())
            if caseInfo["caseId"] == 1:
                # 2、保存到环境变量中
                GlobalEnvironment().put("token1", token)

            elif caseInfo["caseId"] == 2:
                # 2、保存到环境变量中
                GlobalEnvironment().put("token2", token)

            elif caseInfo["caseId"] == 3:
                # 2、保存到环境变量中
                GlobalEnvironment().put("token3", token)
