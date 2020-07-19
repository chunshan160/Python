#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 12:33
# @Author :春衫
# @File :sql.py

import pymysql
from tools.quchong import quchong


class SQL:

    def __init__(self, ip):
        self.ip = ip

    def wallet_detail(self, order):
        '''

        :param order: 订单号
        :return: 流水详情
        '''
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor()

        # 使用execute()执行SQL语句
        select = 'SELECT b.user_id,b.type,b.biz_type,b.changes,b.result,b.current,b.note,b.category from orders a, wallet_detail b where a.order_num="%s" and a.id=b.source_id;' % (
            order)
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()
        db.close()

        return data

    def order(self, user):
        '''

        :param user: 买家id
        :return: 最新的一条订单号
        '''
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor()

        # 使用execute()执行SQL语句
        select = 'SELECT order_num FROM ecloud_orders.orders o WHERE  user_id=%d order by id desc limit 1;' % (user)
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()

        db.close()

        return data

    def regional_agent(self, phone):
        '''

        :param phone: 手机号
        :return:上级城市焕商/代理商
        '''
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 使用execute()执行SQL语句
        # 查上级代理商
        select1 = "select a.type,u.id FROM (select c.id,c.type,c.province,c.city,c.area from ecloud_user.company c LEFT JOIN ecloud_user.`user` u ON (c.area=u.area and c.type = 3 )or (c.city=u.city and  c.type=2) OR (c.province=u.province and c.type =1) where u.phone='{0}') a LEFT JOIN ecloud_user.`user` u ON a.id = u.company_id;".format(
            phone)

        # 查询上级城市焕商
        select2 = "select p.signed_user_id,p.area_name from ecloud_user.partner_agent_area p LEFT JOIN ecloud_user.`user` u ON   (p.province_name=u.province and p.city_name=u.city and p.area_name=u.area) or (p.province_name=u.province and p.city_name=u.city and p.area_name='') OR ( p.province_name=u.province and p.city_name='' and p.area_name='') where u.phone ='{0}';".format(
            phone)

        cursor.execute(select1)
        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()

        # 如果查询上级代理商，数据为空 则根据sql2查询上级城市焕商
        if data == ():
            cursor.execute(select2)
            # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
            data = cursor.fetchall()

        db.close()

        return data

    def personal(self, phone):
        '''

        :param phone: 手机号
        :return: 绑定的个人焕商 dict
        '''
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 查是否绑定个人焕商
        select = "SELECT u.agent_id FROM ecloud_user.`user` u WHERE u.phone='{0}';".format(phone)
        # 使用execute()执行SQL语句
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()
        # print(data)

        # 如果agent_id的值为None
        if (data[0])['agent_id'] == None or (data[0])['agent_id'] == 0:
            data = {"个人焕商": None}
        else:
            data = {"个人焕商": (data[0])['agent_id']}

        db.close()

        return data

    def reserve_fund(self, user_id):
        '''

        :param user_id: 买家id
        :return: 未消耗充值金额,储备池金额  dict
        '''
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 使用execute()执行SQL语句

        # 查储备池
        select = "SELECT sum(r.charge_amount) charge_amount,sum(r.reserve_fund) reserve_fund FROM ecloud_orders.reserve_fund_orders r WHERE r.user_id= {0} and r.is_use=0;".format(
            user_id)
        # 返回未消耗的充值金额和储备池金额
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()

        db.close()

        return data[0]

    #查上级分佣比例
    def ratio(self, province_id, city_id, area_id, personal_id):

        zong_id = [province_id, city_id, area_id, personal_id]
        user_id = tuple(quchong(zong_id, None))
        # 打开数据库连接
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_orders')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 使用execute()执行SQL语句
        if user_id == ():
            data = None
        else:
            # 查上级分佣比例
            if len(user_id) == 1:
                user_id = user_id[0]
                select = "SELECT user_id,ratio,type FROM ecloud_orders.user_agent_ratio WHERE user_id = {0};".format(
                    user_id)
            elif user_id != ():
                select = "SELECT user_id,ratio,type FROM ecloud_orders.user_agent_ratio WHERE user_id in {0};".format(
                    user_id)

            # print("select", select)

            # 返回
            cursor.execute(select)

            # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
            data = cursor.fetchall()
            # print(data)

            db.close()

        return data

    def chengshihuanshang(self, user_id):

        # 打开数据库连接
        global qqq
        db = pymysql.connect(host=self.ip,
                             port=3306,
                             user='root',
                             passwd='iloveyou2016,./',
                             db='ecloud_user')

        # 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
        cursor = db.cursor(pymysql.cursors.DictCursor)

        # 使用execute()执行SQL语句

        # 查询城市焕商具体是市代还是区代
        select = "SELECT area_code FROM `ecloud_user`.`partner_agent_area` WHERE `signed_user_id` = {0}".format(
            user_id)
        # 返回
        cursor.execute(select)

        # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        data = cursor.fetchall()

        if data[0]['area_code'] == '':
            qqq = "市分佣比例"
        else:
            qqq = "区分佣比例"

        db.close()

        return qqq


if __name__ == '__main__':
    pass
    # a = SQL(ip).wallet_detail('EC - 2020050719172600010767')
    # print(a)
    # print(type(a))
    # b = SQL('192.168.0.101').regional_agent(17777777781)
    # # b = SQL().regional_agent(17777777784)
    # print(b)

    # c = SQL('192.168.0.101').personal(17777777781)
    # print(c)
    #
    # d = SQL('192.168.0.101').reserve_fund(1000656)
    # print(d)
    # print(type(d))
    # b={'charge_amount': Decimal('100'), 'reserve_fund': Decimal('60.00')}
    # print(b['reserve_fund'])

    f=SQL('192.168.0.102').regional_agent(17777777774)
    print(f)

    # sss = SQL('192.168.0.102').ratio(None,15239, None, None)
    # print(sss)
