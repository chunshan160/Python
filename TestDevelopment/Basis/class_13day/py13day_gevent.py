#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/30 16:45
# @Author :春衫
# @File :py13day_gevent.py
import queue
import time
import requests
import gevent
from gevent import monkey

"""
协程：gevent
协程存在于线程之中，线程默认不会等待协程执行

spawn：开启协程（第一个参数为协程要执行的参数）
join：让线程等待协程执行

协程之间切换的条件：gevent.sleep()

gevent的程序补丁：monkey.patch_all()
只要耗时就会切换协程

"""

monkey.patch_all()

q = queue.Queue()
for i in range(1000):
    q.put("http://127.0.0.1:5000")


# def work1():
#     for i in range(10):
#         print("---work1---{}".format(i))
#         # gevent.sleep(0.1)
#         # time.sleep(0.1)
#         requests.get("http://127.0.0.1:5000")
#
# def work2():
#     for i in range(10):
#         print("---work2---{}".format(i))
#         # gevent.sleep(0.1)
#         # time.sleep(0.1)
#         requests.get("http://127.0.0.1:5000")


def work():
    while q.qsize() > 0:
        url = q.get()
        requests.get(url)


# 创建两个协程

st = time.time()

g1 = gevent.spawn(work)
g2 = gevent.spawn(work)
g3 = gevent.spawn(work)
g4 = gevent.spawn(work)
g5 = gevent.spawn(work)
g6 = gevent.spawn(work)
g7 = gevent.spawn(work)


g1.join()
g2.join()
g3.join()
g4.join()
g5.join()
g6.join()
g7.join()


et = time.time()
print("耗时：{}".format(et - st))
