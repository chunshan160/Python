#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/29 11:34
# @Author :春衫
# @File :moni.py

from decimal import Decimal

a = Decimal('8')
b = Decimal('4.8')
c = Decimal('3.5')

time = 90
i=1
while time>0:
    print(f"第{i}轮")
    print("开始：", a, b, c)

    d = min(a, b, c)
    print("剩余CD", d)

    a = a - d
    b = b - d
    c = c - d
    time = time - d
    print("结束：", a, b, c)

    if a == Decimal('0'):
        print("触发A")
        a = Decimal('8')
    elif b == Decimal('0'):
        print("触发B")
        b = Decimal('4.8')
    elif c == Decimal('0'):
        print("触发C")
        c = Decimal('3.5')

    print("剩余时间", time)
    i=i+1
    print("--------------")
