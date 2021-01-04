#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/14 16:26
# @Author :春衫
# @File :zy_07day.py


#描述器
class BoolFiled(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise ValueError

    def __delete__(self, instance):
        self.value = None

class Model:
    a=BoolFiled()

m=Model()
m.a=True

print(m.a)

"""
1. object.__getattr__ 方法
如果被访问(查找)属性不存在时会被触发

2.object.__getattrbute__ 方法
访问(查找)属性时，第一时间触发__getattribute__ 方法查找属性

3.object.__setattr__ 方法
设置属性时，触发__setattr__ 方法

4.object.__delattr__ 方法
在删除属性的时候会被触发
"""