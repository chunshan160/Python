#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 14:00
# @Author :春衫
# @File :class_10day_threa.py

import threading
import time

import requests


#通过继承Thread类来创建线程

class RequestsThread(threading.Thread):
    """发送requests请求"""

    def __init__(self,url):
        self.url=url
        super().__init__()

    def run(self):
        for i in range(10):
            res=requests.get(self.url)
            print("线程：{}--返回的状态码:{}--".format(threading.current_thread(),res.status_code))

#创建五个线程，发起请求
s_time=time.time()
for i in range(5):
    t=RequestsThread("http://www.baidu.com")
    t.start()

t.join()
e_time = time.time()
print("耗时：",e_time-s_time)