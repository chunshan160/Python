#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:04
# @Author :春衫
# @File :order.py

from tools.sql import SQL


def order(ip, user):
    '''

    :param user: 买家id
    :return: 最新的一条订单号
    '''
    # SQL语句
    select = 'SELECT id,order_num FROM ecloud_orders.orders o WHERE  user_id=%d order by id desc limit 1;' % (user)
    data = SQL(ip).do_mysql(select)
    return data
