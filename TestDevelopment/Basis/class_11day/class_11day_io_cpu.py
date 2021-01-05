#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 14:16
# @Author :春衫
# @File :class_11day_io_cpu.py

import threading
import time

# 全局变量
a = 0


def func1():
    global a
    for i in range(10000000):
        # print("-----1-----")
        a += 1
    # print("线程1修改完a：", a)


def func2():
    global a
    for i in range(10000000):
        # print("-----2-----")
        a += 1
    # print("线程2修改完b：", a)


def func3():
    global a
    for i in range(10000000):
        # print("-----2-----")
        a += 1
    # print("线程3修改完b：", a)


def func4():
    global a
    for i in range(10000000):
        # print("-----2-----")
        a += 1
    # print("线程4修改完b：", a)


# cpu密集型：多线程相加 200000000
# 单线程一般比多线程快，因为多线程需要不停切换
# -----------------------------
s_time = time.time()
# 创建一个线程去执行 事情1
t1 = threading.Thread(target=func1)
# 创建一个线程去执行 事情2
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()

# 单线程
# func1()
# func2()

# 网络io密集型
# 多线程比单线程快
func3()
func4()

e_time = time.time()
print("时间：{}".format(e_time - s_time))
