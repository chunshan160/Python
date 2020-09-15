#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 14:20
# @Author :春衫
# @File :user_special_ratio.py

from Common.DoMySQL import SQL

def user_special_ratio(ip,user_id):
    #查询用户是否有临时费率  四种费率
    select = f"SELECT cbp_ratio,commission_ratio FROM `ecloud_user`.`user_special_ratio` WHERE `user_id` = '{user_id}' AND `deleted` = '-1';"
    data = SQL(ip).do_mysql_dict(select)
    if data != ():
        cbp_ratio=data[0]['cbp_ratio']
        commission_ratio=data[0]['commission_ratio']
        return cbp_ratio,commission_ratio

if __name__ == '__main__':
    a=user_special_ratio("192.168.0.101",1000166)
    print(a)