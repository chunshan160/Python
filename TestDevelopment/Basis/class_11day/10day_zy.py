#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 14:42
# @Author :春衫
# @File :10day_zy.py

import threading
import time

import requests


count=0

class RequestsThread(threading.Thread):

    def run(self):
        global count
        for i in range(100):
            res = requests.post("http://httpbin.org/post")
            count+=1
            print("Thread-{}--第{}次请求".format(self.name, i + 1))


def main():
    s_time = time.time()
    # 创建10个线程对象
    th = [RequestsThread() for i in range(10)]
    # 遍历线程对象：开启线程
    for i in th:
        i.start()
    # 遍历线程对象：关闭线程
    for j in th:
        j.join()
    e_time = time.time()
    print("平均时间：{}".format((e_time - s_time) / count))

main()
