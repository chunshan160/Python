#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 14:44
# @Author :春衫
# @File :class_12day_pre_01.py
import time
from multiprocessing import Process

# 多进程：不共享全局变量

a = 100


def work1():
    for i in range(10):
        global a
        print("这个是任务1-----{}".format(a))
        a += 1
        time.sleep(0.5)


def work2():
    for i in range(10):
        global a
        print("这个是任务2-----{}".format(a))
        a += 1
        time.sleep(0.5)


# 多进程执行多任务
# 创建两个进程

if __name__ == '__main__':
    # 进程执行时，不加__name__=="__main__"，就会无限递归，报错
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()
