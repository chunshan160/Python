#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/19 12:14
# @Author :春衫
# @File :get_two_float.py

from decimal import *


def get_two_float(f_str, n):
    '''

    Parameters
    ----------
    f_str：'{}'.format(f_str) 也可以转换为字符串
    n：无论传入的函数有几位小数，在字符串后面都添加n位小数0

    Returns
    -------

    '''
    f_str = str(f_str)
    a, b, c = f_str.partition('.')
    c = (c + "0" * n)[:n]
    return ".".join([a, c])


if __name__ == '__main__':
    b = Decimal('0.1350')
    a = get_two_float(b, 2)
    print(a)
    print(type(a))
    d = Decimal(a)
    print(d)
    print(type(d))
