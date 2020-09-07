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
# print(fun2(3))

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


# def count_book(a=0, b=0, c=0):
#     """算买100不等的方式"""
#     if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:  # 判断条件是否成
#         # print(a, b, c)
#         global count  # 更改全局变量计数
#         count += 1
#         print(count)
#     if a <= int(100 / 5):
#         if b <= int(100 / 3):
#             if c <= (100):
#                 return count_book(a, b, c + 1)
#             else:
#                 return count_book(a, b + 1)
#         else:
#             return count_book(a + 1)
#
#
# count_book()
# # 递归次数的最大限制python解释器默认的（1000）


