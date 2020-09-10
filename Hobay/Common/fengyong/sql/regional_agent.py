#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/9 11:06
# @Author :春衫
# @File :regional_agent.py

from Common.DoMySQL import SQL


def regional_agent(ip, phone):
    '''

    :param phone: 手机号
    :return:上级城市焕商/代理商
    '''
    # SQL语句
    # 查上级代理商
    select1 = "select a.type,u.id FROM (select c.id,c.type,c.province,c.city,c.area from ecloud_user.company c LEFT JOIN ecloud_user.`user` u ON (c.area=u.area and c.type = 3 )or (c.city=u.city and  c.type=2) OR (c.province=u.province and c.type =1) where u.phone='{0}') a LEFT JOIN ecloud_user.`user` u ON a.id = u.company_id;".format(
        phone)

    # 查询上级城市焕商
    select2 = "select p.signed_user_id,p.area_name from ecloud_user.partner_agent_area p LEFT JOIN ecloud_user.`user` u ON   (p.province_name=u.province and p.city_name=u.city and p.area_name=u.area) or (p.province_name=u.province and p.city_name=u.city and p.area_name='') OR ( p.province_name=u.province and p.city_name='' and p.area_name='') where u.phone ='{0}';".format(
        phone)

    data = SQL(ip).do_mysql_dict(select1)
    # print(data)
    # 如果查询上级代理商，数据为空 则根据sql2查询上级城市焕商
    if data == ():
        data = SQL(ip).do_mysql_dict(select2)

    return data
