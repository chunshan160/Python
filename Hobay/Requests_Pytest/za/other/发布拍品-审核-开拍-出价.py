#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:17
# @Author :春衫
# @File :发布拍品-审核-开拍-出价.py

from get_time import getTime
from http_request import HttpRequest


def auction(buyer_phone, seller_phone, start_time, end_time, payPassword, goods_name="发布拍品用"):
    # 卖家登录
    seller_login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    seller_login_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    seller_login_res = HttpRequest().http_request(seller_login_url, "post", json=seller_login_data)
    print("登录结果是：", seller_login_res.json())

    # 发布拍品
    SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/publishAuction'
    SaveOrder_data = {"productImg": ["/group1/M00/07/B8/wKgAZl8fhxaASFpSAAF7g0bXYPA38!546x546.jpeg"],
                      "name": goods_name,
                      "price": 1, "securityPayment": 1, "scope": 1, "normalPrice": "", "categoryId": 101,
                      "categoryName": "电视", "description": "111", "imgList": [], "firstCategory": 1}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data,
                                               cookies=seller_login_res.cookies,
                                               headers=SaveOrder_headers)
    print("发布拍品结果是：", SaveOrder_res.json())

    # operate登录
    operate_url = 'http://operate.test.hobay.com.cn/adminuser/userLogin'  # 登录
    operate_data = {
        "__RequestVerificationToken": "fkfh8D89BFqTdrE2iiSdG_L781RSRtdWOH411poVUWhxzA5MzI8es07g6KPYQh9Log-xf84pIR2RIAEkOokZL3Ee3UKmX0Jc8bW8jOdhqo81",
        "username": "admin", "password": 123, "rememberMe": "true"}
    operate_res = HttpRequest().http_request(operate_url, "post", data=operate_data)
    print("operate登录结果是：", operate_res.json())

    # 审核拍品
    data_id = SaveOrder_res.json()['data']
    preBeginTime = getTime(start_time)
    preEndTime = getTime(end_time)
    url = 'http://operate.test.hobay.com.cn/auctionolproduct/passCheckNew'  # 登录
    data = {"id": data_id, "saleablePhones": [""], "applyNum": "0", "preBeginTime": preBeginTime,
            "preEndTime": preEndTime, "browserBaseNum": "0", "remindNum": "0", "categoryName": "电视",
            "description": "111", "name": goods_name, "normalPrice": "0.00", "price": "1.00", "saleablePhone": "",
            "unsaleable": "-1", "scope": "1.00", "securityPayment": "1.00", "firstCategory": "1", "categoryId": "101",
            "checkNote": "", "images": ["/group1/M00/07/A5/wKgAZV8sxDuAbS2cAAD-_goQPAc283!512x150.png"],
            "detailImages": []}
    res = HttpRequest().http_request(url, "post", json=data, cookies=operate_res.cookies)
    print("审核拍品的结果是：", res.json())

    # 卖家设置开拍时间
    signed_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/starAuction"
    data = {"starTime": preBeginTime + 10000, "endTime": preEndTime - 60000, "auctionProductId": data_id}
    headers = {"login": ""}
    signed_res = HttpRequest().http_request(signed_url, "post", data=data, cookies=seller_login_res.cookies,
                                            headers=headers)
    print("卖家设置开拍时间的结果是：", signed_res.json())

    # 参与者登录
    buyer_login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    buyer_login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    buyer_login_res = HttpRequest().http_request(buyer_login_url, "post", json=buyer_login_data)
    print("参与者登录结果是：", buyer_login_res.json())

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
    addressId = address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
    SaveOrder_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlProduct/enrollAndPay"
    SaveOrder_data = {"auctionOlProductId": data_id, "receivingAddressId": addressId}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", data=SaveOrder_data,
                                               cookies=buyer_login_res.cookies,
                                               headers=SaveOrder_headers)
    print("提交订单结果是：", SaveOrder_res.json())

    # 报名支付
    sign_up_order = SaveOrder_res.json()['data']['tradeNum']
    sign_up_pay_url = "http://m.test.hobay.com.cn/ribbon-api/pay/payCash"
    sign_up_pay_data = {"tradeNum": sign_up_order}
    sign_up_pay_headers = {"login": "", "payPassword": payPassword}
    sign_up_pay_res = HttpRequest().http_request(sign_up_pay_url, "post", data=sign_up_pay_data,
                                                 cookies=buyer_login_res.cookies,
                                                 headers=sign_up_pay_headers)
    print("支付订单的结果是：", sign_up_pay_res.json())

    # 出价
    chujia_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/bidPrice"
    chujia_data = {"bidPrice": 2, "auctionOlProductId": data_id}
    chujia_headers = {"login": ""}
    chujia_res = HttpRequest().http_request(chujia_url, "post", data=chujia_data, cookies=buyer_login_res.cookies,
                                            headers=chujia_headers)
    print("出价的结果是：", chujia_res.json())

    # 发起者立即成交
    click_url = f"http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/no_get5AuctionOlBids?auctionOlProductId={data_id}"
    click_headers = {"login": ""}
    click_res = HttpRequest().http_request(click_url, "get", cookies=seller_login_res.cookies,
                                           headers=click_headers)
    print("点击立即成交的结果是：", click_res.json())

    auctionOlBidId = click_res.json()["data"][0]["id"]
    liji_url = f"http://m.test.hobay.com.cn/ribbon-api/orders/saveOrderForAuction?auctionOlBidId={auctionOlBidId}"
    liji_headers = {"login": ""}
    liji_res = HttpRequest().http_request(liji_url, "get", cookies=seller_login_res.cookies,
                                          headers=liji_headers)
    print("立即成交的结果是：", liji_res.json())

    # 得拍者拍品支付
    pay_order = liji_res.json()['data']['tradeNum']
    pay_order_url = "http://m.test.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
    pay_order_data = {"tradeNUm": pay_order, "payType": 3, "shareWalletUserId": "", "shareWalletId": ""}
    pay_order_headers = {"login": "", "payPassword": payPassword}
    pay_order_res = HttpRequest().http_request(pay_order_url, "post", json=pay_order_data,
                                               cookies=buyer_login_res.cookies,
                                               headers=pay_order_headers)
    print("得拍者支付订单的结果是：", pay_order_res.json())

    # 发起人立即发货
    fahuo_url = 'http://m.test.hobay.com.cn/orders/sendProduct'
    seller_userId = seller_login_res.json()['userId']
    fahou_data = {'orderId': data_id, 'payType': 3, 'buyerUserId': seller_userId, 'type': 1, 'logisticsCompany': '德邦物流',
                  'companyNum': 'debangwuliu', 'logisticsNum': '123456789'}
    fahuo_headers = {'login': ''}
    fahuo_res = HttpRequest().http_request(fahuo_url, 'post', data=fahou_data, headers=fahuo_headers,
                                           cookies=seller_login_res.cookies)
    print('卖家发货成功', fahuo_res.json())

    # 得拍者确认收货
    orderId=pay_order_res.json()["data"]["orderId"]
    buyer_url = 'http://m.test.hobay.com.cn/ribbon-api/orders/recieve'
    buyer_UserId = seller_login_res.json()['userId']
    buyer_data = {'orderId': orderId, 'payType': 3, 'sellerUserId': buyer_UserId}
    buyer_headers = {'login': '', 'payPassword': payPassword}
    buyer_res = HttpRequest().http_request(buyer_url, 'post', data=buyer_data, headers=buyer_headers,
                                           cookies=buyer_login_res.cookies)
    print("得拍者确认收货的结果是：", buyer_res)


if __name__ == '__main__':
    # auction(17777777781, 13724765586,goods_name="37发布拍品测绑定用")
    auction(17777777781, 13724765586, '2020-08-12 17:38:00', '2020-08-15 17:20:00', "qNlHQue5Y/U=",
            goods_name="86发布拍品测绑定用")
    # auction(17777777781, 17777777781, goods_name="81发布拍品测绑定用")
