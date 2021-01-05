#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/8 17:23
# @Author :春衫
# @File :chuli.py

from decimal import *

from Web.Common.fengyong.sql.current import current


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
    b = current(ip,order)

    b = list(b)


    for i in range(len(data)):

        data[i] = list(data[i])
        data[i][5] = b[i][0]
        data[i][4] = data[i][5] + data[i][3]
        data[i] = tuple(data[i])

    a = tuple(data)
    return a


if __name__ == '__main__':
    data = [(1000419, 2, 3, Decimal('-10.00'), None, None, '易贝券支付购物商品费用：扣除买家订单易贝金额', 10),
            (10, 2, 3, Decimal('10.00'), None, None, '易贝券支付购物商品费用：扣除买家订单易贝金额转入平台', 1),
            (10, 2, 3, Decimal('-10.00'), None, None, '易贝券支付购物商品费用：订单易贝金额从平台转出', 1),
            (1000504, 2, 3, Decimal('10.00'), None, None, '易贝券支付购物商品费用:扣除买家订单易贝金额转给卖家', 1),
            (1000419, 2, 9, Decimal('-65.00'), None, None, '购买商品：扣除买家储备金', 11),
            (1000504, 2, 10, Decimal('15.00'), None, None, '购买商品：代理商分佣金额（激励金）收入', 2),
            (1000284, 2, 10, Decimal('35.00'), None, None, '购买商品：代理商分佣金额（激励金）收入', 2),
            (1000348, 2, 10, Decimal('2.00'), None, None, '购买商品：代理商分佣金额（激励金）收入', 2),
            (1000520, 2, 11, Decimal('1.50'), None, None, 'TCO分佣金额（现金）收入', 2),
            (1000519, 2, 11, Decimal('0.75'), None, None, '业务焕商分佣金额（现金）收入', 2),
            (1000515, 2, 11, Decimal('0.75'), None, None, '销售分佣金额（现金）收入', 2),
            (10, 2, 10, Decimal('10.00'), None, None, '购买商品：代理商分佣金额（激励金）收入', 2)]
    ip='192.168.0.102'
    order = 'EC-2020102118031100008854'
    a=chulidata(data, ip, order)
    print(a)


