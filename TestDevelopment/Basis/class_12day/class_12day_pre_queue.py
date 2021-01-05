# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 15:06
# @Author :春衫
# @File :class_12day_pre_queue.py

import requests
from multiprocessing import Process, Queue

a = 1


# 多进程之间的通讯问题

def work1(q):
    while q.qsize() > 0:
        global a
        # 判断队列中是否有数据
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print("work1正在执行任务-----{}".format(a))
        a += 1


def work2(q):
    while q.qsize() > 0:
        global a
        # 判断队列中是否有数据
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print("work2正在执行任务-----{}".format(a))
        a += 1


if __name__ == '__main__':
    # 进程执行时，不加__name__=="__main__"，就会无限递归，报错
    # 创建一个队列，添加10个任务
    q = Queue()

    for i in range(10):
        q.put("http://127.0.0.1:5000")

    # 把队列传给进程
    p1 = Process(target=work1, args=(q,))
    p2 = Process(target=work2, args=(q,))

    p1.start()
    p2.start()
