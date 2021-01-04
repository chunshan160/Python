#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/18 15:43
# @Author :春衫
# @File :class_08day_07.py


dic = {"a": 11, "b": 22}

data = list(dic.items())

# 字典遍历的时候 不允许添加元素或者修改元素

# dic["c"] = 11
# print(data)
#
# for i in data:
#     print(i)



li1=[1,2]
li2=[11,22]
li1.append(li2[0])
li2.append(li1[0])

li=[3,4]
print(li2)