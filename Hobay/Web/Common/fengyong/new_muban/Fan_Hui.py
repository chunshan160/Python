#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/7 18:05
# @Author :春衫
# @File :Fan_Hui.py

from Web.Common.fengyong.sql.wallet_detail import wallet_detail


def fan_hui(ip, order, expected_moban):  # 以后写回Excel对比用
    '''

    :param superior: 上级代理商/城市焕商
    :return: user_id, biz_type, changes, category
    '''
    sql_data = wallet_detail(ip,order)  # 支付数据
    user_id = []
    biz_type = []
    changes = []
    category = []

    for i in range(0, len(expected_moban)):
        mmm = (sql_data[i])[0]
        lll = (sql_data[i])[2]
        kkk = (sql_data[i])[3]
        nnn = (sql_data[i])[7]
        user_id.append(mmm)
        biz_type.append(lll)
        changes.append(kkk)
        category.append(nnn)
        # print('次数i:{0}'.format(i))

    return user_id, biz_type, changes, category
