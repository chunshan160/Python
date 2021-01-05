#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/28 15:32
# @Author :春衫
# @File :test_add_loan.py

import unittest

import jmespath
import requests
from ddt import ddt, data
from Requests_Unittest.Base.BaseCase import BaseCase
from Requests_Unittest.Base.GlobalEnvironment import GlobalEnvironment
from Requests_Unittest.tools.do_excel import DoExcel
from Requests_Unittest.tools.project_path import test_case_path


@ddt
class AddLoanTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "addLoan")

    @classmethod
    def setUpClass(cls):
        print("=======所有测试用例执行之前，setupClass整个测试类只执行一次==========")
        caseInfoList = BaseCase().params_replace_all_case_info(cls.caseInfoList)

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass整个测试类只执行一次==========")

    @data(*caseInfoList)
    def test_add_loan(self, caseInfo):
        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.post(url, json=body, headers=headers)

        # 断言
        # 1、响应结果断言
        BaseCase().assert_expected(caseInfo, res)

        memberId = jmespath.search("data.member_id", res.json())
        if memberId != None:
            loan_id = jmespath.search("data.id", res.json())
            # 2、保存到环境变量中
            GlobalEnvironment().put("loan_id", loan_id)
