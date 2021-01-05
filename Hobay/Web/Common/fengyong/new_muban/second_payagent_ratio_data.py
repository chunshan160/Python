#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/14 18:24
# @Author :春衫
# @File :second_payagent_ratio_data.py
from Web.Common import platform_second_payagent_ratio
from Web.Common import second_payagent_ratio


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
        second_payagent_ratio_data = platform_second_payagent_ratio(ip, platform_id)
    # 买家注册地有代理商
    else:
        second_payagent_ratio_data = second_payagent_ratio(ip, province_id, city_id, area_id)

    return second_payagent_ratio_data


if __name__ == '__main__':
    ip = '192.168.0.102'

    province_id = None
    city_id = None
    area_id = 1000445
    platform_id = 10

    aaa = second_payagent_ratio_data(ip, province_id, city_id, area_id, platform_id)
    print(aaa)
