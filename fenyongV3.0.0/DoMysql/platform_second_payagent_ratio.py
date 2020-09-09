#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:26
# @Author :春衫
# @File :platform_second_payagent_ratio.py

from DoMysql.sql import SQL
from new_muban.XunZhao import xunzhao


def platform_second_payagent_ratio(ip, platform_id):
    '''

    :param order: 平台
    :return: 二级分佣比例
    '''

    select = "SELECT agent_id,sales_ratio,tco_ratio,free_sales_ratio FROM `ecloud_orders`.`second_payagent_ratio` WHERE `agent_id` = {0};".format(
        platform_id)

    data = SQL(ip).do_mysql_dict(select)
    data = xunzhao(data)

    return data
