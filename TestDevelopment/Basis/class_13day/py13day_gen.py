#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/30 16:22
# @Author :春衫
# @File :py13day_gen.py


"""
#生成器
#生成器表达式
#在函数中使用yield这个关键字：生成器
"""

import time

def work1():
    for i in range(10):
        print("---work1---{}".format(i))
        time.sleep(0.1)
        yield


def work2():
    for i in range(10):
        print("---work2---{}".format(i))
        time.sleep(0.1)
        yield

# 通过生成器实现多任务
g1 = work1()
g2 = work2()

while True:
    try:
        next(g1)
        next(g2)
    except StopIteration:
        break

# 协程：微线程
"""
协程本质上是单任务
协程依赖于线程
协程相对于线程来讲占用的资源更少（几乎不要占用什么资源）
"""
