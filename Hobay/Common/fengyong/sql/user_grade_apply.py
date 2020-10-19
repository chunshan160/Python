#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 13:58
# @Author :春衫
# @File :user_grade_apply.py

from Common.DoMySQL import SQL
from TestData.user_grade import cbp
from TestData.user_grade import cash

def user_grade_ratio(ip,user_id):
    global grade
    #查询用户的等级，获取等级支付服务费费率
    select = f"SELECT grade_id FROM `ecloud_user`.`user` WHERE `id` = '{user_id}';"
    data = SQL(ip).do_mysql_dict(select)
    if data[0]['grade_id']==1:
        grade="普通会员"
    elif data[0]['grade_id']==2:
        grade="白银会员"
    elif data[0]['grade_id']==3:
        grade="黄金会员"
    elif data[0]['grade_id']==4:
        grade="铂金会员"
    elif data[0]['grade_id']==5:
        grade="钻石会员"

    buy_cbp_ratio=cbp[grade]
    buy_cash_ratio=cash[grade]
    sale_cash_ratio=buy_cbp_ratio+buy_cash_ratio
    return buy_cbp_ratio,buy_cash_ratio,sale_cash_ratio

if __name__ == '__main__':
    a=user_grade_ratio("192.168.0.102",1000166)
    print(a)