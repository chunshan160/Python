#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/26 12:32
# @Author :春衫
# @File :第05节_元组和列表的原理和操作.py

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

# 集合是无序的  Python3.7后字典是有序的

# 数值:1
# 序列:字符串 列表 元祖
# 散列:字典 集合 #特征 内部元素是无序的

# 二、字典和集合的原理和应用
# dict与set实现原理是一样的， 都是将实际的值放到list中,唯一不同的在 于hash函数操作的对象，对于dict, hash
# 函数操作的是其key,而对于set是直接操作的它的元素，假设操作内容为x，其作为因变量,放入hash函数,通过
# 运算后取list的余数, I转化为-个list的下标, 此下标位置对于set而言用来放其本身，而对于dict则是创建了两个
# list,一个list该 下表放此key,另-个list中该下标方对应的value。其中,我们把实现set的方式叫做HashSet,实
# 现dict的方式叫做Hash Map/Table(注: map指的就是通过key来寻找value的过程

# 2、字典查找值的过程

# 计算键的散列值--使用散列值的一部分来定位散列表中的一个表元--表元为空？--是--抛出keyError--否--键相等？
# --是--返回表元里的值--否（散列冲突）--使用散列值的另一部分来定位散列表中的另一行--表元为空？


#可变和不可变：可hash  不可hash
#集合值不可变 只能存储不可变类型
#字典key不可变 只能存储不可变类型

#性能分析
#从时间上比较：集合 字典 元祖 列表  越来越慢
#占用内存比较：字典 集合 列表 元祖  越来越小