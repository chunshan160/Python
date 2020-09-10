#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:10
# @Author :春衫
# @File :personal.py

from tools.sql import SQL


def personal(ip, phone):
    '''

    :param phone: 手机号
    :return: 绑定的个人焕商 dict
    '''

    # 查是否绑定个人焕商
    select = "SELECT u.agent_id FROM ecloud_user.`user` u WHERE u.phone='{0}';".format(phone)
    data = SQL(ip).do_mysql_dict(select)

    # 如果agent_id的值为None
    if (data[0])['agent_id'] == None or (data[0])['agent_id'] == 0:
        data = {"个人焕商": None}
    else:
        data = {"个人焕商": (data[0])['agent_id']}

    return data
