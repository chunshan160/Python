#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:11
# @Author :春衫
# @File :BuyServerGoods.py

from tools.http_request import HttpRequest


def buy_server_goods(buyer_phone, seller_phone, product_name, payType,payPassword):

    # 卖家登录
    seller_login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    seller_login_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    seller_login_res = HttpRequest().http_request(seller_login_url, "post", json=seller_login_data)
    print("卖家登录结果是：", seller_login_res.json())

    # 获取商品productStockId
    # 卖家-商品管理
    product_url = "http://m.test.hobay.com.cn/ribbon-api/product/queryPageProductsByType?currentPage=1&type=2&pageSize=10"
    product_headers = {"login": ""}
    product_res = HttpRequest().http_request(product_url, "get", headers=product_headers,
                                             cookies=seller_login_res.cookies)
    print("商品管理出售中的商品是：", product_res.json())

    #获取商品规格id
    product_data = product_res.json()['data']['result']
    for i in range(0, len(product_data)):
        if product_data[i]['title'] == product_name:
            productStockId = product_data[i]['productStockWithStockImages'][0]['id']
            print("商品规格id是：", productStockId)

    # 买家登录
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 买家提交订单
    SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": "",
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 3}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data, cookies=login_res.cookies,
                                               headers=SaveOrder_headers)
    print("提交订单结果是：", SaveOrder_res.json())

    # 买家支付订单
    orderNum = SaveOrder_res.json()['data']['orderNum']
    order = SaveOrder_res.json()['data']['tradeNum']
    pay_url = "http://m.test.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
    pay_data = {"tradeNUm": order, "payType": payType, "shareWalletUserId": "", "shareWalletId": ""}
    pay_headers = {"login": "", "payPassword": payPassword}
    pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=login_res.cookies,
                                         headers=pay_headers)
    print("支付订单的结果是：", pay_res.json())
    print("订单编号", pay_res.json()['data']['orderNums'][0])



    # 确认订单
    orderId = SaveOrder_res.json()['data']['orderId']
    AcceptOrder_url = f"http://m.test.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={orderId}"
    AcceptOrder_headers = {"login": ""}
    AcceptOrder_res = HttpRequest().http_request(AcceptOrder_url, "get", cookies=seller_login_res.cookies,
                                                 headers=AcceptOrder_headers)
    print("确认订单的结果是：", AcceptOrder_res.json())

    # 签约
    sellerUserId = seller_login_res.json()['userId']
    signed_url = f"http://m.test.hobay.com.cn/ribbon-api/orders/signed"
    data = {"orderId": orderId, "payType": payType, "sellerUserId": sellerUserId}
    headers = {"login": "", "payPassword": payPassword}
    signed_res = HttpRequest().http_request(signed_url, "post", data=data, cookies=login_res.cookies,
                                            headers=headers)
    print("签约的结果是：", signed_res.json())

    return orderNum

if __name__ == '__main__':
    buy_server_goods(17777777781, 17777777776, "普通焕商商企服务",3)
