#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py


import requests


# from tools.my_log import MyLog

# my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request(url, data, http_method, **kwargs):
        global res
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, data, **kwargs)
            elif http_method.lower() == 'post':
                res = requests.post(url, json=data, **kwargs)
            else:
                print("输入的请求方式不对")
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    # 登录
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": "13724765586", "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, login_data, "post")
    print("登录结果是：", login_res.json())
    print(login_res.cookies)

    # 确认订单
    url = "http://m.test.hobay.com.cn/ribbon-api/batchCart/immediatelyBuySettlement"
    data = {"productStockIdAndNums": [{"num": 1, "productStockId": 362028, "productId": "1079744"}]}
    headers={Host: m.test.hobay.com.cn
Connection: keep-alive
Content-Length: 83
Accept: */*
login: 46e0ea66ba01000
payPassword:
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
versionKey: 2.5.7
Content-Type: application/json
Origin: http://m.test.hobay.com.cn
Referer: http://m.test.hobay.com.cn/vuespa/index.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8
Cookie: pgv_pvid=3801153360; Hm_lvt_27de5d535c910bfba35a45d9868f2eb1=1595211506,1595297161,1595555347,1595817298; __qc_wId=111; Hm_lpvt_27de5d535c910bfba35a45d9868f2eb1=1595844946; login=46e0ea66ba01000}
    res = requests.post(url, json=data, cookies=login_res.cookies)
    print("确认订单的结果是：", res.json())

    # # 提交订单
    # SaveOrder_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/immediatelySaveOrder'
    # SaveOrder_data = {"message": "", "couponUserId": "", "addressId": "",
    #                   "productStockIdAndNums": [{"num": 1, "productStockId": 362028}], "type": 3}
    # headers = {"Content-Type": "application/json"}
    # SaveOrder_res = HttpRequest().http_request(SaveOrder_url, SaveOrder_data, "post", cookies=login_res.cookies,
    #                                            headers=headers)
    # print("提交订单结果是：", SaveOrder_res.json())
