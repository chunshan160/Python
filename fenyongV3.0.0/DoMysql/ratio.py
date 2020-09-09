#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:13
# @Author :春衫
# @File :ratio.py

from DoMysql.sql import SQL
from tools.quchong import quchong

# 查上级分佣比例
def ratio(ip, province_id, city_id, area_id, personal_id):

    zong_id = [province_id, city_id, area_id, personal_id]
    user_id = tuple(quchong(zong_id, None))

    if user_id == ():
        data = None
    else:
        # 查上级分佣比例
        if len(user_id) == 1:
            user_id = user_id[0]
            select = "SELECT user_id,ratio,type FROM ecloud_orders.user_agent_ratio WHERE user_id = {0};".format(
                user_id)
        elif user_id != ():
            select = "SELECT user_id,ratio,type FROM ecloud_orders.user_agent_ratio WHERE user_id in {0};".format(
                user_id)

        data = SQL(ip).do_mysql_dict(select)

    return data