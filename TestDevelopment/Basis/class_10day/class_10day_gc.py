#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/24 10:24
# @Author :春衫
# @File :class_10day_gc.py

import gc

res = gc.get_threshold()
print(res)
# (700, 10, 10) 第一代链表达到700个变量时，清理一次，剩下的移到第二代链表
# 第一代链表清理十次之后，清理第二代链表，以此类推
# 最多三代链表，幸存的一直存在三代链表里面
