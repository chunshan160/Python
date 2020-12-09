#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/19 15:27
# @Author :春衫
# @File :第15节_魔术方法.py

'''
python进阶（三)∶面向对象之魔术方法
一、魔术方法（魔法方法、特殊方法)
·问题一:_init___有什么作用?
    ·在创建对象的时候，自动调用对创建的对象进行初始化设置的，
·问题二:什么是魔术方法?
    ·在python中像_init_这类双下划线开头和结尾的方法，我们把它统称为魔术方法。

·注意点:
·魔术方法都是python内部定义的，自己不要去定义__init__这中双下划线先开头的方珐

·问题三:创建一个对象的时候，调用的第一个方法是什么?
'''


# class MyClass(object):
#     def __init__(self, name):
#         self.name = name
#
#
# m = MyClass('ceshi')
# print(m.name)

'''
1、_new__方法
问题:那么这个_new_方法呢，它有什么作用?又在什么时候会调用呢?
·小案例
'''


class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('------这个是new方法-------')
        return super().__new__(cls)

m = MyClass('ceshi')
print(m.name)