#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/6 13:09
# @Author :春衫
# @File :第12节_作业.py

import sys


# 作业

# 一:实现斐波那契数列数列，输入一个数列的位置数，返回斐波那契数列相应位置的值
# 斐波那契数列[1,1，2,3,5,8,13,21,34.....],第一个数是1，后面的数等于前两个数相加的结果Ⅰ

# def fixb(n):
#     if (n == 1 or n == 2):
#         return 1
#     else:
#         return fixb(n - 1) + fixb(n - 2)
#
#
# print(fixb(3))


# 二、古典问题:第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月
# 的兔子总数为多少?(意味着生长期为2)

# def fun2(n):
#     if n == 1 or n == 2:
#         return 2
#     else:
#         return (fun2(n - 2) + fun2(n - 1))
#
#
# print(fun2(6))

# 三、小明有100元钱打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共够多
# 少种买法?(面试笔试题)
# money = 100
# book = 100
# count = 0
# for a in range(int(money / 5)):
#     for b in range(int(money / 3)):
#         for c in range(int(money / 0.5)):
#             if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:
#                 print(a, b, c)
#                 count += 1
# print(count)

# sys.setrecursionlimit(3000)
#
# count = 0
#
#
# def count_book(a=0, b=0, c=0):
#     """算买100不等的方式"""
#     if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:  # 判断条件是否成
#         print(a, b, c)
#         global count  # 更改全局变量计数
#         count += 1
#     if a < int(100 / 5):
#         if b < int(100 / 3):
#             if c < (100):
#                 return count_book(a, b, c + 1)
#             else:
#                 return count_book(a, b + 1)
#         else:
#             return count_book(a + 1)
#
#
# count_book()
# # 递归次数的最大限制python解释器默认的（1000）

# 闭包
# def func():
#     print('----func被调用-—-----------')
#
#     def count_book():
#         print('这个是计算买书方式的函数')
#
#     return count_book

# #方法一：
# func()()
#
# #方法二：
# res = func( )
# res()


# 满足三个闭包条件:
# 条件一:函数中嵌套数
# 条件二:外层函数返回内存嵌套函数名
# 条件三:内层嵌套函数有引用外层的一个非全局变量

# 作用：实现数据的锁定 提高稳定性


# 二、装饰器
# 讲装饰器之前我们先来了解一下开放封闭原则(面向对象原则的核心)
# 开放封闭原则:软件实体应该是可扩展，而不可修改的。也就是说，对扩展是开放的，而对修改是封闭的。
# 装饰器的作用∶在不更改原功能函数内部代码，并且不改变调用方法的情况下为原函数添加新的功能。
# 装饰器的应用场景:
# 1.登录验证
# 2.函数运行时间统计
# 3.执行函数之前做准备工作
# 4.执行函教后清理功能
# 5.1、实现一个装饰器
# 在上面的过程中其实我们已经完成了一个装饰器定义并应用，只是现在的语法并不是安装整个的装饰器来写的，装
# 饰器之要在上面的基础稍加改动一点点就可以了

def func_a(fun):
    print('------func_a--调用了---')

    def func_w():
        print('----先洗手-')
        fun()

    return func_w
