#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:22
# @Author :春衫
# @File :second_payagent_ratio.py

from Web.Common.DoMySQL import SQL
from Web.Common import xunzhao
from Web.Common import quchong


def second_payagent_ratio(ip, province_id, city_id, area_id):
    '''

    :param order: 省市区平台
    :return: 二级分佣比例
    '''

    zong_id = [province_id, city_id, area_id]
    user_id = tuple(quchong(zong_id, None))

    # 使用execute()执行SQL语句
    if len(user_id) == 3:
        select = "SELECT agent_id,sales_ratio,tco_ratio,free_sales_ratio FROM `ecloud_orders`.`second_payagent_ratio` WHERE `agent_id` IN {0} order by field(agent_id ,{1},{2},{3});".format(
            user_id, user_id[0], user_id[1], user_id[2])
    elif len(user_id) == 2:
        select = "SELECT agent_id,sales_ratio,tco_ratio,free_sales_ratio FROM `ecloud_orders`.`second_payagent_ratio` WHERE `agent_id` IN {0} order by field(agent_id ,{1},{2});".format(
            user_id, user_id[0], user_id[1])
    else:
        select = "SELECT agent_id,sales_ratio,tco_ratio,free_sales_ratio FROM `ecloud_orders`.`second_payagent_ratio` WHERE `agent_id` = {0};".format(
            user_id[0])

    data = SQL(ip).do_mysql_dict(select)
    data = xunzhao(data)
    return data

if __name__ == '__main__':
    province_id = None
    city_id = None
    area_id = 1000445
    ip="192.168.0.102"
    a=second_payagent_ratio(ip, province_id, city_id, area_id)
    print(a)