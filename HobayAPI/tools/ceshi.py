#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/13 10:51
# @Author :春衫
# @File :ceshi.py
from http_request import HttpRequest


def input_user(login_phone, input_phone):
    # 登录
    global login_type
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": login_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 录入客户
    input_data = {"area": "", "city": "", "company": "大", "detailedAddress": "",
                  "headImage": "/group1/M00/07/AC/wKgAZV8zdWaAFK94AARVJeKqSr452!1280x959.jpeg", "name": "测试",
                  "partnerStatus": 0, "phone": input_phone, "position": "", "province": ""}
    input_url = "http://m.test.hobay.com.cn/ribbon-api/customer/saveCustomer"
    headers = {"login": ""}
    input_res = HttpRequest().http_request(input_url, "post", json=input_data, cookies=login_res.cookies,
                                           headers=headers, )
    print("录入客户的结果是：", input_res.json())


#正式个人焕商
#代理商小号
#非正式焕商
input_phone=17777777998
#区域焕商
# input_user_id =1001363
for login_phone in [17777777952,17777777953,22222222222,17777777950,17777777772]:
    input_user(login_phone, input_phone)