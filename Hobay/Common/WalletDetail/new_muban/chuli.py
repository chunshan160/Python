#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/8 17:23
# @Author :春衫
# @File :chuli.py

from decimal import *
from Common.DoMysql.sql import SQL


def chulidata(data, ip, order):
    '''

    Parameters
    ----------
    data:待处理流水文本 list
    ip:数据库ip
    order:订单号

    Returns:把钱包变化之前的值、变化之后的值替换回去
    -------

    '''

    b = SQL(ip).current(order)

    b = list(b)


    for i in range(len(data)):

        data[i] = list(data[i])
        data[i][5] = b[i][0]
        data[i][4] = data[i][5] + data[i][3]
        data[i] = tuple(data[i])

    a = tuple(data)
    return a


if __name__ == '__main__':
    data = [(1000656, 2, 3, Decimal('-10.00'), None, None, '易贝购买商品：扣除买家订单易贝金额', 1),
            (1000656, 2, 1, Decimal('-0.10'), None, None, '易贝购买商品：扣除买家易贝服务费', 1),
            (1000656, 2, 1, Decimal('-0.30'), None, None, '易贝购买商品：扣除买家现金服务费', 3),
            (10, 2, 3, Decimal('10.00'), None, None, '易贝购买商品：扣除买家订单易贝金额转入平台', 1),
            (10, 2, 1, Decimal('0.10'), None, None, '易贝购买商品：扣除买家易贝服务费转入平台', 1),
            (10, 2, 1, Decimal('0.30'), None, None, '易贝购买商品：扣除买家现金服务费转入平台', 3),
            (10, 2, 3, Decimal('-10.00'), None, None, '易贝购买商品：订单易贝金额从平台转出', 1),
            (1000648, 2, 3, Decimal('10.00'), None, None, '易贝购买商品:扣除买家订单易贝金额转给卖家', 1),
            (10, 2, 1, Decimal('-0.10'), None, None, '易贝购买商品：扣除买家易贝服务费分润(服务费)总金额支出', 1),
            (1000648, 2, 2, Decimal('0.06'), None, None, '易贝购买商品：扣除买家易贝服务费分润', 1),
            (1000647, 2, 2, Decimal('0.01'), None, None, '易贝购买商品：扣除买家易贝服务费分润', 1),
            (1000646, 2, 2, Decimal('0.01'), None, None, '易贝购买商品：扣除买家易贝服务费分润', 1),
            (1000757, 2, 11, Decimal('0.00'), None, None, 'TCO分佣金额（易贝）收入', 1),
            (1000745, 2, 11, Decimal('0.00'), None, None, '业务焕商分佣金额（易贝）收入', 1),
            (10, 2, 2, Decimal('0.02'), None, None, '易贝购买商品：扣除买家易贝服务费分润', 1)]


