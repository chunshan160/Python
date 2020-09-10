#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 12:33
# @Author :春衫
# @File :DoMySQL.py

import pymysql


class SQL:

    def __init__(self, ip):
        self.ip = ip

    def do_mysql_tuple(self,select):
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor()

        # 使用execute()执行SQL语句
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()
        db.close()

        return data

    def do_mysql_dict(self,select):
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 使用execute()执行SQL语句
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()
        db.close()

        return data

if __name__ == '__main__':
    pass
    a = SQL('192.168.0.101').do_mysql_dict("SELECT phone FROM `ecloud_user`.`user` WHERE  `id` = 1000656;")
    print(a)

    # b = SQL('192.168.0.101').bind_user_relationship2(1000745)
    # print(b)

    # print(type(a))
    # b = SQL('192.168.0.107').second_payagent_ratio(11602, 11601, 1000176)
    # b = SQL('192.168.0.107').second_payagent_ratio(13691, 13947, None)

    # b = SQL('192.168.0.107').regional_agent(17777777786)
    # b=SQL('192.168.0.101').order(1000166)
    # print(b)

    # c = SQL('192.168.0.101').current("EC-2020061614153800014047")
    # print(c)
    # print(len(c))

    # c=SQL('192.168.0.101').user_phone(1000656)
    # print(c)

    # d = SQL('192.168.0.107').bind_user_relationship(1000173)
    # print(d)
    # print(type(d))
    # b={'charge_amount': Decimal('100'), 'reserve_fund': Decimal('60.00')}
    # print(b['reserve_fund'])

    # f = SQL('192.168.0.102').regional_agent(17777777774)
    # print(f)
