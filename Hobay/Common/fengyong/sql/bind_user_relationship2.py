#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:21
# @Author :春衫
# @File :bind_user_relationship2.py


from Common.DoMySQL import SQL
from Common.fengyong.sql.business_relationship import business_relationship


def bind_user_relationship2(ip, user_id):
    '''

    :param order: 用户id
    :return: 销售/业务焕商的上级
    '''

    # SQL语句
    select = "SELECT business_user_id,bind_type FROM `ecloud_user2`.`bind_user_relationship` WHERE `user_id` = {0} AND `is_valid` = '1'  AND (`bind_type` = 'FREE_SALES' or `bind_type` = 'SALES');".format(
        user_id)

    data = SQL(ip).do_mysql_dict(select)

    bind_user_id=data[0]['business_user_id']
    data2 = business_relationship(ip,bind_user_id)

    if data == ():
        data = None
    else:
        if data2==():
            data=None

    return data

if __name__ == '__main__':
    id=1000519
    ip='192.168.0.102'
    a=bind_user_relationship2(ip,id)
    print(a)
