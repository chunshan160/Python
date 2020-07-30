#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/3/23 13:58
# @Author :春衫
# @File :http_request.py

import requests


# # get请求  def get (url，params=None，**kwargs) :      **kwargs 关键字参数
#
# url = 'http://m.test.hobay.com.cn/search-feign/product/no_getProductRecommend?currentPage=1&pageSize=20&city=广州'
# res = requests.get(url, cookies=None)  # 返回一个消息实体  响应头响应体
# print(res)
#
# # 响应头 响应状态码 响应报文/正文
# print("响应头：", res.headers)
# print("响应状态码：", res.status_code)
# print("响应正文：", res.text)  # 格式json
#
# # post 请求  带参数
# url = 'http://m.test.hobay.com.cn/search-feign/product/no_getProductRecommend'
# data = {"currentPage": "1", "pageSize": "20", "city": "广州"}
# res = requests.post(url, data)
# print("响应头：", res.headers)
# print("响应状态码：", res.status_code)
# print("响应正文：", res.text, type(res.text))  # 格式json  <class 'str'>
# print(" **cookies**:", res.cookies)#类字典形式  key取值
# print("响应正文2：", res.json(), type(res.json()))  # 格式json  <class 'dict'>   推荐用这种，方便取值key

# #html xml json-- 》text
# html xml -->json()会报错! 只有json类型的返回值才支持json



#先登录
login_url = 'http://m.test.hobay.com.cn/api/app/user/login'
login_data = {"loginValidateType": "PASSWORD", "phone": "77777777777", "validateValue": "qaz123"}
# headers没用的，只要设置json=传值就好了
# headers = {
           # "Accept": "application/json, text/plain, */*",
           # "Accept-Encoding": "gzip, deflate",
           # "Connection": "keep-alive",
           # "Content-Type": "application/json",
           # "charset": "UTF-8",
           # "User-Agent": ": Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
           # "Referer": "http://m.test.hobay.com.cn/vuespa/index.html"}
res = requests.post(login_url, json=login_data)
print("请求头：", res.request.headers)
# print("Content-Type:",res.headers["Content-Type"])
print("响应正文：", res.json())
print(" **cookies**:", res.cookies["login"])  # 类字典形式  key取值
# cookies=res.cookies["login"]
# cookies_2=("login="+str(cookies))
# print(cookies_2)

#焕焕商超
sc_url='http://m.test.hobay.com.cn/ribbon-api/storage/queryOwnerStorage?page=1&pageSize=10'
res_sc=requests.get(sc_url,cookies=res.cookies)
print("响应正文：", res.json())

# 请求头：res.leaen_request.headers
# 响应头：res.headers
# 响应正文：res.json()

# # 注册
# register_url = 'http://8.129.65.165:8080/futureloan/mvc/api//member/register'
# data = {"mobilephone": "13724765586", "pwd": "123456", "regname": "chunshan"}
# res = requests.post(register_url, data)
# print(res.json())


# # 充值
# recharge_url = "http://8.129.65.165:8080/futureloan/mvc/api/member/recharge"
# recharge_data = {"mobilephone": "13724765586", "amount": "1000"}
# recharge_res = requests.get(recharge_url, recharge_data, headers={}, cookies=res.cookies)
# print("充值结果:", recharge_res.json())
# print("状态码:", recharge_res.status_code)
# print("代理user-agent", res.leaen_request.headers)

#
class HttpRequest:
    # 利用requests封装get请求和post请求
    def http_request(self, url, data, method, cookie=None):
        # url:请求的地址http://AXXX:port
        # param:传递的参数  非必填参数  字典的格式传递参数
        # method: 请求方式。支持get以及post
        # cookie:请求的时候传递的cookie值
        if method.lower() == 'get':  # lower()都小写
            res = requests.get(url, data, cookies=cookie)
        else:
            res = requests.post(url, data, cookies=cookie)
        return res  # 返回消息实体


if __name__ == '__main__':
    # 登录
    url = 'http://8.129.65.165:8080/futureloan/mvc/api/member/login'
    data = {"mobilephone": "13724765586", "pwd": "123456"}
    res = HttpRequest().http_request(url, data, 'post')
    print("登录结果是：", res.json())

    # 充值
    recharge_url = "http://8.129.65.165:8080/futureloan/mvc/api/member/recharge"
    recharge_data = {"mobilephone": "13724765586", "amount": "1000"}
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, 'get', res.cookies, )
    print("充值结果是：", recharge_res.json())

# 1:我想要有post请求怎么办?
# 接口是否发送get还是post请求这个是写代码的时候定义功能的时候就已经确定了的
# 2:并不是所有的请求都支持get和post根据接口 文档来看
# 3:为什么有些接口抓不到?接口地址参数你未必都可以抓到数据会加密根本抓不到
