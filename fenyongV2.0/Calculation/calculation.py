#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/23 10:11
# @Author :春衫
# @File :calculation.py

from Calculation.recharge_service_fee import Dividend
from Calculation.payment_method import PaymentMethod
from test_data.test_data import yibei as yb
from Do_mysql.sql import SQL
from DoExcel.do_excel import DoExcel
from tools.project_path import *
from decimal import *

test_data = DoExcel.get_data(test_case_path)


class A:

    def __init__(self, buyer_identity, seller_identity, buyer_province_proportion, buyer_city_proportion,
                 buyer_area_proportion, buyer_personal_proportion,
                 disanfang_province_proportion=None, disanfang_city_proportion=None,
                 disanfang_area_proportion=None, disanfang_personal_proportion=None):

        '''

        :param buyer_identity: 买家身份
        :param seller_identity: 卖家身份
        :param buyer_province_proportion: 买家上级省代分佣比例
        :param buyer_city_proportion: 买家上级市代分佣比例
        :param buyer_area_proportion: 买家上级区代分佣比例
        :param buyer_personal_proportion: 买家上级个人焕商分佣比例
        :param disanfang_province_proportion: 卖家上级省代分佣比例
        :param disanfang_city_proportion: 卖家上级市代分佣比例
        :param disanfang_area_proportion: 卖家上级区代分佣比例
        :param disanfang_personal_proportion: 卖家上级个人焕商分佣比例
        '''

        self.buyer_identity = buyer_identity  # 买家身份 1公海用户 2非公海用户
        self.seller_identity = seller_identity  # 卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        self.buyer_province_proportion = buyer_province_proportion  # 省代分佣比例
        self.buyer_city_proportion = buyer_city_proportion  # 市代分佣比例
        self.buyer_area_proportion = buyer_area_proportion  # 区代分佣比例
        self.buyer_personal_proportion = buyer_personal_proportion  # 个人焕商分佣比例
        # 抵工资 家人购
        self.disanfang_province_proportion = disanfang_province_proportion  # 省代分佣比例
        self.disanfang_city_proportion = disanfang_city_proportion  # 市代分佣比例
        self.disanfang_area_proportion = disanfang_area_proportion  # 区代分佣比例
        self.disanfang_personal_proportion = disanfang_personal_proportion  # 个人焕商分佣比例

    def recharge(self):
        # 充值
        recharge = 0  # 充值金额
        reserve_fund = 0  # 储备池金额

        while True:
            choose = input("1、充值，2、结束")
            if choose == "1":
                recharge = float(input("输入充值金额："))
                reserve_fund_amount = Dividend(self.buyer_identity, self.seller_identity,
                                               self.buyer_province_proportion,
                                               self.buyer_city_proportion, self.buyer_area_proportion,
                                               self.buyer_personal_proportion).recharge(recharge)  # 返回的是每次充值存入储备池的金额
                reserve_fund = reserve_fund + reserve_fund_amount
                print("储备池金额是：%.2f" % reserve_fund)
            else:
                print("结束了！")
                break

    def transaction(self, ip, member_level, payment_method, order, charge_amount, reserve_fund):
        global service_fee_data, pay_commission
        print("---------------------分割线-------------------------")

        # 根据订单号查流水
        sql_data = SQL(ip).wallet_detail(order)

        # 商品价格
        price = ((sql_data[0])[3]) * -1

        print("选择的会员等级是：{0}".format(member_level))
        print("选择的支付方式是：{0}".format(payment_method))

        # 通过调用方法返回的需要支付的易贝/现金服务费
        service_fee_data = PaymentMethod().payment_method(member_level, payment_method,
                                                          price)

        print("----------------计算支付服务费分佣----------------")

        # pay_service_fee方法计算服务费分佣  支付方式 要分佣的服务费 服务费分佣比例
        if payment_method in ["易贝"]:

            pay_commission = Dividend(self.buyer_identity, self.seller_identity, self.buyer_province_proportion,
                                      self.buyer_city_proportion, self.buyer_area_proportion,
                                      self.buyer_personal_proportion).pay_service_fee(payment_method,
                                                                                      service_fee_data[1],
                                                                                      yb[member_level])
        # 这些支付方式需要考虑 买家上级 和 企业/家人/卖家上级
        elif payment_method in ["抵工资", "家人购", "现金", "微信", "支付宝"]:
            pay_commission = Dividend(self.buyer_identity, self.seller_identity,
                                          self.buyer_province_proportion, self.buyer_city_proportion,
                                          self.buyer_area_proportion, self.buyer_personal_proportion,
                                          self.disanfang_province_proportion,
                                          self.disanfang_city_proportion, self.disanfang_area_proportion,
                                          self.disanfang_personal_proportion).pay_service_fee(payment_method,
                                                                                              service_fee_data[1],
                                                                                              yb[member_level])

        # 公海用户购买个人焕商商品 需要考虑储备池分佣
        if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):  # 公海用户需要考虑储备池分佣
            print("----------------计算现金服务费（储备池）分佣----------------")
            cash_commission = Dividend(self.buyer_identity, self.seller_identity, self.buyer_province_proportion,
                                       self.buyer_city_proportion, self.buyer_area_proportion,
                                       self.buyer_personal_proportion).cash_service_fee(charge_amount, reserve_fund)
            # 公海用户购买个人焕商商品  易贝券不会有支付服务费分佣 其他的需要
            if payment_method != '易贝券':
                return service_fee_data, cash_commission, pay_commission
            else:
                return service_fee_data, cash_commission
        # 其他情况都不用考虑储备池分佣
        else:
            if payment_method == '易贝券':
                return service_fee_data
            else:
                return service_fee_data, pay_commission


if __name__ == '__main__':
    pass
    # aaaaa = A(1, 1, buyer_province_proportion=0.8, buyer_city_proportion=0.7, buyer_area_proportion=0.6,
    #           buyer_personal_proportion=0.15).recharge()
    # aaaaa = A("公海用户", "个人焕商", buyer_province_proportion=0.8, buyer_city_proportion=0.7, buyer_area_proportion=0.6,
    #           buyer_personal_proportion=0.15).transaction("钻石会员", "易贝", "EC-2020051419075900011717", Decimal('100'),
    #                                                       Decimal('60.00'))
    # print(aaaaa)
