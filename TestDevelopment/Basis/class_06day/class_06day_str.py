#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/7 16:11
# @Author :春衫
# @File :class_06day_str.py

class MyStr(object):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        return self.data + other.data

    def __sub__(self, other):
        # 替换为""，相当于去掉
        return self.data.replace(other.data, "")


s1 = MyStr("sss111")
s2 = MyStr("sss222")

# s1触发，后面的当参数传进去
# s1+s2=s1._add(s2)
s3 = MyStr(s1 + s2)
print(s3)
print(s3 - s2)
