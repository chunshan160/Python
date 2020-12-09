#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/7 16:36
# @Author :春衫
# @File :class_06day_func.py

# 伪多态的实现
class Base(object):
    def run(self):
        print("_Base_run_：慢慢走路")


class Cat(Base):
    def run(self):
        print("_Cat_run_：会爬树")


class Dog(Base):
    def run(self):
        print("_Dog_run_：跑得特别快")


class Pig(Base):
    def run(self):
        print("这个是一个幂运算的操作")


class CCC(object):
    def run(self):
        print("CCC功能")

class MyClass(object):
    def run(self):
        print("是MyClass的run方法")

b_obj = Base()
c_obj = Cat()
d_obj = Dog()
p_obj = Pig()

c=CCC()
m=MyClass()
# print(isinstance(c_obj,Base))

# Python中的函数的参数没有类型限制
# 假设func的参数需要Base类型的
def func(base_obj):
    base_obj.run()


func(b_obj)
func(c_obj)
func(d_obj)
func(p_obj)
func(c)
func(m)
