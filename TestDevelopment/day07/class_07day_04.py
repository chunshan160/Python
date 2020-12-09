#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/9 15:56
# @Author :春衫
# @File :class_07day_04.py

# Python2才区分旧/新式类

# 经典类/旧式类 继承：instance类型
class MyClass:
    pass


# 新式类 继承：object
class Test(object):
    pass


t = Test()
print(type(t))  # <class '__main__.Test'>
print(type(Test))  # <class 'type'>
print(type(type))  # <class 'type'>

# type Python中所有的类都是通过type来创建出来的 创建 元类
# object Python中所有类的顶级父类都是object 继承
