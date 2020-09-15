#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 14:26
# @Author :春衫
# @File :platform_promotion_ratio.py

from Common.DoMySQL import SQL

def platform_promotion_ratio(ip):
    # 查询是否有活动费率
    select = f"SELECT * FROM `ecloud_user`.`platform_promotion_ratio` WHERE `deleted` = '-1';"
    data = SQL(ip).do_mysql_dict(select)
    if data != ():
        cbp_ratio = data[0]['cbp_ratio']
        commission_ratio = data[0]['commission_ratio']
        return cbp_ratio, commission_ratio

if __name__ == '__main__':
    a=platform_promotion_ratio("192.168.0.101")
    print(a)