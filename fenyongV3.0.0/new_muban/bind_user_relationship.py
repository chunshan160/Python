#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/14 17:18
# @Author :春衫
# @File :bind_user_relationship.py
from DoMysql.bind_user_relationship2 import bind_user_relationship2


def bind_user_relationship_id(ip, data):
    '''

    Parameters
    ----------
    ip:数据库ip
    data:用户绑定的销售/业务焕商/TCO

    Returns:文字转换后的用户绑定的销售/业务焕商/TCO
    -------

    '''

    b = {}

    for i in range(len(data)):
        if data[i]['bind_type'] == "FREE_SALES":
            b["业务焕商"] = data[i]['business_user_id']

        elif data[i]['bind_type'] == "SALES":
            b["销售"] = data[i]['business_user_id']

        else:
            b["TCO"] = data[i]['business_user_id']

    
    if "业务焕商" in b.keys():
        Q = bind_user_relationship2(ip,b["业务焕商"])

    elif "销售" in b.keys():
        Q = bind_user_relationship2(ip,b["销售"])

    

    if Q != None:
        b["买家上级的上级id"] = Q[0]['business_user_id']
        b["买家上级的上级身份"] = Q[0]['bind_type']
        if b["买家上级的上级身份"] =='SALES':
            b["买家上级的上级身份"] ="销售"
        elif b["买家上级的上级身份"] =='FREE_SALES':
            b["买家上级的上级身份"] ="业务焕商"
        elif b["买家上级的上级身份"] =='TCO':
            b["买家上级的上级身份"] ="TCO"
    else:
        b["买家上级的上级id"] = None
        b["买家上级的上级身份"] = None



    return b


if __name__ == '__main__':
    ip = '192.168.0.107'
    data = [{'business_user_id': 1000218, 'bind_type': 'SALES'}, {'business_user_id': 1000222, 'bind_type': 'TCO'}]
    qqq = bind_user_relationship_id(ip, data)
    print(qqq)
    # {'业务焕商': 1000745, 'TCO': 1000757, '销售': None, '买家上级的上级id': None, '买家上级的上级身份': None}

