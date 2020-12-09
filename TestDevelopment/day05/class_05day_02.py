#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 16:22
# @Author :春衫
# @File :class_05day_02.py


# class MyClass(object):
#     def __init__(self, name):
#         self.name = name
#         print("__init__方法调用了")
#
#     def __new__(cls, *args, **kwargs):
#         print("这个是new方法")
#         # return super().__new__(cls)
#         return object.__new__(cls)
#
#
# m = MyClass("ceshi")
# print(m)  # 不return就是None
# print(m.name)


# __new__方法在__init__之前原型 来自object类  是静态方法


# 单例模式
class MyTest(object):
    __isinstance = None  # 设置一个类属性来记录这个类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:  # 初始None=False 不是False时 就是为真 if True 进下一级
            cls.__isinstance = object.__new__(cls)
            return cls.__isinstance
        else:
            return cls.__isinstance


# 装饰器实现单例模式


t1 = MyTest()
t1.name = "chunshan"

t2 = MyTest()
print(t2.name)

print(id(t1))
print(id(t2))

t2.age = 18
print(t1.age)
