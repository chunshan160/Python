#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/13 10:51
# @Author :春衫
# @File :ceshi.py

import decimal

a=0.01
# a=Decimal.from_float(0.01)
a = decimal.Decimal('0.01')
print(a)
print(type(a))

print(type(a) == decimal.Decimal)
print(isinstance(a,decimal.Decimal))