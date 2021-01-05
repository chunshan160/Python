#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/13 16:58
# @Author :春衫
# @File :cishu.py

class CiShu:

    def cishu(self, payment_method, superior):
        '''

        :param payment_method: 支付方式
        :param superior: 绑定关系
        :return:
        '''

        global personal, personal1, personal2

        if payment_method in ['易贝', '易贝券']:
            personal = superior[0]['个人焕商']  # 个人焕商
            if personal == None:
                personal = 0
            else:
                personal = 1

            regional_agent = len((superior[1]))

            if (superior[1])['省代理商'] == None:
                regional_agent -= 1
            if (superior[1])['市代理商'] == None:
                regional_agent -= 1
            if (superior[1])['区代理商'] == None:
                regional_agent -= 1

            cishu = [personal + regional_agent + 1]  # 加上平台
            return cishu

        else:  # 抵工资 家人购 现金
            personal1 = ((superior['储备池分佣'])[0])['个人焕商']  # 个人焕商
            personal2 = ((superior['支付服务费分佣'])[0])['个人焕商']  # 个人焕商
            regional_agent1 = len((superior['储备池分佣'])[1])
            a = (((superior)['储备池分佣'])[1])
            if a['省代理商'] == None:
                regional_agent1 -= 1
            if a['市代理商'] == None:
                regional_agent1 -= 1
            if a['区代理商'] == None:
                regional_agent1 -= 1

            regional_agent2 = len((superior['支付服务费分佣'])[1])
            b = ((superior['支付服务费分佣'])[1])
            if b['省代理商'] == None:
                regional_agent2 -= 1
            if b['市代理商'] == None:
                regional_agent2 -= 1
            if b['区代理商'] == None:
                regional_agent2 -= 1

            if personal1 == None:
                personal1 = 0
            else:
                personal1 = 1
            # print(regional_agent1)
            if personal2 == None:
                personal2 = 0
            else:
                personal2 = 1
            # print(regional_agent2)
            cishu1 = personal1 + regional_agent1 + 1
            cishu2 = personal2 + regional_agent2 + 1
            # print(cishu1, cishu2)
            return cishu1, cishu2  # cishu1是储备池  cishu2是服务费


if __name__ == '__main__':
    superior = [{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]

    a = CiShu().cishu("易贝", superior)
    print(a)
