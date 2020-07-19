#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/28 13:34
# @Author :春衫
# @File :ten.py

# #1、变量的交换
# a=1
# b=2
# a,b=b,a
# print(a,b)
#
# #2、字符串格式化 f-string
# name="Ross"
# country="china"
# age=28
#
# print(f"la,{name},la,{country},la{age+1}")

# # 3、yield 生成器
# def fibonacci(n):
#     a = 0
#     b = 1
#     # nums=[]
#     # for _ in range(n):
#     #     nums.append(a)
#     #     a,b=b,a+b
#     # return nums
#
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# for i in fibonacci(10):
#     print(i)

# #4、列表解析式
# fruit=["appear","pear","pineapple","orange","banana"]
#
# # # for i in range(len(fruit)):
# # #     fruit[i]=fruit[i].upper()#改成大写
# #
# # fruit=[x.upper() for x in fruit]
# #
# # print(fruit)
#
# #挑选a开头的水果
# # filtered_fruit=[]
# # for f in fruit:
# #     if f.startswith("a"):
# #         filtered_fruit.append(f)
#
# #新列表x x来自fruit 满足条件首字母为a
# filtered_fruit=[x for x in fruit if x.startswith("a")]
# print(filtered_fruit)

# #5、Enumerate 函数 元素和索引值
# #获取元素和索引值
# fruit=["appear","pear","pineapple","orange","banana"]
# for i,x in enumerate(fruit):
#     print(i,x)

# #6.1、反向遍历 reversed
# fruit=["appear","pear","pineapple","orange","banana"]
# for i,x in enumerate(reversed(fruit)):
#     print(i,x)

# #6.2、按顺序遍历 sorted
# #以首字母排序遍历
# fruit=["appear","pear","pineapple","orange","banana"]
# for i,x in enumerate(sorted(fruit)):
#     print(i,x)

# #7、字典的合并操作
# a={"a":"123","b":"123","c":"123"}
# b={"1":"123","2":"123","3":"123"}
#
# # c={}
# # for k in a:
# #     c[k]=a[k]
# # for k in b:
# #     c[k]=b[k]
#
# c={**a,**b}
#
# print(c)

# #8、三元运算符 Ternary Operator
# score=70
# # if score>60:
# #     s="pass"
# # else:
# #     s="fail"
#
# s="pass" if score >60 else "fail"
# print(s)

#9、序列解包
name="San Zhang"

# str_list=name.split()
# first_name=str_list[0]
# last_name=str_list[1]
# print(first_name,last_name)

first_name,last_name=name.split()
print(first_name,last_name)