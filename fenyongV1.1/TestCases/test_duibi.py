#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/25 14:40
# @Author :春衫
# @File :test_duibi.py

from tools.project_path import *
import unittest
from ddt import ddt, data
from DoExcel.do_excel import DoExcel
from Do_mysql.sql import SQL
from muban.template import GeShiHua
from muban.title import Title
from Calculation.calculation import A
from test_data.test_data import IP
# 别删这个decimal 也别注释掉
from decimal import *
from tools.project_path import *
from tools.my_log import MyLog
import warnings

test_data = DoExcel().get_data(test_case_path)
my_logger = MyLog()

@ddt
class DuiBi(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        warnings.simplefilter("ignore", ResourceWarning)
        my_logger.info("=======开始执行测试用例==========")



    @data(*test_data)
    def test_2_duibi(self, item):

        global i, expected_userid, fanhui, expected_changes, expected, sql_data, TestResult, Error

        try:

            ip = IP[item['surroundings']]

            if item['payment_method'] in ["易贝", "易贝券"]:
                buyer_province_proportion = eval(item['proportion'])['省分佣比例']
                buyer_city_proportion = eval(item['proportion'])['市分佣比例']
                buyer_area_proportion = eval(item['proportion'])['区分佣比例']
                buyer_personal_proportion = eval(item['proportion'])['个人分佣比例']
                disanfang_province_proportion = None
                disanfang_city_proportion = None
                disanfang_area_proportion = None
                disanfang_personal_proportion = None
            else:
                buyer_province_proportion = (eval(item['proportion']))['储备池分佣']['省分佣比例']
                buyer_city_proportion = (eval(item['proportion']))['储备池分佣']['市分佣比例']
                buyer_area_proportion = (eval(item['proportion']))['储备池分佣']['区分佣比例']
                buyer_personal_proportion = (eval(item['proportion']))['储备池分佣']['个人分佣比例']
                disanfang_province_proportion = (eval(item['proportion']))['支付服务费分佣']['省分佣比例']
                disanfang_city_proportion = (eval(item['proportion']))['支付服务费分佣']['市分佣比例']
                disanfang_area_proportion = (eval(item['proportion']))['支付服务费分佣']['区分佣比例']
                disanfang_personal_proportion = (eval(item['proportion']))['支付服务费分佣']['个人分佣比例']

            if item['buyer_identity'] == "公海用户":
                if item['seller_identity'] == "个人焕商" or item['seller_identity'] == "非焕商且已绑定个人焕商":
                    charge_amount = eval(item['reserve_fund'])['charge_amount']
                    reserve_fund = eval(item['reserve_fund'])['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            # 预期分佣的用户id流水
            expected_userid = GeShiHua(item['buyer_identity'], item['seller_identity'], item['member_level'],
                                       item['payment_method'], item['order']).userid(eval(item['data']),
                                                                                     eval(item['superior']))
            # print("expected_userid", expected_userid)

            # 计算出来的（商品价格，需要支付的易贝服务费，需要支付的现金服务费）（储备池分佣）（服务费分佣）
            calculation = A(item['buyer_identity'], item['seller_identity'],
                            buyer_province_proportion=buyer_province_proportion,
                            buyer_city_proportion=buyer_city_proportion,
                            buyer_area_proportion=buyer_area_proportion,
                            buyer_personal_proportion=buyer_personal_proportion,
                            disanfang_province_proportion=disanfang_province_proportion,
                            disanfang_city_proportion=disanfang_city_proportion,
                            disanfang_area_proportion=disanfang_area_proportion,
                            disanfang_personal_proportion=disanfang_personal_proportion, ).transaction(ip,
                                                                                                       item[
                                                                                                           'member_level'],
                                                                                                       item[
                                                                                                           'payment_method'],
                                                                                                       item['order'],
                                                                                                       charge_amount,
                                                                                                       reserve_fund)

            # print("calculation", calculation)

            # 预期的变化金额值流水
            expected_changes = GeShiHua(item['buyer_identity'], item['seller_identity'], item['member_level'],
                                        item['payment_method'], item['order']).expected_changes(ip, calculation,
                                                                                                reserve_fund=reserve_fund)
            # print('expected_changes', expected_changes)

            # 预期的流水
            expected = GeShiHua(item['buyer_identity'], item['seller_identity'], item['member_level'],
                                item['payment_method'], item['order']).expected(ip, calculation, eval(item['data']),
                                                                                eval(item['superior']),
                                                                                reserve_fund=reserve_fund)
            # print("expected", expected)

            # 写回Excel用
            fanhui = GeShiHua(item['buyer_identity'], item['seller_identity'], item['member_level'],
                              item['payment_method'], item['order']).fanhui(ip, eval(item['superior']))

            sql_data = SQL(ip).wallet_detail(item['order'])

            shuju = Title(item['buyer_identity'], item['seller_identity'],
                           item['payment_method']).title(eval(item['superior']))

            for i in range(0, len(shuju)):
                self.assertEqual(expected[i], sql_data[i])

            self.assertEqual(expected, sql_data)

            my_logger.info("用例{0}正确！{1}".format(item['case_id'], item['title']))
            TestResult = 'Pass'
            Error = None

        except AssertionError as e:
            my_logger.info("用例错误！错误原因是第{0}行，{1}：".format(i + 1, e))
            TestResult = 'Failed'
            Error = "用例错误！错误原因是：第{0}行，{1}：".format(i + 1, e)
            raise e  # 异常处理完后记得抛出

        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, item['sheet_name'], item['case_id'] + 1, str(expected_userid),
                                 str(fanhui[0]), str(expected_changes), str(fanhui[2]), str(expected),
                                 str(sql_data), TestResult, str(Error))


    def tearDown(cls):
        my_logger.info("----------测试用例执行结束----------")

if __name__ == '__main__':
    unittest.main(verbosity=2)