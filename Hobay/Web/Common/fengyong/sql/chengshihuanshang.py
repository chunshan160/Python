#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:16
# @Author :春衫
# @File :chengshihuanshang.py

from Web.Common.DoMySQL import SQL


def chengshihuanshang(ip, user_id):
    # 查询城市焕商具体是市代还是区代
    select = "SELECT area_code FROM `ecloud_user`.`partner_agent_area` WHERE `signed_user_id` = {0}".format(
        user_id)

    data = SQL(ip).do_mysql_dict(select)

    if data[0]['area_code'] == '':
        data = "市分佣比例"
    else:
        data = "区分佣比例"

    return data

if __name__ == '__main__':
    ip='192.168.0.102'
    a=chengshihuanshang(ip,1000446)
    print(a)
