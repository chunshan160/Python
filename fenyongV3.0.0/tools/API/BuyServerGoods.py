#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:11
# @Author :春衫
# @File :BuyServerGoods.py
from tools.API.login import login
from tools.API.productStockId import get_productStockId
from tools.http_request import HttpRequest


def buy_server_goods(surroundings, buyer_phone, seller_phone, product_name, payType, payPassword):
    # 卖家登录
    seller_login_res = login(surroundings, seller_phone)
    # print("卖家登录结果是：", seller_login_res.json())

    # 获取商品productStockId
    productStockId = get_productStockId(surroundings, product_name, cookies=seller_login_res.cookies)

    # 买家登录
    buyer_login_res = login(surroundings, buyer_phone)
    # print("登录结果是：", login_res.json())

    # 买家提交订单
    buyer_SaveOrder_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    buyer_SaveOrder_data = {"message": "", "couponUserId": "", "addressId": "",
                            "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 3}
    buyer_SaveOrder_headers = {"login": ""}
    buyer_SaveOrder_res = HttpRequest().http_request(buyer_SaveOrder_url, "post", json=buyer_SaveOrder_data,
                                                     cookies=buyer_login_res.cookies,
                                                     headers=buyer_SaveOrder_headers)
    # print("提交订单结果是：", buyer_SaveOrder_res.json())

    # 查询买家各种钱包明细
    myPayWay_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/userWallet/myPayWay"
    myPayWay_headers = {"login": ""}
    myPayWay_res = HttpRequest().http_request(myPayWay_url, "get", headers=myPayWay_headers,
                                              cookies=buyer_login_res.cookies)
    # print("买家各种钱包明细是：", myPayWay_res.json())

    # 支付订单
    orderNum = buyer_SaveOrder_res.json()['data']['orderNum']
    if payType in [3, 4]:
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/payAllCBP'
        pay_data = {"tradeNUm": orderNum, "payType": payType, "shareWalletUserId": "", "shareWalletId": ""}
    elif payType in [5, 6]:
        if payType == 5:
            shareWalletUserId = myPayWay_res.json()['results']['myPayWay']['myKinship'][0]['shareWalletUserId']
            shareWalletId = myPayWay_res.json()['results']['myPayWay']['myKinship'][0]['shareWalletId']
        else:
            shareWalletUserId = myPayWay_res.json()['results']['myPayWay']['myWages']['shareWalletUserId']
            shareWalletId = myPayWay_res.json()['results']['myPayWay']['myWages']['shareWalletId']
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/batchOrders/payAllCBP'
        pay_data = {"tradeNum": orderNum, "payType": payType, "shareWalletUserId": shareWalletUserId,
                    "shareWalletId": shareWalletId}
    elif payType == 7:
        pay_url = f'http://m.{surroundings}.hobay.com.cn/ribbon-api/pay/payCash'
        pay_data = {"tradeNum": orderNum}
    pay_headers = {"login": "", "payPassword": payPassword}
    pay_res = HttpRequest().http_request(pay_url, "post", data=pay_data, cookies=buyer_login_res.cookies,
                                         headers=pay_headers)
    # print("支付订单的结果是：", pay_res.json())

    # 确认订单
    buyer_orderId = buyer_SaveOrder_res.json()['data']['orderId']
    seller_AcceptOrder_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={buyer_orderId}"
    seller_AcceptOrder_headers = {"login": ""}
    seller_AcceptOrder_res = HttpRequest().http_request(seller_AcceptOrder_url, "get", cookies=seller_login_res.cookies,
                                                        headers=seller_AcceptOrder_headers)
    # print("确认订单的结果是：", seller_AcceptOrder_res.json())

    # 签约
    sellerUserId = seller_login_res.json()['userId']
    buyer_signed_url = f"http://m.{surroundings}.hobay.com.cn/ribbon-api/orders/signed"
    buyer_signed_data = {"orderId": buyer_orderId, "payType": payType, "sellerUserId": sellerUserId}
    buyer_signed_headers = {"login": "", "payPassword": payPassword}
    buyer_signed_res = HttpRequest().http_request(buyer_signed_url, "post", data=buyer_signed_data,
                                                  cookies=buyer_login_res.cookies,
                                                  headers=buyer_signed_headers)
    # print("签约的结果是：", buyer_signed_res.json())

    return orderNum


if __name__ == '__main__':
    # buy_server_goods("test", 13724765586, 17777777781, "一天两件商企服务", 3, "gQyzNznHAvc=")
    buy_server_goods("test", 13724765586, 17777777781, "两天一件商企服务", 3, "gQyzNznHAvc=")
