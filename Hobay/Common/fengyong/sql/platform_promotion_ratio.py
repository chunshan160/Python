#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 14:26
# @Author :春衫
# @File :platform_promotion_ratio.py
import time

from Common.DoMySQL import SQL

def platform_promotion_ratio(ip):
    now_time = int(round(time.time() * 1000))
    # 查询是否有活动费率
    select = f"SELECT * FROM `ecloud_user`.`platform_promotion_ratio` WHERE `deleted` = '-1' AND `end_time` >= {now_time};"
    data = SQL(ip).do_mysql_dict(select)
    if data != ():
        buy_cbp_ratio = data[0]['cbp_ratio']
        buy_cash_ratio = data[0]['commission_ratio']
        sale_cash_ratio=data[0]['sale_commission_ratio']
        return buy_cbp_ratio, buy_cash_ratio,sale_cash_ratio

if __name__ == '__main__':
    a=platform_promotion_ratio("192.168.0.101")
    print(a)