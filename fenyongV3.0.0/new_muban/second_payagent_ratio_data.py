#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/14 18:24
# @Author :春衫
# @File :second_payagent_ratio_data.py

from Do_mysql.sql import SQL
from decimal import *


def second_payagent_ratio_data(ip, province_id, city_id, area_id, platform_id):
    '''

    Parameters
    ----------
    ip：数据库IP
    province_id：省代理商id
    city_id：市代理商id
    area_id：区代理商id
    platform_id：平台id

    Returns：返回所用的二级分佣比例
    -------

    '''

    # 买家注册地没有代理商
    if province_id == None and city_id == None and area_id == None:
        # 用平台比例
        second_payagent_ratio = SQL(ip).platform_second_payagent_ratio(platform_id)
    # 买家注册地有代理商
    else:
        second_payagent_ratio = SQL(ip).second_payagent_ratio(province_id, city_id, area_id)

    return second_payagent_ratio




if __name__ == '__main__':
    ip = '192.168.0.107'

    province_id = 13691
    city_id = 13947
    area_id = None
    platform_id = 8

    aaa=second_payagent_ratio_data(ip, province_id, city_id, area_id, platform_id)
    print(aaa)