#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/8 14:06
# @Author :春衫
# @File :class_06day_slots.py

# __slots__
# 限制对象的属性

class Base(object):
    # 指定类对象所能绑定的属性
    # 限制属性
    # 节约内存：定义了slots属性之后，那么该对象不会再自动生成__dict__属性
    __slots__ = ["name","age"]

    def __init__(self, name, age):
        self.name = name
        # self.age = age  # AttributeError: 'Base' object has no attribute 'age'


b = Base("ceshi", 18)

# b.age = 200  # AttributeError: 'Base' object has no attribute 'age'
b.name = "ceshi"

# print(b.__dict__)
