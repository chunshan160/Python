#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/22 12:59
# @Author :春衫
# @File :boss_setting.py

from selenium import webdriver
from Web.Common import user_phone
from Web.Common.fengyong.API.Boss_setting_requests import boss_setting_requests


class BossSetting:

    def main(self, ip, surroundings, payment_method, superior, operational_setting):
        '''

        Parameters
        ----------
        ip
        surroundings：test/dev1/mtest
        payment_method
        superior
        operational_setting：[{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]

        Returns
        -------

        '''

        if payment_method in ["易贝", "易贝券"]:

            operational_setting_province_id = superior[1]["省代理商"]
            operational_setting_province_data = operational_setting["省代理商"]

            operational_setting_city_id = superior[1]["市代理商"]
            operational_setting_city_data = operational_setting["市代理商"]

            operational_setting_area_id = superior[1]["区代理商"]
            operational_setting_area_data = operational_setting["区代理商"]

            if operational_setting_province_id != None:
                phone = user_phone(ip,operational_setting_province_id)
                boss_setting_requests(surroundings, phone, operational_setting_province_data)

            if operational_setting_city_id != None:
                phone = user_phone(ip,operational_setting_city_id)
                boss_setting_requests(surroundings, phone, operational_setting_city_data)

            if operational_setting_area_id != None:
                phone = user_phone(ip,operational_setting_area_id)
                boss_setting_requests(surroundings, phone, operational_setting_area_data)
        else:

            reserve_fund_superior_province_id = superior["储备池分佣"][1]["省代理商"]
            reserve_fund_operational_setting_province_data = operational_setting["储备池分佣"]["省代理商"]

            reserve_fund_superior_city_id = superior["储备池分佣"][1]["市代理商"]
            reserve_fund_operational_setting_city_data = operational_setting["储备池分佣"]["市代理商"]

            reserve_fund_superior_area_id = superior["储备池分佣"][1]["区代理商"]
            reserve_fund_operational_setting_area_data = operational_setting["储备池分佣"]["区代理商"]

            if reserve_fund_superior_province_id != None:
                phone = user_phone(ip,reserve_fund_superior_province_id)
                boss_setting_requests(surroundings, phone, reserve_fund_operational_setting_province_data)

            if reserve_fund_superior_city_id != None:
                phone = user_phone(ip,reserve_fund_superior_city_id)
                boss_setting_requests(surroundings, phone, reserve_fund_operational_setting_city_data)

            if reserve_fund_superior_area_id != None:
                phone = user_phone(ip,reserve_fund_superior_area_id)
                boss_setting_requests(surroundings, phone, reserve_fund_operational_setting_area_data)

            service_fee_superior_province_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_province_data = operational_setting["支付服务费分佣"]["省代理商"]

            service_fee_superior_city_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_city_data = operational_setting["支付服务费分佣"]["省代理商"]

            service_fee_superior_area_id = superior["支付服务费分佣"][1]["省代理商"]
            service_fee_operational_setting_area_data = operational_setting["支付服务费分佣"]["省代理商"]

            if service_fee_superior_province_id != None:
                phone = user_phone(ip,service_fee_superior_province_id)
                boss_setting_requests(surroundings, phone, service_fee_operational_setting_province_data)

            if service_fee_superior_city_id != None:
                phone = user_phone(ip,service_fee_superior_city_id)
                boss_setting_requests(surroundings, phone, service_fee_operational_setting_city_data)

            if service_fee_superior_area_id != None:
                phone = user_phone(ip,service_fee_superior_area_id)
                boss_setting_requests(surroundings, phone, service_fee_operational_setting_area_data)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    ip = "192.168.0.101"
    operational_setting = {'省代理商': {'销售': 0.3, '业务焕商': 0, 'TCO': 0.3}, '市代理商': '未设置', '区代理商': '未设置'}
    superior = [{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]
