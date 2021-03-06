#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/5 17:15
# @Author :春衫
# @File :第10节_递归函数、纯函数、匿名函数和偏函数.py


# from collections import Iterable
from functools import partial

# 一、递归函数
# 问题一:函数内部可以调用自身这个函数吗?
# 递归函数:在函数中调用函数自身，我们把这样的函数叫做递归函数
# 递归边界:退出递归的终止条件

# 案列需求一:通过递归函数实现的任意数的阶乘通过递归函数实现的任意数的阶乘


# def func(n):
#     # 判断n是否等于1 ,如果等于则返回1，
#     if n == 1:  # 递归临界点:不再调用自身函数的条件
#         return n
#     else:
#         # 不等于则继续调用自身函数进行判断
#         return n * func(n - 1)  # 3*2*1


# res = func(3)




# 二、纯函数
# 2.1、纯函数的概念
# 简单来说，一个函数的返回结果只依赖于它的参数（没有引用外部变量），并且在执行过程里面没有副作用，我们就把这个函数叫做纯函数。

# 2.1、纯函数的3个原则
# ·变量都只在函数作用域内获取,作为的函数的参数传入
# ·不会产生副作用(side effects),不会改变被传入的数据或者其他数据（全局变量)
# ·相同的输入保证相同的输出

# 2.3函数的副作用
# ·副作用是指函数被调用，完成了函数既定的计算任务，但同时因为访问了外部数据，尤其是因为对外部数据进行了写操作，从而一定程度地改变了系统环境


# 案例说明:
# 函数func1返回的结果为两个参数相加的结果
# def func1(a, b):
#     return a + b


# var1 = 100


# 函数func2返回的结果为参数a和外部变量var1相加的结果
# def func2(a):
#     return var1 + a


# 在上面的两个案例中func1返回的结果只受传入的参数的影响，而func2不仅受传入参数的影响而且还会受外部变量var1的影响，像func1这样的返回值只跟传入参数有关的函数我们把它叫做纯函数。



