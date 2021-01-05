#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/30 16:37
# @Author :春衫
# @File :py13day_gree.py

import time
import greenlet


def work1():
    for i in range(10):
        print("---work1---{}".format(i))
        g2.switch()
        time.sleep(0.1)


def work2():
    for i in range(10):
        print("---work2---{}".format(i))
        g1.switch()
        time.sleep(0.1)

g1=greenlet.greenlet(work1)
g2=greenlet.greenlet(work2)

g1.switch()