#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:27
# @Author :春衫
# @File :user_phone.py

from tools.sql import SQL


def user_phone(ip, user_id):
    '''

    :param order: 平台
    :return: 二级分佣比例
    '''

    # 使用execute()执行SQL语句
    select = "SELECT phone FROM `ecloud_user`.`user` WHERE  `id` = {0};".format(user_id)

    # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
    data = SQL(ip).do_mysql_dict(select)

    return data[0]['phone']
