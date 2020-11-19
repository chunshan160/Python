#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/24 17:07
# @Author :春衫
# @File :ceshi.py

import grequests
import requests


# s=requests.Session()

login_url = 'http://m.mtest.hobay.com.cn/api/app/user/login'  # 登录
login_data = {"loginValidateType": "CODE", "phone": 17777777776, "validateValue": "666666"}
login_res = requests.post(login_url, json=login_data)
print("登录结果是：", login_res.json())


product_data={"ids":[173187],"storageId":"2393"}
url="http://m.mtest.hobay.com.cn/ribbon-api/product/submitToStorage"
# res = requests.post(url, json=product_data,headers={"login":""},cookies=login_res.cookies)
# print("上传已有商品的结果是：", res.json())



req_list = [grequests.post(url, json=product_data,headers={"login":""},cookies=login_res.cookies) for i in range(100)]
res_list = grequests.map(req_list)
print(res_list[0].text)


