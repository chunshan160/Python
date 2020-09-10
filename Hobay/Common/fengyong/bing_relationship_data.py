#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/7 17:18
# @Author :春衫
# @File :bing_relationship_data.py

from Common.fengyong.sql.bind_user_relationship import bind_user_relationship
from Common.fengyong.new_muban.bind_user_relationship import bind_user_relationship_id


class BingRelationshipData:

    def bing_relationship_data(self, ip, payment_method, data, buyer_id):
        # 查询买家是否绑定销售/业务焕商/TCO
        if payment_method in ["易贝", "易贝券"]:
            # 获取买家绑定的销售/业务焕商/TCO dict
            bind_buyer_relationship = bind_user_relationship(ip, buyer_id)
            if bind_buyer_relationship != None:
                bind_buyer_relationship_data = bind_user_relationship_id(ip, bind_buyer_relationship)
            else:
                bind_buyer_relationship_data = None

            return bind_buyer_relationship_data

        elif payment_method in ["抵工资", "家人购", "现金"]:
            if payment_method == "现金":
                payer_id = data['卖家']
            else:
                payer_id = data['出钱方']

            # 获取买家绑定的销售/业务焕商/TCO dict
            bind_buyer_relationship = bind_user_relationship(ip, buyer_id)
            if bind_buyer_relationship != None:
                bind_buyer_relationship_data = bind_user_relationship_id(ip, bind_buyer_relationship)
            else:
                bind_buyer_relationship_data = None

            # 获取出钱人绑定的销售/业务焕商/TCO dict
            bind_payer_relationship = bind_user_relationship(ip, payer_id)
            if bind_payer_relationship != None:
                bind_payer_relationship_data = bind_user_relationship_id(ip, bind_payer_relationship)
            else:
                bind_payer_relationship_data = None

            return bind_buyer_relationship_data, bind_payer_relationship_data
