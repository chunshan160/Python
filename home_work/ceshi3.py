#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/20 17:16
# @Author :春衫
# @File :ceshi3.py


import requests

login_url = f'http://boss.test.hobay.com.cn/bosszuul/boss/user/login'  # 登录
login_data = {"phone": 17777777781, "password": "qaz123"}
login_res = requests.post(login_url, data=login_data)
# print(f"BOSS登录结果是：{login_res.json()}")

# url="http://boss.test.hobay.com.cn/bosszuul/activiti/productStorageAudit/queryProductStorage"
# data={"page":1,"pageSize":100,"isRestrictions":"ALL"}
# res=requests.post(url,json=data,cookies=login_res.cookies,headers={"login":""})
# # print(f"商品{res.json()}")
#
# product=res.json()['result']
#
# for i in range(len(product)):
#     product_id=product[i]['taskId']
#     print(product_id)
#     print("===========")
#     url2="http://boss.test.hobay.com.cn/bosszuul/activiti/productStorageAudit/fail"
#     data2={"taskId":product_id}
#     res2=requests.post(url2,json=data2,cookies=login_res.cookies)
#     print(res2.status_code)


url3="http://boss.test.hobay.com.cn/bosszuul/product/operateProduct/queryPageProductsByType"
data3={"currentPage":1,"pageSize":100,"type":1,"sort":"","categoryId":"","createTimeBegin":"","createTimeEnd":"","firstCategoryId":"","name":"实物推荐0库存","parentCategoryId":"","productType":"","qtyNuMEnd":"","qtyNumBegin":"","status":""}
res3=requests.post(url3,json=data3,cookies=login_res.cookies,headers={"login":""})
# print(f"商品{res3.json()}")

product=res3.json()['result']

for i in range(len(product)):
    product_id=product[i]['id']
    print(product_id)
    print("===========")
    url4=f"http://boss.test.hobay.com.cn/bosszuul/product/operateProduct/cancelCheckProudct?productId={product_id}"
    res4=requests.get(url4,cookies=login_res.cookies)
    print(res4.status_code)