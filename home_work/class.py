#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/6 12:45
# @Author :春衫
# @File :class.py

num="135"

num1=input("请输入数字：")

for i in range(len(num)):

    if num1[i] not in num:
        print("不在")
    elif list(num).index(num1[i]) != i:
        print("位置不对")
    else:
        print("对了")