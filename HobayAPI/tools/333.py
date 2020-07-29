#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/13 11:32
# @Author :春衫
# @File :http_request.py

import time
import requests


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
    pass
