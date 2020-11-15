#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/24 17:07
# @Author :春衫
# @File :ceshi.py

def input_number():
    number = input("请输入四位数字：")
    if str.isdigit(number):
        print("输入成功！")
        return number
    else:
        print("请重新输入四位数字！")


# input_number=input_number()

def max_number(number):
    list_number = []
    for k in range(len(number)):
        a = number[k]
        list_number.append(int(a))
    print(list_number)

    n = len(list_number)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_number[j] > list_number[j + 1]:
                list_number[j], list_number[j + 1] = list_number[j + 1], list_number[j]

    print(list_number)
    max_number=""
    for l in range(n):
        max_number=max_number+str(list_number[l])
    print(max_number[::-1])
max_number("1564")


