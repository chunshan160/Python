#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/9 15:18
# @Author :春衫
# @File :class_07_03.py

from django.db import models

models.CharField()

"""
ORM模型介绍
O(objects)：类和对象。
R(Relation)：关系，关系数据库中的表格。
M(Mapping)：映射。|

ORM框架的功能:
建立模型类和表之间的对应关系，允许我们通过面向对象的方式来操作数据库。
根据设计的模型类生成数据库中的表格。
通过方便的配置就可以进行数据库的切换。


数据库的字段类型
mysq|常用数据类型:
整数: int, bit
小数: decimal (decimal表示浮点数, 如decimal(5,2)表示共存5位数，小数占2位)
字符串: varchar,char (char不可变长度，varchar可变长度)
日期时间: date, time, datetime
枚举类型(enum)


ORM模型中对应的字段(下面为diango的ORM模型中选取的几个字段)
类型              描述
BooleanField：布尔字段，值为True或False。
CharField(max_lengjh=最大长度)：字符串。参数max_length表示最大字符个数。
IntegerField：整数。

"""


class CharFiled:

    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError("字符串长度在{}以内".format(self.max_lenght))
        else:
            raise TypeError("need a str")

    def __delete__(self, instance):
        self.value = None


class IntFiled:

    # def __init__(self, max_lenght=20):
    #     self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("need a int")

    def __delete__(self, instance):
        self.value = None


class UserModel(object):
    # 假设这个是模型类
    name = CharFiled(max_lenght=5)  # 只能赋值成str
    pwd = CharFiled(max_lenght=10)  # 只能赋值成str
    age = IntFiled()  # 只能赋值成int


m = UserModel()

m.name = "ceshi"
m.pwd = "qaz123"
m.age = 18
print(m.name)
print(m.pwd)
print(m.age)
