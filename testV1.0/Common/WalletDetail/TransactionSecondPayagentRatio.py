#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/7 17:31
#@Author :春衫
#@File :TransactionSecondPayagentRatio.py

from Common.WalletDetail.new_muban.second_payagent_ratio_data import second_payagent_ratio_data

class TransactionSecondPayagentRatio:
    
    def transaction_second_payagent_ratio(self,ip,payment_method,superior,data):
        platform_id = data['平台']
        # 生成易贝、抵工资、家人购流水模板
        if payment_method in ['易贝', '抵工资', '家人购']:

            if payment_method == "易贝":
                reserve_fund_bind_area_id = superior[1]['区代理商']
                reserve_fund_bind_city_id = superior[1]['市代理商']
                reserve_fund_bind_province_id = superior[1]['省代理商']
                service_fee_bind_area_id = superior[1]['区代理商']
                service_fee_bind_city_id = superior[1]['市代理商']
                service_fee_bind_province_id = superior[1]['省代理商']

            # 抵工资 家人购
            else:
                service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
                service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
                service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']
                reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
                reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
                reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']

        # 生成易贝券流水模板
        elif payment_method == "易贝券":
            reserve_fund_bind_area_id = superior[1]['区代理商']
            reserve_fund_bind_city_id = superior[1]['市代理商']
            reserve_fund_bind_province_id = superior[1]['省代理商']

        # 生成现金账户、微信、支付宝流水模板
        else:
            reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
            reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
            reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']
            service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
            service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
            service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']

        # 获取这笔订单应该【使用】的二级分佣比例
        reserve_fund_second_payagent_ratio = second_payagent_ratio_data(ip, reserve_fund_bind_province_id,
                                                                        reserve_fund_bind_city_id,
                                                                        reserve_fund_bind_area_id,
                                                                        platform_id)
        if payment_method == "易贝券":
            # 交易服务费二级分佣比例
            transaction_second_payagent_ratio = {"储备金二级分佣比例": reserve_fund_second_payagent_ratio,
                                                 "支付服务费二级分佣比例": None}


        if payment_method != "易贝券":
            # 获取出钱方所使用的二级分佣比例
            service_fee_second_payagent_ratio = second_payagent_ratio_data(ip, service_fee_bind_province_id,
                                                                           service_fee_bind_city_id,
                                                                           service_fee_bind_area_id,
                                                                           platform_id)

            # 交易服务费二级分佣比例
            transaction_second_payagent_ratio = {"储备金二级分佣比例": reserve_fund_second_payagent_ratio,
                                                 "支付服务费二级分佣比例": service_fee_second_payagent_ratio}

        return transaction_second_payagent_ratio