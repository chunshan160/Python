#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:11
# @Author :春衫
# @File :reserve_fund_sql.py

from Web.Common.DoMySQL import SQL


def reserve_fund_sql(ip, user_id):
    '''

    :param user_id: 买家id
    :return: 未消耗充值金额,储备池金额  dict
    '''

    # 查储备池
    select = "SELECT sum(r.charge_amount) charge_amount,sum(r.reserve_fund) reserve_fund FROM ecloud_orders.reserve_fund_orders r WHERE r.user_id= {0} and r.is_use=0;".format(
        user_id)

    data = SQL(ip).do_mysql_dict(select)

    return data[0]
