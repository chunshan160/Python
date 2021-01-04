#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/22 16:46
# @Author :春衫
# @File :RegisterTest.py

import unittest

import ddt
import jmespath
import requests

from Requests.Base.BaseCase import BaseCase
from Requests.Base.GlobalEnvironment import GlobalEnvironment

from Requests.tools.do_excel import DoExcel
from Requests.tools.project_path import test_case_path


@ddt.ddt
class RegisterTest(unittest.TestCase):
    caseInfoList = DoExcel.getCaseDataFromExcel(test_case_path, "register")

    @classmethod
    def setUpClass(cls):
        print("=======所有测试用例执行之前，setUpClass==========")
        GlobalEnvironment()._init()

    @classmethod
    def tearDownClass(cls):
        print("=======所有测试用例执行之后，tearDownClass==========")

    @ddt.data(*caseInfoList)
    def testRegister(self, caseInfo):
        # 读数据库获取没有注册过的手机号码
        if caseInfo["caseId"] == 1:
            mobile_phone = BaseCase().get_random_phone()
            GlobalEnvironment().put("mobile_phone1", str(mobile_phone + 1))
        elif caseInfo["caseId"] == 2:
            mobile_phone = BaseCase().get_random_phone()
            GlobalEnvironment().put("mobile_phone2", str(mobile_phone + 2))
        elif caseInfo["caseId"] == 3:
            mobile_phone = BaseCase().get_random_phone()
            GlobalEnvironment().put("mobile_phone3", str(mobile_phone + 3))

        # 对当前的case进行参数化替换
        caseInfo = BaseCase().params_replace_current_case_info(caseInfo)

        headers = caseInfo['requestHeader']
        body = caseInfo['inputParams']
        url = "http://api.lemonban.com/futureloan" + caseInfo['url']
        res = requests.post(url, json=body, headers=headers)

        # 断言
        # 1、响应结果断言
        BaseCase().assert_expected(caseInfo, res)
        # 2、数据库断言
        BaseCase().assert_SQL(caseInfo)

        memberId = jmespath.search("data.id", res.json())
        if memberId != None:
            mobile_phone = jmespath.search("data.mobile_phone", res.json())
            # 3、注册成功的密码--从用例数据里面
            pwd = caseInfo['inputParams']['pwd']
            if caseInfo["caseId"] == 1:
                # 2、保存到环境变量中
                GlobalEnvironment().put("mobile_phone1", mobile_phone)
                GlobalEnvironment().put("member_id1", memberId)
                GlobalEnvironment().put("pwd1", pwd)

            elif caseInfo["caseId"] == 2:
                # 2、保存到环境变量中
                GlobalEnvironment().put("mobile_phone2", mobile_phone)
                GlobalEnvironment().put("member_id2", memberId)
                GlobalEnvironment().put("pwd2", pwd)

            elif caseInfo["caseId"] == 3:
                # 2、保存到环境变量中
                GlobalEnvironment().put("mobile_phone3", mobile_phone)
                GlobalEnvironment().put("member_id3", memberId)
                GlobalEnvironment().put("pwd3", pwd)
