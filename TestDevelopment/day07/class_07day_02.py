#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/9 14:42
# @Author :春衫
# @File :class_07day_02.py


# 描述器
class Filed(object):
    """
    一个类中，只要出现以下三个方法中的任何一个，该类就被称为描述器
    """

    def __get__(self, instance, owner):
        print("访问属性的时候被触发")
        # print(instance)
        # print(owner)
        return self.value

    def __set__(self, instance, value):
        # print(self)  # 类对象 attr
        # print(instance)  # 类对象 m
        # print(value) # 值
        print("修改属性的时候触发了__set__方法")
        self.value = value

    def __delete__(self, instance):
        print("删除属性值的时候会被触发")
        # del self.value
        self.value = None


class Mode(object):
    name = "ceshi"
    attr = Filed()  # 描述器对象：会覆盖类属性的相关操作


m = Mode()

# m.name = "lala"
# print(m.name)

m.attr = 1000
del m.attr
print(m.attr)
