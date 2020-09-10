#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:21
# @Author :春衫
# @File :bind_user_relationship2.py


from Common.DoMySQL import SQL


def bind_user_relationship2(ip, user_id):
    '''

    :param order: 用户id
    :return: 销售/业务焕商的上级
    '''

    # SQL语句
    select = "SELECT business_user_id,bind_type FROM `ecloud_user2`.`bind_user_relationship` WHERE `user_id` = {0} AND `is_valid` = '1'  AND (`bind_type` = 'FREE_SALES' or `bind_type` = 'SALES');".format(
        user_id)

    data = SQL(ip).do_mysql_dict(select)

    if data == ():
        data = None

    return data
