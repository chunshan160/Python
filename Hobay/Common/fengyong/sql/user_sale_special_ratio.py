#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/21 15:36
# @Author :春衫
# @File :user_sale_special_ratio.py

from Common.DoMySQL import SQL

def user_sale_special_ratio(ip,user_id):
    #查询用户的临时销售费率
    select = f"SELECT commission_ratio FROM `ecloud_user`.`user_sale_special_ratio` WHERE `user_id` = '{user_id}' AND `deleted` = '-1';"
    data = SQL(ip).do_mysql_dict(select)
    if data != ():
        sale_cash_ratio=data[0]['commission_ratio']
        return float(sale_cash_ratio)

if __name__ == '__main__':
    a=user_sale_special_ratio("192.168.0.102",2000482)
    print(a)
    print(type(a))