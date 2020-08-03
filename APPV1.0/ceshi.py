#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/25 12:52
#@Author :春衫
#@File :ceshi.py
import datetime
import time

t1=time.time()
time.sleep(5)
t2=time.time()

print("相差",(datetime.datetime.fromtimestamp(t2)-datetime.datetime.fromtimestamp(t1)).seconds,"秒")
