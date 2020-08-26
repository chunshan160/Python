#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/26 12:32
# @Author :春衫
# @File :01、元祖列表字典集合.py

import timeit
from collections import namedtuple

# 1、元祖和列表的性能分析

# 创建元祖比创建列表快得多
# 元祖占用内存小

# 计算创建元祖和列表所需的时间：ipython 中使用 timeit
# pip install ipython
# 计算时间模块


# def func():
#     for i in range(10):
#         print(i)

# res=timeit.Timer(func).timeit(100)
# print(res)

# res = timeit.timeit('[1,2,3]')
# print(res)


# 2、元组取值
# 方式一:
tu = ('小明', 18, '男')
NAME = 0
AGE = 1
GENDER = 2
name = tu[NAME]  # 获取姓名
AGE = tu[AGE]  # 获取年龄
GENDER = tu[GENDER]  # 获取性别
# print(name)
# print(AGE)
# print(GENDER)

# # 方式二：
# # 命名元组
# student_info = namedtuple('student_info', ['name', 'age', 'gender'])
# tu = student_info('小明', 18, '男')
# print(tu)  # student_info(name='小明', age=18, gender='男')
# print(tu.name)  # 小明
# print(type(tu))  # class 类
# print(type(student_info))  # type 元类

# 字典和集合 {}
se = set()  # 创建空集合
set1 = {1, 2, 3}  # 集合 只有值没有键
dic = {}  # 空字典

# 集合会去重
set2 = {1, 1, 1, 2, 2, 2, 3, 3, 3}
# print(set2)

# 利用集合 对列表去重
li = [1, 2, 1, 1, 1, 2, 3, 4]
li2 = list(set(li))
print(li2)

# 集合 添加数据
se.add('ceshi')  # 添加
print(se)
se.remove('ceshi')  # 删除
print(se)

se.update((11, 22, 33))  # 注意这里是传了个元祖  等同列表extend方法
print(se)
se.clear()  # 清空
se.copy()  # 复制


#集合是无序的  Python3.7后字典是有序的