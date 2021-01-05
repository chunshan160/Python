#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 14:16
# @Author :春衫
# @File :class_11day_bug.py

import threading
import time

# 多线程使用全局变量不稳定，会出现资源竞争问题，导致数据结果不准确

# 全局变量
a = 0


# 死锁
def func1():
    global a
    for i in range(1000000):
        meta_A.acquire()  # 上锁
        meta_B.acquire()  # 上锁
        print("-----1-----")
        a += 1
        meta_B.release()  # 释放锁
        meta_A.release()  # 释放锁
    print("线程1修改完a：", a)


def func2():
    global a
    for i in range(1000000):
        meta_B.acquire()  # 上锁
        meta_A.acquire()  # 上锁
        print("-----2-----")
        a += 1
        meta_A.release()  # 释放锁
        meta_B.release()  # 释放锁
    print("线程2修改完b：", a)


# 创建锁 互斥锁
meta_A = threading.Lock()
meta_B = threading.Lock()

s_time = time.time()
# 创建一个线程去执行 事情1
t1 = threading.Thread(target=func1)
# 创建一个线程去执行 事情2
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()

print(a)
e_time = time.time()
print("时间：{}".format(e_time - s_time))

"""
上锁前：
线程1修改完a： 1298123
线程2修改完b： 1360925
1360925
时间：0.25200581550598145

上锁后：
线程1修改完a： 1940514
线程2修改完b： 2000000
2000000
时间：2.1930019855499268
"""
