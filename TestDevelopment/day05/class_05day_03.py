#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 17:09
# @Author :春衫
# @File :class_05day_03.py


# 重写__str__和__repr__方法时，必须要记得写return
# 重写__str__和__repr__方法时，return返回的必须是一个字符串对象

class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("----str触发了----")
        # print("重写str")  # TypeError: __str__ returned non-string (type NoneType)
        # return [1, 2, 3]  # TypeError: __str__ returned non-string (type list)
        # return "重写str"
        return self.name

    def __repr__(self):
        print("----repr触发了----")
        print("重写repr")
        return "<MyClass.object-{}>".format(self.name)

    def __call__(self, *args, **kwargs):
        #对象像函数一样被调用时触发（加()）
        print("__call__")


m = MyClass("ceshi")


# 没有str方法就会触发repr方法 备胎
# print(m)
# str(m)
# format(m)

# a = repr(m)
# print(a)

#通过类来实现装饰器  __call__




def fun():
    print("---------")


a = "100"
fun()
m()
# a()  # TypeError: 'str' object is not callable
