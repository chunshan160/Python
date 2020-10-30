#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:01
# @Author :春衫
# @File :wallet_detail.py

from Common.DoMySQL import SQL


def wallet_detail(ip, order):
    '''
    :param ip: 数据库IP
    :param order: 订单号
    :return: 流水详情
    '''
    # SQL语句
    select = f'SELECT b.user_id,b.type,b.biz_type,b.changes,b.result,b.current,b.note,b.category from `ecloud_orders`.`orders` a, `ecloud_orders`.`wallet_detail` b where a.order_num="{order}" and a.id=b.source_id;'
    # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
    data = SQL(ip).do_mysql_tuple(select)
    return data


if __name__ == '__main__':
    a=wallet_detail("192.168.0.101","EC-2020103010170000000456")
    print(a)