#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/9 18:01
# @Author :春衫
# @File :qushe.py

def qushe(data):
    '''

    Parameters
    ----------
    data:待处理流水文本 list

    Returns:去掉不分佣的行 list
    -------

    '''

    data2 = []
    for i in range(len(data)):
        if data[i][0] != None:
            data2.append(data[i])

    return data2
