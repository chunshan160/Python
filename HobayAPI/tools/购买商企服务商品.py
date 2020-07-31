#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:11
# @Author :春衫
# @File :购买商企服务商品.py

from tools.http_request import HttpRequest


def buy_goods(buyer_phone, seller_phone, productStockId,payType):
    # 买家登录
    login_url = 'http://m.dev1.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 买家提交订单
    SaveOrder_url = 'http://m.dev1.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": "",
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 3}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data, cookies=login_res.cookies,
                                               headers=SaveOrder_headers)
    print("提交订单结果是：", SaveOrder_res.json())

    # 买家支付订单
    order = SaveOrder_res.json()['data']['tradeNum']
    pay_url = "http://m.dev1.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
    pay_data = {"tradeNUm": order, "payType": 3, "shareWalletUserId": "", "shareWalletId": ""}
    pay_headers = {"login": "", "payPassword": "xqdt77d9tjE="}
    pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=login_res.cookies,
                                         headers=pay_headers)
    print("支付订单的结果是：", pay_res.json())
    print("订单编号", pay_res.json()['data']['orderNums'][0])

    # 卖家登录
    login2_url = 'http://m.dev1.hobay.com.cn/api/app/user/login'  # 登录
    login2_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    login2_res = HttpRequest().http_request(login2_url, "post", json=login2_data)
    print("登录结果是：", login2_res.json())

    # 确认订单
    orderId = SaveOrder_res.json()['data']['orderId']
    AcceptOrder_url = f"http://m.dev1.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={orderId}"
    AcceptOrder_headers = {"login": ""}
    AcceptOrder_res = HttpRequest().http_request(AcceptOrder_url, "get", cookies=login2_res.cookies,
                                                 headers=AcceptOrder_headers)
    print("确认订单的结果是：", AcceptOrder_res.json())

    # 签约
    sellerUserId = login2_res.json()['userId']
    signed_url = f"http://m.dev1.hobay.com.cn/ribbon-api/orders/signed"
    data = {"orderId": orderId, "payType": 3, "sellerUserId": sellerUserId}
    headers = {"login": "", "payPassword": "xqdt77d9tjE="}
    signed_res = HttpRequest().http_request(signed_url, "post", data=data, cookies=login_res.cookies,
                                            headers=headers)
    print("签约的结果是：", signed_res.json())

if __name__ == '__main__':
    buy_goods(17777777781, 13724765586, 359326)
