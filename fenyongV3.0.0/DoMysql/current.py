#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:18
# @Author :春衫
# @File :current.py

from DoMysql.sql import SQL


def current(ip, order):
    '''

    :param order: 订单号
    :return: 钱包变化值 tuple
    '''

    select = 'SELECT b.current from `ecloud_orders`.`orders` a, `ecloud_orders`.`wallet_detail` b where a.order_num="%s" and a.id=b.source_id;' % (
        order)

    data = SQL(ip).do_mysql_tuple(select)

    return data
