#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 14:20
# @Author :春衫
# @File :user_special_ratio.py

from Common.DoMySQL import SQL

def user_special_ratio(ip,user_id):
    #查询用户的临时采购费率+临时销售费率
    select1 = f"SELECT cbp_ratio,commission_ratio FROM `ecloud_user`.`user_special_ratio` WHERE `user_id` = '{user_id}' AND `deleted` = '-1';"
    select2=f"SELECT * FROM `ecloud_user`.`user_sale_special_ratio` WHERE `user_id` = '{user_id}' AND `deleted` = '-1';"
    data1 = SQL(ip).do_mysql_dict(select1)
    data2 = SQL(ip).do_mysql_dict(select2)

    buy_cbp_ratio = None
    buy_cash_ratio=None
    sale_cash_ratio=None

    if data1 != ():
        buy_cbp_ratio=data1[0]['cbp_ratio']
        buy_cash_ratio=data1[0]['commission_ratio']

    if data2 !=():
        sale_cash_ratio=data2[0]['commission_ratio']

    return buy_cbp_ratio,buy_cash_ratio,sale_cash_ratio

if __name__ == '__main__':
    a=user_special_ratio("192.168.0.101",1000656)
    print(a)