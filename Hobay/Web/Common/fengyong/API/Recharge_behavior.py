#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 1:07
# @Author :春衫
# @File :Recharge_behavior.py

from Web.Common.fengyong.API.login import login
from Web.Common.fengyong.API.pay import Pay
from Web.Common import recharge
from Web.Common import UserLog

my_logger = UserLog()
def recharge_behavior(surroundings, buyer_phone, payPassword, payAmount=100):
    # 买家登录
    buyer_login_res = login(surroundings, buyer_phone)
    my_logger.debug(f"登录结果是：{buyer_login_res.json()}")

    # 提交充值订单
    recharge_res = recharge(surroundings, payAmount,cookies=buyer_login_res.cookies)
    my_logger.debug(f"充值的结果是：{recharge_res.json()}")

    # 买家支付订单
    buyer_orderNum = recharge_res.json()['results']['ordersNum']
    buyer_pay_res = Pay(surroundings, buyer_orderNum, payPassword, 7, cookies=buyer_login_res.cookies)
    my_logger.debug(f"支付订单的结果是：{buyer_pay_res.json()}")


if __name__ == '__main__':
    surroundings = 'test'
    buyer_phone = 17777777781
    payPassword = 'qhr7qcahoKc='
    payAmount = 100
    a=recharge_behavior(surroundings, buyer_phone, payPassword, payAmount=100)
    print(a)
