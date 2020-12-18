#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/16 13:42
# @Author :春衫
# @File :class_08day_metaclass.py


# 自定义元类

# 自定义元类必须继承type
# type创建类：三个参数


class MyMetaClass(type):
    """自定义的元类,将类的所有属性名变大写"""

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print("最基础的自定义元类")
        for k, v in list(attr_dict.items()):
            attr_dict.pop(k)
            attr_dict[k.upper()] = v

        attr_dict["__slots__"] = ["name", "age", "gender"]
        # return type.__new__(name, base, attr_dict)
        return super().__new__(cls, name, bases, attr_dict)


# 通过自定义的子类来创建类
class Test(metaclass=MyMetaClass):
    name = "ceshi"
    age = 99
    gender = "男"


# print(type(Test))
# print(Test.name)

# 父类指定元类，子类可以继承父类所指定的元类
class MyClass(Test):
    pass


# print(type(MyClass))

# 定义一个类，通过元类来让该类的类属性变成大写

t=Test()
print(t.__dict__)

# print(Test.__dict__)
