#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/22 9:51
# @Author :春衫
# @File :business_relationship.py

from Common.DoMySQL import SQL


def business_relationship(ip, bind_user_id):
    '''

    :param order: 用户id
    :return: 判断绑定的上级销售/TCO身份有没有失效
    '''
    # SQL语句
    select = f"SELECT * FROM `ecloud_user2`.`business_relationship` WHERE `business_user_id` = '{bind_user_id}' AND `is_valid` = '1';"
    data = SQL(ip).do_mysql_dict(select)

    return data

if __name__ == '__main__':
    bind_user_id=1000519
    ip='192.168.0.102'
    a=business_relationship(ip, bind_user_id)
    print(a)