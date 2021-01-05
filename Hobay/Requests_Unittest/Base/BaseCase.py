#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/27 17:05
# @Author :春衫
# @File :BaseCase.py
import decimal
import unittest
import random
import re
import jmespath

from Requests_Unittest.Base.GlobalEnvironment import GlobalEnvironment
from Requests_Unittest.tools.do_sql import DoMysql


class BaseCase:

    def params_replace_all_case_info(self, caseInfoList):
        """

        Parameters
        ----------
        caseInfoList：当前测试类中的所有测试用例数据

        Returns：参数化替换之后的用例数据
        -------

        """
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        for caseInfo in caseInfoList:
            # 如果数据是为空的，没有必要去进行参数化的处理
            if caseInfo['requestHeader'] != None:
                requestHeader = self.regex_replace(caseInfo['requestHeader'])
                caseInfo['requestHeader'] = eval(requestHeader)

            if caseInfo['url'] != None:
                url = self.regex_replace(caseInfo['url'])
                caseInfo['url'] = url

            if caseInfo['inputParams'] != None:
                inputParams = self.regex_replace(caseInfo['inputParams'])
                caseInfo['inputParams'] = eval(inputParams)

            if caseInfo['expected'] != None:
                expected = self.regex_replace(caseInfo['expected'])
                caseInfo['expected'] = eval(expected)

            if caseInfo['checkSQL'] != None:
                expected = self.regex_replace(caseInfo['checkSQL'])
                caseInfo['checkSQL'] = eval(expected)

        return caseInfoList

    def params_replace_current_case_info(self, caseInfo):
        """

        Parameters
        ----------
        caseInfo：当前测试类中的某个用例

        Returns：参数化替换之后的用例数据
        -------

        """
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        # 如果数据是为空的，没有必要去进行参数化的处理
        if caseInfo['requestHeader'] != None:
            requestHeader = self.regex_replace(caseInfo['requestHeader'])
            caseInfo['requestHeader'] = eval(requestHeader)

        if caseInfo['url'] != None:
            url = self.regex_replace(caseInfo['url'])
            caseInfo['url'] = url

        if caseInfo['inputParams'] != None:
            inputParams = self.regex_replace(caseInfo['inputParams'])
            caseInfo['inputParams'] = eval(inputParams)

        if caseInfo['expected'] != None:
            expected = self.regex_replace(caseInfo['expected'])
            caseInfo['expected'] = eval(expected)

        if caseInfo['checkSQL'] != None:
            expected = self.regex_replace(caseInfo['checkSQL'])
            caseInfo['checkSQL'] = eval(expected)

        return caseInfo

    def regex_replace(self, sourceStr):

        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        while re.search('{{(.*?)}}', str(sourceStr)):
            key = re.search('{{(.*?)}}', str(sourceStr)).group(0)
            value = re.search('{{(.*?)}}', str(sourceStr)).group(1)
            new_value = str(GlobalEnvironment().get(value))
            sourceStr = str(sourceStr).replace(key, new_value)

        return sourceStr

    # def get_phone(self):
    #     #缺陷，会留出很多空白没有注册的手机号
    #     phonePrefix = [133, 134]
    #     choice_num = random.choice(phonePrefix)
    #     sql = f"SELECT mobile_phone FROM `futureloan`.`member` WHERE `mobile_phone` LIKE '{choice_num}%' ORDER BY `mobile_phone` DESC LIMIT 1;"
    #     res = DoMysql().do_mysql(sql)
    #     mobile_phone = eval(res[0][0])
    #     return mobile_phone

    def get_random_phone(self):
        # 随机生成一个手机号码
        # 定义手机的号段
        phone_prefix_list = ["133", "137", "189"]
        while True:
            phone_prefix = random.choice(phone_prefix_list)
            choice_num = str(random.randint(0, 99999999)).zfill(8)
            phone = phone_prefix + choice_num
            sql = f"select count(*) from member where mobile_phone={phone};"
            res = DoMysql("tuple").query_one(sql)
            if res[0] == 0:
                return eval(phone)

    def assert_expected(self, caseInfo, res):
        # 用例公共的断言方法，断言期望值和实际值
        expected = caseInfo['expected']
        for i in expected.keys():
            result = jmespath.search(i, res.json())
            # unittest.TestCase().assertEqual(expected[i], result, "期望值断言失败:{}".format(i))
            assert expected[i] == result

    def assert_SQL(self, caseInfo):
        check_SQL_data = caseInfo['checkSQL']
        if check_SQL_data != None:
            for sql in check_SQL_data.keys():
                actual = DoMysql("tuple").query_one_value(sql)

                if isinstance(actual, decimal.Decimal):
                    expected = decimal.Decimal(str(check_SQL_data[sql]))
                else:
                    expected = check_SQL_data[sql]
                # unittest.TestCase().assertEqual(expected, actual, "数据库断言失败:{}".format(sql))
                assert expected == actual


if __name__ == '__main__':
    res = BaseCase().get_random_phone()
    print(res)
