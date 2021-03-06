#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py

import requests


class HttpRequest:

    @staticmethod
    def http_request(url, http_method, **kwargs):
        global res
        msg = url.split("/")[-1]
        try:
            if http_method.lower() == 'get':
                res = requests.get(url, **kwargs)
            elif http_method.lower() == 'post':
                res = requests.post(url, **kwargs)
            else:
                print("输入的请求方式不对")

            if res.status_code == 200:
                print(f"{msg}接口请求成功")
            else:
                print(f"{msg}接口请求异常，异常的原因是：{res.json()}")

        except Exception as e:
            print(f"{msg}接口请求失败，失败的原因是：{e}")
            raise e
        return res


if __name__ == '__main__':
    pass
