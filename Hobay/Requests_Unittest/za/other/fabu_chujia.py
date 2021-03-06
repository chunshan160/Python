#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/29 10:17
#@Author :春衫
#@File :fabu_chujia.py

import time ,datetime
from http_request import HttpRequest
from get_time import getTime

def auction(buyer_phone, seller_phone,start_time,end_time,goods_name="7025发布自留拍品，立即成交，生成订单，支付，不完成交易，退保证金时间"):
    # 卖家登录
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 发布拍品
    SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/publishAuction'
    SaveOrder_data = {"productImg": ["/group1/M00/07/B8/wKgAZl8fhxaASFpSAAF7g0bXYPA38!546x546.jpeg"], "name": goods_name,
                      "price": 1, "securityPayment": 1, "scope": 1, "normalPrice": "", "categoryId": 101,
                      "categoryName": "电视", "description": "111", "imgList": [], "firstCategory": 1}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data, cookies=login_res.cookies,
                                               headers=SaveOrder_headers)
    print("发布拍品结果是：", SaveOrder_res.json())

    # operate登录
    login2_url = 'http://operate.test.hobay.com.cn/adminuser/userLogin'  # 登录
    login2_data = {
        "__RequestVerificationToken": "fkfh8D89BFqTdrE2iiSdG_L781RSRtdWOH411poVUWhxzA5MzI8es07g6KPYQh9Log-xf84pIR2RIAEkOokZL3Ee3UKmX0Jc8bW8jOdhqo81",
        "username": "admin", "password": 123, "rememberMe": "true"}
    login2_res = HttpRequest().http_request(login2_url, "post", data=login2_data)
    print("operate登录结果是：", login2_res.json())

    # 审核拍品
    data_id = SaveOrder_res.json()['data']
    preBeginTime = getTime(start_time)
    preEndTime = getTime(end_time)
    url = 'http://operate.test.hobay.com.cn/auctionolproduct/passCheckNew'  # 登录
    data = {"id": data_id, "applyNum": "0", "preBeginTime": preBeginTime, "preEndTime": preEndTime,
            "browserBaseNum": "0", "categoryName": "电视", "description": "111", "name": goods_name, "normalPrice": "0.00",
            "price": "1.00", "saleablePhone": "", "unsaleable": "-1", "scope": "1.00", "securityPayment": "1.00",
            "firstCategory": "1", "categoryId": "101", "checkNote": "",
            "images": ["/group1/M00/07/B8/wKgAZl8fhxaASFpSAAF7g0bXYPA38!546x546.jpeg"], "detailImages": []}
    res = HttpRequest().http_request(url, "post", json=data, cookies=login2_res.cookies)
    print("审核拍品的结果是：", res.json())

    # 卖家设置开拍时间
    signed_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/starAuction"
    data = {"starTime": preBeginTime+60000, "endTime": preEndTime-60000, "auctionProductId": data_id}
    headers = {"login": ""}
    signed_res = HttpRequest().http_request(signed_url, "post", data=data, cookies=login_res.cookies,
                                            headers=headers)
    print("卖家设置开拍时间的结果是：", signed_res.json())

    # 参与者登录
    login3_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login3_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    login3_res = HttpRequest().http_request(login3_url, "post", json=login3_data)
    print("参与者登录结果是：", login3_res.json())

    # 获取收货地址
    address_url = "http://m.test.hobay.com.cn/api/user/graphql/flat"
    address_data = {
        "query": "query currentUser{\n        currentUser{\n          receiveAddress(page:1,pageSize:100){\n            numPerPage\n            pageNum\n            totalCount\n            totalPage\n            recordList{\n              id\n              name\n              provinceName\n              cityName\n              areaName\n              detailAddress\n              phone\n              default\n            }\n          }\n        }\n      }"}
    address_headers = {"login": ""}
    address_res = HttpRequest().http_request(address_url, 'post', json=address_data,
                                             cookies=login3_res.cookies,
                                             headers=address_headers)
    print("获取收货地址的结果是：", address_res.json())

    # 提交订单
    addressId = address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
    SaveOrder_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlProduct/enrollAndPay"
    SaveOrder_data = {"auctionOlProductId": data_id, "receivingAddressId": addressId}
    SaveOrder_headers = {"login": ""}
    SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", data=SaveOrder_data,
                                               cookies=login3_res.cookies,
                                               headers=SaveOrder_headers)
    print("报名提交订单结果是：", SaveOrder_res.json())

    # 报名支付
    order = SaveOrder_res.json()['data']['tradeNum']
    pay_url = "http://m.test.hobay.com.cn/ribbon-api/pay/payCash"
    pay_data = {"tradeNum": order}
    pay_headers = {"login": "", "payPassword": "Y6QsYMqOfRI="}
    pay_res = HttpRequest().http_request(pay_url, "post", data=pay_data, cookies=login3_res.cookies,
                                         headers=pay_headers)
    print("报名支付订单的结果是：", pay_res.json())

    # 出价
    time.sleep(5)
    chujia_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/bidPrice"
    chujia_data = {"bidPrice": 2, "auctionOlProductId": data_id}
    chujia_headers = {"login": ""}
    chujia_res = HttpRequest().http_request(chujia_url, "post", data=chujia_data, cookies=login3_res.cookies,
                                            headers=chujia_headers)
    print("出价的结果是：", chujia_res.json())

    # 出价排行接口
    paihang_url = 'http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/no_get5AuctionOlBids'
    paihang_data = {'auctionOlProductId': data_id}
    paihang_headers = {'login': ''}
    paihang_res = HttpRequest().http_request(paihang_url, "get", params=paihang_data, headers=paihang_headers,
                                             cookies=login3_res.cookies)
    print("出价排行榜", paihang_res.json())




if __name__ == '__main__':
    auction(12000000074, 13570258645,'2020-08-10 17:56:00','2020-08-11 17:20:00')

