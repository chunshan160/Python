#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/9 14:07
# @Author :春衫
# @File :class_07_01.py

# 自定义属性访问

class Test:

    def __init__(self):
        self.age = 18

    # def __getattr__(self, item):
    #     # 当访问属性的时候，如果属性不存在（出现attrError时），该方法会被触发
    #     print("---这个是getattr---")
    #     # object.__getattribute__(self,item)
    #     return 100
    #
    # def __getattribute__(self, item):
    #     # 当访问属性的时候，第一时间触发该方法去找属性
    #     print("---这个是getattribute---")
    #     # return 999
    #     return super().__getattribute__(item)

    # def __setattr__(self, key, value):
    #     # 这个方法在给对象设置属性的时候触发
    #
    #     if key=="age":
    #         super().__setattr__(key,18)
    #     else:
    #         print("设置属性的时候会触发setattr方法")
    #         # print(key)  # name
    #         # print(value)  # 10
    #         super().__setattr__(key,value)

    def __delattr__(self, item):
        # 这个方法在删除属性的时候会触发
        # print(item)
        if item == "name":
            pass
        else:
            print("__delattr__被调用")
            super().__delattr__(item)


t = Test()
t.name = 10
t.age = 9999

del t.name

print(t.name)
# print(t.age)
# print(t.name1)  # 默认None
# print(t.name2)


