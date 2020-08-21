#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/1 1:07
# @Author :春衫
# @File :Recharge_requests.py

from tools.http_request import HttpRequest


def recharge(surroundings,buyer_phone,payPassword, payAmount=100):
    # 买家登录
    buyer_login_url = f'http://m.{surroundings}.hobay.com.cn/api/app/user/login'  # 登录
    buyer_login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    buyer_login_res = HttpRequest().http_request(buyer_login_url, "post", json=buyer_login_data)
    print("登录结果是：", buyer_login_res.json())

    # 充值
    recharge_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/charge/saveServiceFeeOrders'
    recharge_data = {"payAmount": payAmount}
    recharge_headers = {"login": ""}
    recharge_res = HttpRequest.http_request(recharge_url, "post", data=recharge_data, headers=recharge_headers,
                                                        cookies=buyer_login_res.cookies)
    print("充值的结果是：", recharge_res.json())

    # 买家支付订单
    orderNum = recharge_res.json()['results']['ordersNum']
    pay_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/pay/payCash"
    pay_data = {"tradeNum": orderNum}
    print(pay_data)
    pay_headers = {"login": "", "payPassword": payPassword}
    pay_res = HttpRequest().http_request(pay_url, "post", data=pay_data, cookies=buyer_login_res.cookies,
                                         headers=pay_headers)
    print("支付订单的结果是：", pay_res.json())

if __name__ == '__main__':
    recharge(17777777776,)
