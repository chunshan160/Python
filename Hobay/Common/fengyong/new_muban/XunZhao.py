#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/12 12:43
# @Author :春衫
# @File :XunZhao.py

from decimal import *


def xunzhao(data):
    '''

    Parameters
    ----------
    data：省市区平台二级分佣比例

    Returns
    -------

    '''
    #也许需要考虑没有上级省市区的情况
    ratio = None

    i = 0
    while i < len(data):
        if data[i]['sales_ratio'] == Decimal('0.00') and data[i]['tco_ratio'] == Decimal('0.00') and \
                data[i]['free_sales_ratio'] == Decimal('0.00'):
            i += 1
        else:
            ratio = data[i]
            break

    return ratio


if __name__ == '__main__':
    # data = [{'agent_id': 1000347, 'sales_ratio': Decimal('0.00'), 'tco_ratio': Decimal('0.00'),
    #          'free_sales_ratio': Decimal('0.00')},
    #         {'agent_id': 1000348, 'sales_ratio': Decimal('0.00'), 'tco_ratio': Decimal('0.00'),
    #          'free_sales_ratio': Decimal('0.00')},
    #         {'agent_id': 1000349, 'sales_ratio': Decimal('0.00'), 'tco_ratio': Decimal('0.00'),
    #          'free_sales_ratio': Decimal('0.00')}]

    data = []

    a = xunzhao(data)
    print(a)
