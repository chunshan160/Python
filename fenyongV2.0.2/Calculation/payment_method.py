#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/23 11:47
# @Author :春衫
# @File :payment_method.py

from test_data.test_data import yibei as yb
from test_data.test_data import xianjin as xj
from decimal import *


class PaymentMethod:

    def payment_method(self, member_level, payment_method, price):
        '''

        :param member_level: 会员等级
        :param payment_method: 支付方式
        :param price: 商品价格
        :return:
        '''
        yibei = float(price) * yb[member_level]  # 需要支付的易贝服务费
        yibei = Decimal(str(yibei)).quantize(Decimal('0.00'))

        cash = float(price) * xj[member_level]  # 需要支付的现金服务费
        cash = Decimal(str(cash)).quantize(Decimal('0.00'))

        goods_price = Decimal(str(price)).quantize(Decimal('0.00'))

        if payment_method == "易贝":
            print("买家需要支付易贝服务费：{0}".format(yibei))
            print("买家需要支付现金服务费：{0}".format(cash))
            return goods_price, yibei, cash
        elif payment_method == "易贝券":
            print("买家不需要支付易贝服务费")
            print("买家不需要支付现金服务费")
            return goods_price
        elif payment_method == "抵工资":
            print("企业需要支付易贝服务费：{0}".format(yibei))
            print("企业需要支付现金服务费：{0}".format(cash))
            return goods_price, yibei, cash
        elif payment_method == "家人购":
            print("家人需要支付易贝服务费：{0}".format(yibei))
            print("家人需要支付现金服务费：{0}".format(cash))
            return goods_price, yibei, cash
        else:
            cash = float(price) * (yb[member_level] + xj[member_level])
            cash = Decimal(str(cash)).quantize(Decimal('0.00'))
            print("卖家不需要支付易贝服务费")
            print("卖家需要支付现金服务费：{0}".format(cash))
            return goods_price,cash


if __name__ == '__main__':
    a = PaymentMethod().payment_method("钻石会员", "易贝", 10)
    print(a)
    b = '8.50'
    print(b)
