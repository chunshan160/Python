#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/7 14:50
# @Author :春衫
# @File :zy_05day.py

# 第一题：通过装饰器实现单利模式，只要任意一个类使用该装饰器那么就会变成一个单例模式的类。

# 单例模式装饰器  控制对象创建次数
def single(func):
    instance = {}

    def fun(*args, **kwargs):
        if func not in instance:
            # 字典[函数(key)]:创建的对象(value)
            # {<class '__main__.Test'>: <__main__.Test object at 0x000001E5E8492E80>}
            instance[func] = func(*args, **kwargs)
            return instance[func]
        else:
            return instance[func]

    return fun


@single
class Test:
    pass


# t1 = Test()
# t2=Test()
# print(t1)
# print(t2)

# 第二题：通过类实现一个通用的装饰器，既可以装饰函数，也可以装饰器类，既可以装饰器有参数的，又可以装饰器无参数的
class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("-----这个是装饰器里面的功能-----")
        self.func()
        print("-----装饰器-----功能2-----")


@Decorator
def test_01():
    print("-----原来的功能函数-----")


test_01()

# 第三题：请描述__new__、__str__、__repr__、__call__分别在什么情况下会被触发
"""
__new__：创建实例对象的时候被调用
__str__：print()、str()、format()
__repr__：没有str方法就会触发repr方法
__call__：对象被调用时就会触发
"""