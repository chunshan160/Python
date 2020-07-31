#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/28 11:48
# @Author :春衫
# @File :购买实物商品.py
import time

from tools.http_request import HttpRequest


def bug_goods(buyer_phone, seller_phone, product_name, payType):
    # 卖家登录
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    seller_login_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    seller_login_res = HttpRequest().http_request(login_url, "post", json=seller_login_data)
    print("登录结果是：", seller_login_res.json())

    # 获取商品productStockId
    # 卖家-商品管理
    product_url = "http://m.test.hobay.com.cn/ribbon-api/product/queryPageProductsByType?currentPage=1&type=2&pageSize=10"
    product_headers = {"login": ""}
    product_res = HttpRequest().http_request(product_url, "get", headers=product_headers,
                                             cookies=seller_login_res.cookies)
    # print("商品管理出售中的商品是：", product_res.json())

    # 获取商品规格id
    product_data = product_res.json()['data']['result']
    for i in range(0, len(product_data)):
        if product_data[i]['title'] == product_name:
            productStockId = product_data[i]['productStockWithStockImages'][0]['id']
            print("商品规格id是：", productStockId)

    # 买家登录
    buyer_login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    buyer_login_res = HttpRequest().http_request(login_url, "post", json=buyer_login_data)
    print("登录结果是：", buyer_login_res.json())

    # 获取收货地址
    address_url = "http://m.test.hobay.com.cn/api/user/graphql/flat"
    address_data = {
        "query": "query currentUser{\n        currentUser{\n          receiveAddress(page:1,pageSize:100){\n            numPerPage\n            pageNum\n            totalCount\n            totalPage\n            recordList{\n              id\n              name\n              provinceName\n              cityName\n              areaName\n              detailAddress\n              phone\n              default\n            }\n          }\n        }\n      }"}
    address_headers = {"login": ""}
    address_res = HttpRequest().http_request(address_url, 'post', json=address_data,
                                             cookies=buyer_login_res.cookies,
                                             headers=address_headers)
    print("获取收货地址的结果是：", address_res.json())

    # 提交订单
    SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    SaveOrder_data = {"message": "", "couponUserId": "", "addressId": "",
                      "productStockIdAndNums": [{"num": 1, "productStockId": productStockId}], "type": 2}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data,
                                               cookies=buyer_login_res.cookies,
                                               headers=SaveOrder_headers)
    print("提交订单结果是：", SaveOrder_res.json())

    # 支付订单
    orderNum = SaveOrder_res.json()['data']['orderNum']
    pay_url = "http://m.test.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
    pay_data = {"tradeNUm": orderNum, "payType": payType, "shareWalletUserId": "", "shareWalletId": ""}
    pay_headers = {"login": "", "payPassword": "Y6QsYMqOfRI="}
    pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=buyer_login_res.cookies,
                                         headers=pay_headers)
    print("支付订单的结果是：", pay_res.json())

    # 卖家确认订单
    orderId = SaveOrder_res.json()['data']['orderId']
    order_data = {'orderStatus': 0,
                  'buyOrSell': 2,
                  'type': 0,
                  'currentPage': 1,
                  'pageSize': 10}
    AcceptOrder_url = f"http://m.test.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={orderId}"
    AcceptOrder_headers = {"login": ""}
    AcceptOrder_res = HttpRequest().http_request(AcceptOrder_url, "get", json=order_data,
                                                 cookies=seller_login_res.cookies, headers=AcceptOrder_headers)
    print("确认订单的结果是：", AcceptOrder_res.json())

    # 获取买家订单序列号
    print(orderId)
    OrderDetail_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/queryOrderDetail'
    OrderDetail_data = {"orderId": orderId, "buyOrSell": 1}
    OrderDetail_headers = {'login': ''}
    OrderDetail_res = HttpRequest().http_request(OrderDetail_url, 'post', data=OrderDetail_data,
                                                 headers=OrderDetail_headers,
                                                 cookies=buyer_login_res.cookies)
    print('获取买家订单序列号的结果是：', OrderDetail_res.json())
    qrCode = OrderDetail_res.json()['data']['qrCode']
    # print("买家订单序列号是：", qrCode)

    # 卖家确认序列号
    consume_url = 'http://m.test.hobay.com.cn/ribbon-api/orders/consume'
    buyerUserId = buyer_login_res.json()['userId']
    consume_data = {"orderId": orderId,
                    "payType": payType,
                    "buyerUserId": buyerUserId,
                    "qrCode": qrCode}
    consume_headers = {'login': '', 'payPassword': 'Y6QsYMqOfRI='}
    consume_res = HttpRequest().http_request(consume_url, 'post', data=consume_data, headers=consume_headers,
                                             cookies=seller_login_res.cookies)
    print('确认收货的结果是：', consume_res.json())


if __name__ == '__main__':
    bug_goods(17777777781, 17777777776, "普通焕商本地生活", 3)
