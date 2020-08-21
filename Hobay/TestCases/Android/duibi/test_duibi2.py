#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/25 14:40
# @Author :春衫
# @File :test_duibi.py

import unittest
from ddt import ddt, data
from Common.DoExcel.do_excel import DoExcel
from Common.DoMysql.sql import SQL
from Common.WalletDetail.Calculation_Data import CalculationData
from TestData.test_data import IP
# 别删这个decimal 也别注释掉
from Common.project_path import *
from Common.user_log import UserLog
import warnings
from Common.WalletDetail.new_muban.moban2 import MoBan
from Common.WalletDetail.new_muban.Fan_Hui import FanHui

test_data = DoExcel().get_data(test_case_path)
my_logger = UserLog()


@ddt
class DuiBi(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        warnings.simplefilter("ignore", ResourceWarning)
        my_logger.info("=======开始进行对比==========")

    @data(*test_data)
    def test_2_duibi(self, item):

        try:
            sheet_name=item['sheet_name']
            case_id=item['case_id']
            title=item['title']
            ip = IP[item['surroundings']]
            payment_method = item['payment_method']
            member_level = item['member_level']
            buyer_identity = item['buyer_identity']
            seller_identity = item['seller_identity']
            test_data=eval(item['data'])
            proportion = eval(item['proportion'])
            reserve_fund = eval(item['reserve_fund'])
            superior=eval(item['superior'])
            order = item['order']

            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    charge_amount = reserve_fund['charge_amount']
                    reserve_fund = reserve_fund['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            calculation_data = CalculationData().calculation_data(ip, payment_method, member_level,
                                                                  buyer_identity, seller_identity, proportion,
                                                                  charge_amount, reserve_fund, order)

            transaction_second_payagent_ratio = eval(item['second_payagent_ratio'])

            if payment_method in ["易贝", "易贝券"]:
                bind_buyer_relationship_data = eval(item['bind_relationship_data'])

                expected_moban = MoBan(buyer_identity, seller_identity, member_level, payment_method,
                                       order).expected_moban(ip, test_data, superior,reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data)

            elif payment_method in ["抵工资", "家人购", "现金"]:
                bind_buyer_relationship_data = eval(item['bind_relationship_data']["储备金二级分佣对象"])
                bind_payer_relationship_data = eval(item['bind_relationship_data']["支付服务费二级分佣对象"])

                expected_moban = MoBan(buyer_identity, seller_identity, member_level, payment_method,
                                       order).expected_moban(ip, test_data, superior,reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data, bind_payer_relationship_data)

            # 写回Excel用
            fanhui = FanHui().fan_hui(ip, order, expected_moban)

            sql_data = SQL(ip).wallet_detail(order)

            for i in range(0, len(expected_moban)):
                self.assertEqual(expected_moban[i], sql_data[i])

            self.assertEqual(expected_moban, sql_data)

            my_logger.info("用例{0}正确！{1}".format(case_id, title))
            TestResult = 'Pass'
            Error = None

        except AssertionError as e:
            my_logger.info("用例错误！错误原因是第{0}行，{1}：".format(i + 1, e))
            TestResult = 'Failed'
            Error = "用例错误！错误原因是：第{0}行，{1}：".format(i + 1, e)
            raise e  # 异常处理完后记得抛出

        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, sheet_name, case_id + 1,
                                 str(fanhui[0]), str(fanhui[2]), str(expected_moban),
                                 str(sql_data), TestResult, str(Error))

    def tearDown(cls):
        my_logger.info("----------测试用例执行结束----------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
