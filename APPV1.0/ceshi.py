#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/8 20:32
# @Author :春衫
# @File :ceshi.py

import requests
class RequestHandler:
    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url, params=params, headers=headers)
            return result
        except Exception as e:
            print("get请求错误: %s" % e)

    def post(self, url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        try:
            result = requests.post(url, params=params, data=data, json=json)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)

    def run_main(self, method, **kwargs):
        """
        判断请求类型
        :param method: 请求接口类型
        :param kwargs: 选填参数
        :return: 接口返回内容
        """
        if method == 'get':
            result = self.get(**kwargs)
            return result
        elif method == 'post':
            result = self.post(**kwargs)
            return result
        else:
            print('请求接口类型错误')
if __name__ == '__main__':
    # 以下是测试代码
    # get请求接口
    url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'
    res = RequestHandler().get(url)
    # post请求接口
    url2 = 'http://127.0.0.1:8000/user/login/'
    payload = {
        "username": "vivi",
        "password": "123456"
    }
    res2 = RequestHandler().post(url2,json=payload)
    # print(res.json())
    print(res2)
