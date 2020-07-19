#!/usr/bin/envpython
# -*-coding:utf-8-*-
# @Time:2020/4/2616:43
# @Author:春衫
# @File:test_superior.py


from Do_mysql.sql import SQL
from DoExcel.do_excel import DoExcel
from tools.project_path import *
from shangji.superior import Superior
from decimal import *


class SuperiorTemplate:

    # superior
    def superior_template(self, ip, payment_method, data, sheet_name, case_id, phone_1, phone_2=None):
        '''

        :param payment_method: 支付方式
        :param data: data
        :param sheet_name: 表单
        :param case_id: 用例id
        :param phone_1: 手机号 易贝 易贝券
        :param phone_2: 手机号 其余支付方式 需要考虑卖家/家人/企业
        :return: 写回Excel的上级城市焕商/代理商id模板
        '''

        if payment_method in ["易贝", "易贝券"]:
            buyer_phone = eval(data)['buyer_phone']
            buyer_regional_agent = SQL(ip).regional_agent(buyer_phone)  # 查询买家上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            b = buyer_superior
            DoExcel.superior(test_case_path, sheet_name, case_id, str(b))
            return b

        elif payment_method in ["抵工资", "家人购"]:
            buyer_phone = eval(data)['buyer_phone']
            disanfang_phone = eval(data)['disanfang_phone']
            buyer_regional_agent = SQL(ip).regional_agent(buyer_phone)  # 查询买家上级
            disanfang_regional_agent = SQL(ip).regional_agent(disanfang_phone)  # 查询企业/家人上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            disanfang_superior = Superior().superior(ip, disanfang_regional_agent, phone_2)
            b = {"储备池分佣": buyer_superior, "支付服务费分佣": disanfang_superior}
            DoExcel.superior(test_case_path, sheet_name, case_id, str(b))
            return b

        else:  # 现金
            buyer_phone = eval(data)['buyer_phone']
            seller_phone = eval(data)['seller_phone']
            buyer_regional_agent = SQL(ip).regional_agent(buyer_phone)  # 查询买家上级
            seller_regional_agent = SQL(ip).regional_agent(seller_phone)  # 查询卖家上级
            buyer_superior = Superior().superior(ip, buyer_regional_agent, phone_1)
            seller_superior = Superior().superior(ip, seller_regional_agent, phone_2)
            b = {"储备池分佣": buyer_superior, "支付服务费分佣": seller_superior}
            DoExcel.superior(test_case_path, sheet_name, case_id, str(b))
            return b

    # proportion
    def fenyong_template(self, ip, payment_method, sheet_name, case_id, province1_id, city1_id, area1_id, personal1_id,
                         province2_id=None, city2_id=None, area2_id=None, personal2_id=None):
        '''

        :param ip:数据库的地址
        :param payment_method:支付方式
        :param sheet_name:表单名
        :param case_id:用例id
        :param province1_id:买家上级省代理商
        :param city1_id:买家上级市代理商
        :param area1_id:买家上级区代理商
        :param personal1_id:买家上级个人焕商
        :param province2_id:卖家上级省代理商
        :param city2_id:卖家上级市代理商
        :param area2_id:卖家上级区代理商
        :param personal2_id:卖家上级个人焕商
        :return: 写回Excel的上级城市焕商/代理商分佣比例模板
        '''

        if payment_method in ["易贝", "易贝券"]:
            buyer_fenyong = Superior().fenyong(ip, province1_id, city1_id, area1_id, personal1_id)
            if buyer_fenyong == None:
                buyer_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}
            b = buyer_fenyong
            DoExcel.fenyong_bili(test_case_path, sheet_name, case_id, str(b))

        elif payment_method in ["抵工资", "家人购"]:
            buyer_fenyong = Superior().fenyong(ip, province1_id, city1_id, area1_id, personal1_id)
            if buyer_fenyong == None:
                buyer_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            disanfang_fenyong = Superior().fenyong(ip, province2_id, city2_id, area2_id, personal2_id)
            if disanfang_fenyong == None:
                disanfang_fenyong = {'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            b = {"储备池分佣": buyer_fenyong, "支付服务费分佣": disanfang_fenyong}
            DoExcel.fenyong_bili(test_case_path, sheet_name, case_id, str(b))

        else:  # 现金

            buyer_fenyong = Superior().fenyong(ip, province1_id, city1_id, area1_id, personal1_id)
            if buyer_fenyong==None:
                buyer_fenyong={'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            seller_fenyong = Superior().fenyong(ip, province2_id, city2_id, area2_id, personal2_id)
            if seller_fenyong==None:
                seller_fenyong={'省分佣比例': None, '市分佣比例': None, '区分佣比例': None, '个人分佣比例': None}

            b = {"储备池分佣": buyer_fenyong, "支付服务费分佣": seller_fenyong}
            DoExcel.fenyong_bili(test_case_path, sheet_name, case_id, str(b))

        return b


if __name__ == '__main__':
    data = '{"buyer_phone":18888888888,"seller_phone":17777777774,"买家":1000419,"卖家":1000504,"平台":10}'
    a = SuperiorTemplate().superior_template("192.168.0.102", "现金", data, "焕商分佣_dev1", 5, 18888888888, 17777777774)
    print(a)
    # qqq={'储备池分佣': [{'个人焕商': None}, {'省代理商': 13691, '市代理商': 13947, '区代理商': 14453}], '支付服务费分佣': [{'个人焕商': None}, {'市代理商': 1000168, '省代理商': None, '区代理商': 1000169}]}
    # ww = SuperiorTemplate().fenyong_template("192.168.0.102", "现金", "焕商分佣_dev1", 5, 1000348, 1000284, 1000248, 1000504,None,
    #                                          15239, None, None)
    # print(ww)
