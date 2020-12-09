#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/8 11:50
# @Author :春衫
# @File :class_06day_attr.py

class Test:
    # 公有属性
    attr1 = 1000
    # 私有属性
    _attr2 = 3000  # 对外公开
    __attr3 = 4000  # 对外改名字


c = Test()


# 类属性可以通过类和实例来访问
# print(Test.attr1)#指向类
# print(Test().attr1)#指向实例
# print(c.attr1)

# 单下划线先开头的私有属性
# print(Test._attr2)
# print(c._attr2)

# 双下划线先开头的私有属性
# 双下划线开头的私有属性，对外不能直接访问
# 为了保护这个变量，对外改了一个名字
# 在原有的属性名前面加了一个类名
# print(Test.__attr3)  # AttributeError: type object 'Test' has no attribute '__attr3'
# print(c.__attr3)

# print(Test.__dict__)  # 打印类所有属性
# '_Test__attr3'
# print(Test._Test__attr3)

# 私有属性的继承问题
class A(Test):
    name="ceshi"
    __name="test"


# a = A()

# print(a.attr1)
# print(a._attr2)
# print(a._Test__attr3)
# 私有属性可以继承

# __dict__ 不是继承就会消耗内存
class B:
    name = "ceshi"
    __name = "test"


b = B()
print(A.__dict__)
print(B.__dict__)
