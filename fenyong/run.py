#!/usr/bin/env python.txt
# -*- coding:utf-8 -*-
# @Time :2020/4/23 10:11
# @Author :春衫
# @File :run.py

from fenyong.recharge_service_fee import Dividend
from fenyong.payment_method import Pay
from fenyong.test_data import yibei as yb
from fenyong.test_data import xianjin as cash
from fenyong.test_data import *


class A:

    def b(self, province, city, area, personal, province_proportion=None, city_proportion=None, area_proportion=None,
          personal_proportion=None):
        '''

        :param a: 区代分佣比例
        :param b: 个人分佣比例
        :return:
        '''
        # 充值
        reserve_pool = 0  # 储备池金额
        recharge = 0  # 充值金额
        while True:
            choose = input("1、充值，2、结束")
            if choose == "1":
                recharge = float(input("输入充值金额："))
                reserve_pool_amount = Dividend(province, city, area, personal, province_proportion, city_proportion,
                                               area_proportion,
                                               personal_proportion).recharge(recharge)  # 返回的是每次充值存入储备池的金额
                reserve_pool = reserve_pool + reserve_pool_amount
                print("储备池金额是：%.2f" % reserve_pool)
            else:
                print("结束")
                break

        while True:
            print("---------------------分割线-------------------------")
            print("---------------------分割线-------------------------")
            print("---------------------分割线-------------------------")
            price = float(input("输入商品价格："))
            member_level = input("请输入会员等级：1、普通会员2、白银会员3、黄金会员4、铂金会员5、钻石会员")
            payment_method = input("选择支付方式：1、易贝，2、易贝券，3、抵工资，4、家人购，5、现金/微信/支付宝")

            if int(member_level) in [1, 2, 3, 4, 5] and int(payment_method) in [1, 2, 3, 4, 5]:
                print("选择的会员等级是：{0}".format(member_level_data[member_level]))
                print("选择的支付方式是：{0}".format(payment_method_data[payment_method]))

                if payment_method == "1":
                    service_fee_data = Pay().yibei(price, member_level_data[member_level])  # 通过调用方法返回的需要支付的易贝/现金服务费
                    print("----------------计算易贝服务费分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).yibei_service_fee(service_fee_data[0], yb[
                        member_level_data[member_level]])  # 调用方法计算易贝服务费分佣
                    print("----------------计算现金服务费（储备池）分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).cash_service_fee(recharge, reserve_pool, service_fee_data[1],
                                                                   cash[member_level_data[
                                                                       member_level]])  # 调用方法计算现金服务费分佣


                elif payment_method == "2":
                    service_fee_data = Pay().yibeiquan()  # 通过调用方法返回的需要支付的易贝/现金服务费
                    print("----------------计算现金服务费（储备池）分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).cash_service_fee(recharge, reserve_pool, service_fee_data,
                                                                   cash[member_level_data[
                                                                       member_level]])  # 调用方法计算现金服务费分佣


                elif payment_method == "3":
                    service_fee_data = Pay().digongzi(price, member_level_data[member_level])  # 通过调用方法返回的需要支付的易贝/现金服务费
                    print("----------------计算易贝服务费分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).yibei_service_fee(service_fee_data[0], yb[
                        member_level_data[member_level]])  # 调用方法计算易贝服务费分佣
                    print("----------------计算现金服务费（储备池）分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).cash_service_fee(recharge, reserve_pool, service_fee_data[1],
                                                                   cash[member_level_data[
                                                                       member_level]])  # 调用方法计算现金服务费分佣


                elif payment_method == "4":
                    service_fee_data = Pay().jiarengou(price, member_level_data[member_level])  # 通过调用方法返回的需要支付的易贝/现金服务费
                    print("----------------计算易贝服务费分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).yibei_service_fee(service_fee_data[0], yb[
                        member_level_data[member_level]])  # 调用方法计算易贝服务费分佣
                    print("----------------计算现金服务费（储备池）分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).cash_service_fee(recharge, reserve_pool, service_fee_data[1],
                                                                   cash[member_level_data[
                                                                       member_level]])  # 调用方法计算现金服务费分佣


                elif payment_method == "5":
                    service_fee_data = Pay().xianjin(price, member_level_data[member_level])  # 通过调用方法返回的需要支付的易贝/现金服务费
                    print("----------------计算现金服务费（储备池）分佣----------------")
                    Dividend(province, city, area, personal, province_proportion, city_proportion, area_proportion,
                             personal_proportion).cash_service_fee(recharge, reserve_pool, service_fee_data,
                                                                   cash[member_level_data[
                                                                       member_level]])  # 调用方法计算现金服务费分佣


            else:
                print("重新来吧！")
                break


if __name__ == '__main__':
    A().b(province=1000646, city=1000648, area=1000647, personal=1000650, province_proportion=None, city_proportion=0.6,
          area_proportion=0.5, personal_proportion=0.15)
