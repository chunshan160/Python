#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/14 12:59
# @Author :春衫
# @File :quchong.py

from decimal import *


# 去重
def quchong(list, a):
    '''

    :param list: 数据 list
    :param a: 指定去重元素
    :return: 去重后的结果
    '''

    new_list = []
    # 把相同的存进new_list
    for i in range(len(list)):
        if list[i] == a and type(list[i]) == type(a):
            new_list.append(i)

    # 把相同的从list里面删除
    for i in new_list[::-1]:
        list.pop(i)

    return list


if __name__ == '__main__':
    iii = [None, None, 111]
    b = quchong(iii, None)
    print(b)
