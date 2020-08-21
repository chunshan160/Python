#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/3 17:17
# @Author :春衫
# @File :test_BuyGoods.py


import unittest
import warnings
from decimal import *
from ddt import ddt, data
from DoExcel.do_excel import DoExcel
from Do_mysql.sql import SQL
from new_muban.moban2 import MoBan
from new_muban.Fan_Hui import FanHui
from shangji.Superior_template import SuperiorTemplate
from tools.Calculation_Data import CalculationData
from test_data.test_data import IP
from tools.project_path import *
from tools.my_log import MyLog
from tools.BuyEntityGoods import bug_entity_goods
from tools.BuyCouponGoods import buy_coupon_goods
from tools.BuyServerGoods import buy_server_goods
from tools.boss_setting import BossSetting
from tools.bing_relationship_data import BingRelationshipData
from tools.TransactionSecondPayagentRatio import TransactionSecondPayagentRatio
from tools.delete_partner import delete_partner
from tools.Recharge_requests import recharge

my_logger = MyLog()
test_data = DoExcel().get_data(test_case_path)


@ddt
class TestBuyGoods(unittest.TestCase):

    @data(*test_data)
    @classmethod
    def setUp(cls, item):
        # 用setUpClass就能只打开浏览器一次，setUp则是每条用例都执行一次
        warnings.simplefilter("ignore", ResourceWarning)
        my_logger.info("----------开始执行用例{0}，环境是{1}----------".format(item['case_id'], item['surroundings']))

        ip = IP[item['surroundings']]
        data = eval(item['data'])
        buyer_phone = data['buyer_phone']
        seller_phone = data['seller_phone']

        # 获取绑定关系
        superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)
        # 环境
        surroundings = item['surroundings']
        # Boss后台运营设置
        operational_setting = eval(item['operational_setting'])

        print("----------开始BOSS后台设置运营分佣比例操作----------")
        # Boss后台设置运营分佣比例
        BossSetting().main(ip, surroundings, item['payment_method'], superior, operational_setting)
        print("----------BOSS后台运营分佣比例设置完毕----------")

        buyer_identity = item['buyer_identity']
        seller_identity = item['seller_identity']
        payPassword=item['payPassword']
        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                # 充值
                recharge(surroundings, buyer_phone,payPassword)
                # 写回储备池和充值金额
                user_id = data["买家"]
                reserve_fund_data = SQL(ip).reserve_fund_data(user_id)
                DoExcel.reserve_fund(test_case_path, item['sheet_name'], item['case_id'], str(reserve_fund_data))

        if item['payment_method'] == "易贝":
            payType = 3
        elif item['payment_method'] == "易贝券":
            payType = 4
        elif item['payment_method'] == "家人购":
            payType = 5
        elif item['payment_method'] == "抵工资":
            payType = 6
        # 暂不兼容现金支付，不兼容接口传参

        # 根据商品名判断流程
        if "实物商品" in item['goodsname']:
            order = bug_entity_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,payPassword)

        elif "本地服务" in item['goodsname']:
            order = buy_coupon_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,payPassword)

        elif "商企服务" in item['goodsname']:
            order = buy_server_goods(surroundings, buyer_phone, seller_phone, item['goodsname'], payType,payPassword)

        # 写回订单号
        buyerid = data['买家']
        DoExcel.get_order(test_case_path, item['sheet_name'], item['case_id'], order)

        # 获取绑定关系，写回Excel
        superior = SuperiorTemplate().superior_template_main(ip, item['payment_method'], item['data'], buyer_phone)
        DoExcel.superior(test_case_path, item['sheet_name'], item['case_id'], str(superior))

        # 获取上级分佣比例，写回Excel
        proportion = SuperiorTemplate().fenyong_template_main(ip, item['payment_method'], superior)
        DoExcel.fenyong_bili(test_case_path, item['sheet_name'], item['case_id'], str(proportion))

        # 解绑
        if buyer_identity == "公海用户":
            if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                if seller_identity == "个人焕商":
                    delete_partner(surroundings, seller_phone, buyerid)
                elif seller_identity == "非焕商且已绑定个人焕商":
                    bangding_phone = data['bangding_phone']
                    delete_partner(surroundings, bangding_phone, buyerid)

        my_logger.info("----------前端操作执行完毕----------")

        ip = IP[item['surroundings']]


        buyer_id = data['买家']

        # 查询买家是否绑定销售/业务焕商/TCO
        if item['payment_method'] in ["易贝", "易贝券"]:
            # 获取买家绑定的销售/业务焕商/TCO dict
            bind_buyer_relationship_data = BingRelationshipData().bing_relationship_data(ip, item['payment_method'],
                                                                                         data, buyer_id)

            # 把买家上级销售/业务焕商的上级写回Excel
            DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                   str(bind_buyer_relationship_data))

        elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
            bind_relationship_data = BingRelationshipData().bing_relationship_data(ip, item['payment_method'], data,
                                                                                   buyer_id)
            bind_buyer_relationship_data = bind_relationship_data[0]
            bind_payer_relationship_data = bind_relationship_data[1]
            # 买家上级销售/业务焕商的上级，写回模板
            bind_buyer_relationship_id = {"储备金二级分佣对象": bind_buyer_relationship_data,
                                          "支付服务费二级分佣对象": bind_payer_relationship_data}
            DoExcel().bing_sale_id(test_case_path, item['sheet_name'], item['case_id'],
                                   str(bind_buyer_relationship_id))

        # 获取这笔订单应该【使用】的二级分佣比例
        transaction_second_payagent_ratio = TransactionSecondPayagentRatio().transaction_second_payagent_ratio(ip, item[
            'payment_method'], superior, data)
        # 把这笔订单所使用的二级分佣比例写回Excel
        DoExcel().second_payagent_ratio(test_case_path, item['sheet_name'], item['case_id'],
                                        str(transaction_second_payagent_ratio))

    @data(*test_data)
    # 购买实物商品
    def test_1_buy_goods(self, item):
        my_logger.info("----------开始进行对比----------")
        ip = IP[item['surroundings']]
        buyer_identity = item['buyer_identity']
        seller_identity = item['seller_identity']
        data=eval(item['data'])
        reserve_fund_data = eval(item['reserve_fund'])
        proportion = eval(item['proportion'])
        order = item['order']
        superior = eval(item['superior'])
        # 这笔订单应该【使用】的二级分佣比例
        transaction_second_payagent_ratio = eval(item['second_payagent_ratio'])
        bind_relationship_data = eval(item['bind_relationship_data'])

        try:
            if buyer_identity == "公海用户":
                if seller_identity == "个人焕商" or seller_identity == "非焕商且已绑定个人焕商":
                    charge_amount = reserve_fund_data['charge_amount']
                    reserve_fund = reserve_fund_data['reserve_fund']
                else:
                    charge_amount = None
                    reserve_fund = None
            else:
                charge_amount = None
                reserve_fund = None

            calculation_data = CalculationData().calculation_data(ip, item['payment_method'], item['member_level'],
                                                                  buyer_identity, seller_identity, proportion,
                                                                  charge_amount, reserve_fund, order)

            if item['payment_method'] in ["易贝", "易贝券"]:
                bind_buyer_relationship_data = bind_relationship_data
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data, superior, reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data)

            elif item['payment_method'] in ["抵工资", "家人购", "现金"]:
                bind_buyer_relationship_data = bind_relationship_data['储备金二级分佣对象']
                bind_payer_relationship_data = bind_relationship_data['支付服务费二级分佣对象']
                expected_moban = MoBan(buyer_identity, seller_identity, item['member_level'], item['payment_method'],
                                       order).expected_moban(ip, data, superior, reserve_fund, calculation_data,
                                                             transaction_second_payagent_ratio,
                                                             bind_buyer_relationship_data, bind_payer_relationship_data)

            # 写回Excel用
            fanhui = FanHui().fan_hui(ip, order, expected_moban)

            sql_data = SQL(ip).wallet_detail(order)

            for i in range(0, len(expected_moban)):
                self.assertEqual(expected_moban[i], sql_data[i])

            self.assertEqual(expected_moban, sql_data)
            my_logger.info("用例{0}正确！{1}".format(item['case_id'], item['title']))
            TestResult = 'Pass'
            Error = None

        except AssertionError as e:
            my_logger.info("用例错误！错误原因是第{0}行，{1}：".format(i + 1, e))
            TestResult = 'Failed'
            Error = "用例错误！错误原因是：第{0}行，{1}：".format(i + 1, e)
            raise e  # 异常处理完后记得抛出

        finally:  # 不管怎样都得写入Excel
            DoExcel().write_back(test_case_path, item['sheet_name'], item['case_id'] + 1,
                                 str(fanhui[0]), str(fanhui[2]), str(expected_moban),
                                 str(sql_data), TestResult, str(Error))

        # time.sleep(2)
        my_logger.info("----------对比结束----------")
        my_logger.info("----------用例{0}执行完毕----------".format(item['case_id']))

    def tearDown(cls):
        my_logger.info("----------结束----------")


if __name__ == '__main__':
    unittest.main(verbosity=2)
