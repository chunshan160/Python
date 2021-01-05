#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 14:16
# @Author :春衫
# @File :class_10day_global.py

import threading
import time

# 多线程使用全局变量不稳定，会出现资源竞争问题，导致数据结果不准确

# 全局变量
a = 100


def func1():
    global a
    for i in range(100000):
        # 100 并行并发，暂停，切换到任务二
        a += 1
    print("线程1修改完a：", a)


def func2():
    global a
    for i in range(100000):
        # 100 并行并发，暂停，又切换回任务一
        a += 1
    print("线程2修改完b：", a)


# 创建一个线程去执行 事情1
t1 = threading.Thread(target=func1)
# 创建一个线程去执行 事情2
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)
