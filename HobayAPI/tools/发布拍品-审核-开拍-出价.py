#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/29 10:17
#@Author :春衫
#@File :发布拍品-审核-开拍-出价.py

import time
from tools.http_request import HttpRequest

def auction(buyer_phone, seller_phone,payPassword,goods_name="发布拍品用"):
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
    t = time.time()  # 原始时间数据
    data_time = int(round(t * 1000))  # 毫秒级时间戳
    preBeginTime = data_time
    preEndTime = data_time + 4000000
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
    preBeginTime = preBeginTime
    preEndTime = preEndTime - 10000
    print(preBeginTime, preEndTime)
    data = {"starTime": preBeginTime, "endTime": preEndTime, "auctionProductId": data_id}
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
    print("提交订单结果是：", SaveOrder_res.json())

    # 报名支付
    order = SaveOrder_res.json()['data']['tradeNum']
    pay_url = "http://m.test.hobay.com.cn/ribbon-api/pay/payCash"
    pay_data = {"tradeNum": order}
    pay_headers = {"login": "", "payPassword": payPassword}
    pay_res = HttpRequest().http_request(pay_url, "post", data=pay_data, cookies=login3_res.cookies,
                                         headers=pay_headers)
    print("支付订单的结果是：", pay_res.json())

    # 出价
    time.sleep(8)
    chujia_url = "http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/bidPrice"
    chujia_data = {"bidPrice": 2, "auctionOlProductId": data_id}
    chujia_headers = {"login": ""}
    chujia_res = HttpRequest().http_request(chujia_url, "post", data=chujia_data, cookies=login3_res.cookies,
                                            headers=chujia_headers)
    print("出价的结果是：", chujia_res.json())

if __name__ == '__main__':
    # auction(17777777781, 13724765586,goods_name="37发布拍品测绑定用")
    auction(13724765586, 17777777776,"qNlHQue5Y/U=", goods_name="76发布拍品测绑定用")
    # auction(17777777781, 17777777781, goods_name="81发布拍品测绑定用")