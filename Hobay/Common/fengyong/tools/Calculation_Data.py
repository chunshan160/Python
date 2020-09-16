#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/7 17:38
# @Author :春衫
# @File :calculation_Data.py

from Common.fengyong.Calculation.calculation import Calculation


class CalculationData:
    def calculation_data(self, ip, payment_method, member_level, buyer_identity, seller_identity, proportion,
                         charge_amount, reserve_fund, order,user_id):

        if payment_method in ["易贝", "易贝券"]:
            buyer_province_proportion = proportion['省分佣比例']
            buyer_city_proportion = proportion['市分佣比例']
            buyer_area_proportion = proportion['区分佣比例']
            buyer_personal_proportion = proportion['个人分佣比例']
            disanfang_province_proportion = None
            disanfang_city_proportion = None
            disanfang_area_proportion = None
            disanfang_personal_proportion = None
        else:
            buyer_province_proportion = proportion['储备池分佣']['省分佣比例']
            buyer_city_proportion = proportion['储备池分佣']['市分佣比例']
            buyer_area_proportion = proportion['储备池分佣']['区分佣比例']
            buyer_personal_proportion = proportion['储备池分佣']['个人分佣比例']

            disanfang_province_proportion = proportion['支付服务费分佣']['省分佣比例']
            disanfang_city_proportion = proportion['支付服务费分佣']['市分佣比例']
            disanfang_area_proportion = proportion['支付服务费分佣']['区分佣比例']
            disanfang_personal_proportion = proportion['支付服务费分佣']['个人分佣比例']

        # 计算出来的（商品价格，需要支付的易贝服务费，需要支付的现金服务费）（储备池分佣）（服务费分佣）
        calculation_data = Calculation(buyer_identity, seller_identity,
                                       buyer_province_proportion=buyer_province_proportion,
                                       buyer_city_proportion=buyer_city_proportion,
                                       buyer_area_proportion=buyer_area_proportion,
                                       buyer_personal_proportion=buyer_personal_proportion,
                                       disanfang_province_proportion=disanfang_province_proportion,
                                       disanfang_city_proportion=disanfang_city_proportion,
                                       disanfang_area_proportion=disanfang_area_proportion,
                                       disanfang_personal_proportion=disanfang_personal_proportion, ).transaction(ip,
                                                                                                                  member_level,
                                                                                                                  payment_method,
                                                                                                                  order,
                                                                                                                  charge_amount,
                                                                                                                  reserve_fund,user_id)

        return calculation_data
