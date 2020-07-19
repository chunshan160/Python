#!/usr/bin/env python.txt
# -*- coding:utf-8 -*-
# @Time :2020/4/23 11:47
# @Author :春衫
# @File :payment_method.py

from fenyong.test_data import yibei as yb
from fenyong.test_data import xianjin as xj


class Pay:

    def yibei(self, price, member_level_ratio):  # 商品价格*会员等级费率
        yibei = price * yb[member_level_ratio]  # 需要支付的易贝服务费
        cash = price * xj[member_level_ratio]  # 需要支付的现金服务费
        print("买家需要支付易贝服务费：{0}".format(yibei))
        print("买家需要支付现金服务费：{0}".format(cash))
        return yibei, cash

    def yibeiquan(self):
        print("买家不需要支付易贝服务费")
        print("买家不需要支付现金服务费")
        cash=0
        return cash

    def digongzi(self, price, member_level_ratio):
        yibei = price * yb[member_level_ratio]  # 需要支付的易贝服务费
        cash = price * xj[member_level_ratio]  # 需要支付的现金服务费
        print("企业需要支付易贝服务费：{0}".format(yibei))
        print("企业需要支付现金服务费：{0}".format(cash))
        return yibei, cash

    def jiarengou(self, price, member_level_ratio):
        yibei = price * yb[member_level_ratio]  # 需要支付的易贝服务费
        cash = price * xj[member_level_ratio]  # 需要支付的现金服务费
        print("家人需要支付易贝服务费：{0}".format(yibei))
        print("家人需要支付现金服务费：{0}".format(cash))
        return yibei, cash

    def xianjin(self, price, member_level_ratio):
        cash = price * xj[member_level_ratio]  # 需要支付的现金服务费
        print("卖家不需要支付易贝服务费")
        print("卖家需要支付现金服务费：{0}".format(cash))
        return cash


if __name__ == '__main__':
    a = Pay().xianjin(1000, "钻石会员")
    print(a)
