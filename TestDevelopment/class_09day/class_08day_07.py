#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/18 15:43
# @Author :春衫
# @File :class_08day_07.py


dic = {"a": 11, "b": 22}

data = list(dic.items())

# 字典遍历的时候 不允许添加元素或者修改元素

dic["c"] = 11
print(data)

for i in data:
    print(i)
