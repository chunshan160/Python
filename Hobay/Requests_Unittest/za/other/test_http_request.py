#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/14 21:49
# @Author :春衫
# @File :test_http_request.py

import unittest
from Requests_Unittest.tools.project_path import test_case_path
from ddt import ddt, data  # 列表嵌套列表  列表嵌套字典
from Requests_Unittest.za.http_request2 import HttpRequest
from Requests_Unittest.tools.get_data import GetData
from Requests_Unittest.za.do_excel import DoExcel
from Requests_Unittest.tools.UserLog import MyLog
from Requests_Unittest.tools.do_sql import DoMysql

my_logger = MyLog()

test_data = DoExcel.get_data(test_case_path)


@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):

        global TestResult
        # 请求之前完成loanID的替换

        if item['data'].find('${loan_id}') != -1:
            if getattr(GetData, 'loan_id') == None:
                query_sql = 'select max(Id) from loan where memberID={0};'.format(getattr(GetData, 'loan_member_id'))
                loan_id = DoMysql().do_mysql(query_sql)[0][0]
                item['data'] = item['data'].replace('${loan_id}', str(loan_id))
                setattr(GetData, 'loan_id', loan_id)  # 利用这个反射区存储结果
            else:
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData, 'loan_id')))
        my_logger.info('获取到的请求数据是{0}'.format(item['data']))
        res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'],
                                         getattr(GetData, "Cookie"))

        actual_code = res.json()['code']  # 实际结果

        if res.cookies:  # 如果有cookies，那就res.cookies赋值给Cookie属性
            setattr(GetData, 'Cookie', res.cookies)  # 反射
        try:
            self.assertEqual(str(item['expected_code']), actual_code)
            print("用例{0}正确！".format(item['case_id']), item['title'])
            TestResult = 'PASS'
        except AssertionError as e:
            my_logger.info("用例错误！错误原因是{0}：".format(e))
            TestResult = 'Failed'
            raise e  # 异常处理完后记得抛出
        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, item['sheet_name'], item['case_id'] + 1, str(res.json()), TestResult)
            my_logger.error("获取到的结果是：{0}".format(res.json()))

    def tearDown(self):
        pass
