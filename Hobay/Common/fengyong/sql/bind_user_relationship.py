#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:19
# @Author :春衫
# @File :bind_user_relationship.py

from Common.DoMySQL import SQL
from Common.fengyong.sql.business_relationship import business_relationship


def bind_user_relationship(ip, user_id):
    '''

    :param order: 用户id
    :return: 用户绑定的销售/业务焕商/TCO
    '''
    # SQL语句
    select = "SELECT business_user_id,bind_type FROM `ecloud_user2`.`bind_user_relationship` WHERE `user_id` = '{0}' AND `is_valid` = '1';".format(
        user_id)
    data = SQL(ip).do_mysql_dict(select)

    if data != ():
        for i in range(len(data)):
            business_user_id = data[i]['business_user_id']
            data2 = business_relationship(ip, business_user_id)
            if data2 == ():
                data.pop(i)
    else:
        data=None

    return data

if __name__ == '__main__':
    ip = "192.168.0.101"
    user_id = 1000656
    a=bind_user_relationship(ip, user_id)
    print(a)