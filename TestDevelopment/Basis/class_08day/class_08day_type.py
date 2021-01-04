#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/14 16:38
# @Author :春衫
# @File :class_08day_type.py


# 元类

# Python中内置的元类 type

# 空元祖 () 元祖中只有一个元素时需要加逗号 (obj,)

def func(self):
    print("----这个是self----")


# 利用元类直接创建类
# type创建类需要三个参数
# 第一个：类名 -->str
# 第二个：继承的父类 -->tuple
# 第三个：方法和属性 -->字典 键值对的形式表示属性 或者对应的方法
Test = type("Test", (object,), {"attr": 100, "__attr2": 200, "function01": func})

print(Test)  # <class '__main__.Test'>

# t = Test()
# t.function01()
#
# print(Test.__bases__)

# class Test1(object):
#     attr = 100
#     __attr2 = 200
#
# print(Test1)  # <class '__main__.Test1'>
