#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/28 11:48
# @Author :春衫
# @File :233.py

import requests


# from tools.my_log import MyLog

# my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request(url, http_method, **kwargs):
        global res
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, **kwargs)
            elif http_method.lower() == 'post':
                res = requests.post(url, **kwargs)
            else:
                print("输入的请求方式不对")
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    import requests


    # from tools.my_log import MyLog

    # my_logger = MyLog()

    class HttpRequest:

        @staticmethod
        def http_request(url, http_method, **kwargs):
            global res
            try:
                if http_method.lower() == 'get':
                    res = requests.get(url, **kwargs)
                elif http_method.lower() == 'post':
                    res = requests.post(url, **kwargs)
                else:
                    print("输入的请求方式不对")
            except Exception as e:
                print("请求报错了：{0}".format(e))
                raise e
            return res


    if __name__ == '__main__':
        # 登录
        login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
        login_data = {"loginValidateType": "CODE", "phone": "17777777781", "validateValue": "666666"}
        login_res = HttpRequest().http_request(login_url, "post", json=login_data)
        print("登录结果是：", login_res.json())

        # 获取收货地址
        address_url = "http://m.test.hobay.com.cn/api/user/graphql/flat"
        address_data = {
            "query": "query currentUser{\n        currentUser{\n          receiveAddress(page:1,pageSize:100){\n            numPerPage\n            pageNum\n            totalCount\n            totalPage\n            recordList{\n              id\n              name\n              provinceName\n              cityName\n              areaName\n              detailAddress\n              phone\n              default\n            }\n          }\n        }\n      }"}
        address_headers = {"login": ""}
        address_res = HttpRequest().http_request(address_url, 'post', json=address_data,
                                                      cookies=login_res.cookies,
                                                      headers=address_headers)
        print("获取收货地址的结果是：", address_res.json())

        # 提交订单
        addressId = address_res.json()['currentUser_receiveAddress_recordList'][0]['id']
        SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
        SaveOrder_data = {"message": "", "couponUserId": "", "addressId": addressId,
                          "productStockIdAndNums": [{"num": 1, "productStockId": 362014}], "type": 1}
        SaveOrder_headers = {"login": ""}
        SaveOrder_res = HttpRequest().http_request(SaveOrder_url, "post", json=SaveOrder_data,
                                                   cookies=login_res.cookies,
                                                   headers=SaveOrder_headers)
        print("提交订单结果是：", SaveOrder_res.json())

        #支付订单
        order = SaveOrder_res
        pay_url = "http://m.test.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
        pay_data = {"tradeNUm": order, "payType": 3, "shareWalletUserId": "", "shareWalletId": ""}
        pay_headers = {"login": "", "payPassword": "xqdt77d9tjE="}
        pay_res = HttpRequest().http_request(pay_url, "post", json=pay_data, cookies=login_res.cookies,
                                             headers=pay_headers)
        print("支付订单的结果是：", pay_res.json())

        # 卖家登录
        login2_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
        login2_data = {"loginValidateType": "CODE", "phone": "17777777776", "validateValue": "666666"}
        login2_res = HttpRequest().http_request(login2_url, "post", json=login2_data)
        print("登录结果是：", login2_res.json())

        # 确认订单
        orderId = SaveOrder_res.json()['data']['orderId']
        # AcceptOrder_url=f"http://m.test.hobay.com.cn/ribbon-api/orders/acceptOrder?orderId={orderId}"
        # AcceptOrder_headers = {"login": ""}
        # AcceptOrder_res = HttpRequest().http_request(AcceptOrder_url, "get",cookies=login2_res.cookies,headers=AcceptOrder_headers)
        # print("确认订单的结果是：", AcceptOrder_res.json())

        # # 签约
        # sellerUserId = login2_res.json()['userId']
        # signed_url = f"http://m.test.hobay.com.cn/ribbon-api/orders/signed"
        # data = {"orderId": orderId, "payType": 3, "sellerUserId": sellerUserId}
        # headers = {"login": "", "payPassword": "xqdt77d9tjE="}
        # signed_res = HttpRequest().http_request(signed_url, "post", data=data, cookies=login_res.cookies,
        #                                         headers=headers)
        # print("签约的结果是：", signed_res.json())
