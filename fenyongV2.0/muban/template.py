#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/28 10:10
# @Author :春衫
# @File :expected_changes.py

from Do_mysql.sql import SQL
from decimal import *
from Calculation.calculation import A
from DoExcel.do_excel import DoExcel
from tools.project_path import *
from muban.title import Title
from tools.quchong import quchong

test_data = DoExcel.get_data(test_case_path)


class GeShiHua:

    def __init__(self, buyer_identity, seller_identity, member_level, payment_method, order):
        '''

        :param buyer_identity:  买家身份 1公海用户 2非公海用户
        :param seller_identity:  卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        :param member_level: 会员等级
        :param payment_method:支付方式
        :param order: 订单号
        '''

        self.buyer_identity = buyer_identity  # 买家身份 1公海用户 2非公海用户
        self.seller_identity = seller_identity  # 卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        self.member_level = member_level
        self.payment_method = payment_method
        self.order = order

    def userid(self, data, superior):

        global d, i, j, k, l, h
        if self.payment_method in ['抵工资', '家人购']:

            d = data['出钱方']
            e = superior['支付服务费分佣'][0]['个人焕商']
            f = superior['支付服务费分佣'][1]['区代理商']
            g = superior['支付服务费分佣'][1]['市代理商']
            h = superior['支付服务费分佣'][1]['省代理商']
            i = superior['储备池分佣'][0]['个人焕商']
            j = superior['储备池分佣'][1]['区代理商']
            k = superior['储备池分佣'][1]['市代理商']
            l = superior['储备池分佣'][1]['省代理商']

        elif self.payment_method in ['现金', '微信', '支付宝']:
            # 现金服务费给卖家上级，储备池分佣给买家上级
            e = superior['支付服务费分佣'][0]['个人焕商']
            f = superior['支付服务费分佣'][1]['区代理商']
            g = superior['支付服务费分佣'][1]['市代理商']
            h = superior['支付服务费分佣'][1]['省代理商']
            i = superior['储备池分佣'][0]['个人焕商']
            j = superior['储备池分佣'][1]['区代理商']
            k = superior['储备池分佣'][1]['市代理商']
            l = superior['储备池分佣'][1]['省代理商']

        else:  # 易贝、易贝券

            d = superior[0]['个人焕商']
            e = superior[1]['区代理商']
            f = superior[1]['市代理商']
            g = superior[1]['省代理商']

        a = data['买家']
        b = data['卖家']
        c = data['平台']
        if self.payment_method == '易贝':
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                userid = [a, a, a, c, c, c, c, b, a, d, e, f, g, c, c, d, e, f, g, c]


            elif self.buyer_identity == "公海用户":
                userid = [a, a, a, c, c, c, c, b, c, e, f, g, c]

            else:  # 非公海用户 个人焕商不可能为空
                userid = [a, a, a, c, c, c, c, b, a, d, e, f, g, c]


        elif self.payment_method == '易贝券':
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                userid = [a, c, c, b, a, d, e, f, g, c]

            else:
                userid = [a, c, c, b]

        elif self.payment_method in ['抵工资', '家人购']:  # 抵工资和家人购跟买家身份关系不大
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):  # 这里应该理解为企业/家人是公海用户，卖家是个人焕商
                userid = [d, d, d, c, c, c, c, b,
                          a,
                          i, j, k, l, c,
                          c,
                          e, f, g, h, c]  # 企业/家人上级个人、省市区、平台id
            else:
                userid = [d, d, d, c, c, c, c, b,
                          c,
                          e, f, g, h, c]  # 企业上级个人、省市区、平台id

        else:  # 现金账户、微信、支付宝
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                userid = [a, c, c, c, b, b,
                          a,
                          i, j, k, l, c,  # 储备池买家上级个人、省市区、平台id
                          c,
                          e, f, g, h, c]  # 卖家上级个人、省市区、平台id
            else:
                userid = [a, c, c, c, b, b,
                          c,
                          e, f, g, h, c]  # 卖家上级个人、省市区、平台id
        userid = quchong(userid, None)  # 去掉为None的列表
        return userid

    def expected_changes(self,ip, calculation, reserve_fund=None):  # 预期变化值
        '''

        :param charge_amount:未消耗充值金额
        :param reserve_fund:储备池金额
        :return:变化的金额
        '''

        global iii
        sql_data = SQL(ip).wallet_detail(self.order)  # 支付数据

        if self.payment_method in ['易贝', '抵工资', '家人购']:
            a = (sql_data[0])[3]  # 读取的商品价格
            b = (calculation[0])[1]  # 买家应出易贝服务费
            c = (calculation[0])[2]  # 买家应出现金服务费

            if self.payment_method == "易贝":

                d = (calculation[1])[0]  # 储备池买家上级个人焕商分佣
                e = (calculation[1])[1]  # 储备池买家上级区代理商分佣
                f = (calculation[1])[2]  # 储备池买家上级市代理商分佣
                g = (calculation[1])[3]  # 储备池买家上级省代理商分佣
                h = (calculation[1])[4]  # 储备池平台分佣

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    i = (calculation[2])[0]  # 易贝服务费买家上级个人焕商分佣
                    j = (calculation[2])[1]  # 易贝服务费买家上级区代理商分佣
                    k = (calculation[2])[2]  # 易贝服务费买家上级市代理商分佣
                    l = (calculation[2])[3]  # 易贝服务费买家上级省代理商分佣
                    m = (calculation[2])[4]  # 易贝服务费平台分佣
                    iii = [a, b * -1, c * -1, a * -1,
                           b,
                           c, a, a * -1, reserve_fund * -1,
                           d,
                           e, f, g, h,
                           b * -1,
                           i, j, k, l, m]

                elif self.buyer_identity == "公海用户":
                    # i = (calculation[1])[0]  # 易贝服务费买家上级个人焕商分佣
                    j = (calculation[1])[1]  # 易贝服务费买家上级区代理商分佣
                    k = (calculation[1])[2]  # 易贝服务费买家上级市代理商分佣
                    l = (calculation[1])[3]  # 易贝服务费买家上级省代理商分佣
                    m = (calculation[1])[4]  # 易贝服务费平台分佣
                    iii = [a, b * -1, c * -1, a * -1,
                           b,
                           c, a, a * -1,
                           b * -1,
                           j, k, l, m]
                else:
                    i = (calculation[1])[0]  # 易贝服务费买家上级个人焕商分佣
                    j = (calculation[1])[1]  # 易贝服务费买家上级区代理商分佣
                    k = (calculation[1])[2]  # 易贝服务费买家上级市代理商分佣
                    l = (calculation[1])[3]  # 易贝服务费买家上级省代理商分佣
                    m = (calculation[1])[4]  # 易贝服务费平台分佣
                    iii = [a, b * -1, c * -1, a * -1,
                           b,
                           c, a, a * -1,
                           b * -1,
                           i, j, k, l, m]

            else:  # 抵工资、家人购
                d = (calculation[1])[0]  # 储备池买家上级个人焕商分佣
                e = (calculation[1])[1]  # 储备池买家上级区代理商分佣
                f = (calculation[1])[2]  # 储备池买家上级市代理商分佣
                g = (calculation[1])[3]  # 储备池买家上级省代理商分佣
                h = (calculation[1])[4]  # 储备池平台分佣

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    i = (calculation[2])[0]  # 易贝服务费买家上级个人焕商分佣
                    j = (calculation[2])[1]  # 易贝服务费买家上级区代理商分佣
                    k = (calculation[2])[2]  # 易贝服务费买家上级市代理商分佣
                    l = (calculation[2])[3]  # 易贝服务费买家上级省代理商分佣
                    m = (calculation[2])[4]  # 易贝服务费平台分佣

                    iii = [a, b * -1, c * -1, a * -1,
                           b, c,
                           a, a * -1,
                           reserve_fund * -1,
                           d, e, f, g, h,
                           b * -1,
                           i, j, k, l, m]
                    # print("iii",iii)

                else:
                    i = (calculation[1])[0]  # 易贝服务费买家上级个人焕商分佣
                    j = (calculation[1])[1]  # 易贝服务费买家上级区代理商分佣
                    k = (calculation[1])[2]  # 易贝服务费买家上级市代理商分佣
                    l = (calculation[1])[3]  # 易贝服务费买家上级省代理商分佣
                    m = (calculation[1])[4]  # 易贝服务费平台分佣
                    iii = [a, b * -1, c * -1, a * -1,
                           b, c,
                           a, a * -1,
                           b * -1,
                           i, j, k, l, m]

        elif self.payment_method == '易贝券':
            a = (sql_data[0])[3]  # 读取的商品价格
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                b = calculation[0]  # 计算用的商品价格
                d = (calculation[1])[0]  # 储备池买家上级个人焕商分佣
                e = (calculation[1])[1]  # 储备池买家上级区代理商分佣
                f = (calculation[1])[2]  # 储备池买家上级市代理商分佣
                g = (calculation[1])[3]  # 储备池买家上级省代理商分佣
                h = (calculation[1])[4]  # 储备池平台分佣
                iii = [a, b, b * -1, b,
                       reserve_fund * -1,
                       d,
                       e, f, g, h]
                # print("易贝券")
            else:
                b = calculation  # 计算用的商品价格
                iii = [a, b, b * -1, b]

        else:  # 现金
            a = (sql_data[0])[3]  # 读取的商品价格
            b = (calculation[0])[0]  # 计算得到的商品价格
            c = (calculation[0])[1]  # 卖家需要支付的现金服务费
            o = b - c  # 卖家实际应收到的金额

            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):

                d = (calculation[1])[0]  # 储备池买家上级个人焕商分佣
                e = (calculation[1])[1]  # 储备池买家上级区代理商分佣
                f = (calculation[1])[2]  # 储备池买家上级市代理商分佣
                g = (calculation[1])[3]  # 储备池买家上级省代理商分佣
                h = (calculation[1])[4]  # 储备池平台分佣

                i = (calculation[2])[0]  # 现金服务费卖家上级个人焕商分佣
                j = (calculation[2])[1]  # 现金服务费卖家上级区代理商分佣
                k = (calculation[2])[2]  # 现金服务费卖家上级市代理商分佣
                l = (calculation[2])[3]  # 现金服务费卖家上级省代理商分佣
                m = (calculation[2])[4]  # 现金服务费平台分佣
                iii = [a, o, c, o * -1,
                       b,
                       c * -1, reserve_fund * -1,
                       d, e, f, g, h,
                       c * -1,
                       i, j, k, l, m]
            else:
                i = (calculation[1])[0]  # 现金服务费卖家上级个人焕商分佣
                j = (calculation[1])[1]  # 现金服务费卖家上级区代理商分佣
                k = (calculation[1])[2]  # 现金服务费卖家上级市代理商分佣
                l = (calculation[1])[3]  # 现金服务费卖家上级省代理商分佣
                m = (calculation[1])[4]  # 现金服务费平台分佣

                iii = [a, o, c, o * -1, b,
                       c * -1,
                       c * -1,
                       i, j, k, l, m]

        # 精华 我把分佣等于0的值去掉 就意味不分佣给这些人
        iii = quchong(iii, 0)
        return iii

    def expected(self,ip,calculation, data, superior,reserve_fund=None):
        '''

        :param charge_amount:未消耗充值金额
        :param reserve_fund:储备池金额
        :param data: 手机号、id
        :param superior:上级代理商/城市焕商
        :param buyer_province_proportion:买家上级省代理商
        :param buyer_city_proportion:买家上级市代理商
        :param buyer_area_proportion:买家上级区代理商
        :param buyer_personal_proportion:买家上级个人焕商
        :param disanfang_province_proportion:企业/家人上级省代理商
        :param disanfang_city_proportion:企业/家人上级市代理商
        :param disanfang_area_proportion:企业/家人上级区代理商
        :param disanfang_personal_proportion:企业/家人上级个人焕商
        :return:预期流水模板
        '''

        sql_data = SQL(ip).wallet_detail(self.order)  # 支付数据

        user_id = GeShiHua(self.buyer_identity, self.seller_identity, self.member_level, self.payment_method,
                           self.order).userid(data, superior)
        # print("userid", user_id)

        expected_changes = GeShiHua(self.buyer_identity, self.seller_identity, self.member_level,
                                    self.payment_method, self.order).expected_changes(ip,calculation,reserve_fund)  # 格式化之后的changes
        # print("expected_changes", expected_changes)
        biz_type = (GeShiHua(self.buyer_identity, self.seller_identity, self.member_level, self.payment_method,
                             self.order).fanhui(ip,superior))[1]

        category = (GeShiHua(self.buyer_identity, self.seller_identity, self.member_level, self.payment_method,
                             self.order).fanhui(ip,superior))[3]

        # 控制流水条数
        shuju = Title(self.buyer_identity, self.seller_identity, self.payment_method).title(superior)
        # print(shuju)
        # print(len(shuju))

        bbb = []
        for i in range(0, len(shuju)):
            a1 = user_id[i]
            a3 = biz_type[i]
            a4 = expected_changes[i]
            a6 = (sql_data[i])[5]
            a5 = a6 + a4
            a8 = category[i]
            aaa = (a1, 2, a3, a4, a5, a6, shuju[i], a8)
            bbb.append(aaa)
            # print("i", i)
        # print("bbb", bbb)
        bbb=tuple(bbb)
        return bbb

    def fanhui(self,ip, superior):  # 以后写回Excel对比用
        '''

        :param superior: 上级代理商/城市焕商
        :return: user_id, biz_type, changes, category
        '''
        sql_data = SQL(ip).wallet_detail(self.order)  # 支付数据
        global a, b
        user_id = []
        biz_type = []
        changes = []
        category = []
        shuju = Title(self.buyer_identity, self.seller_identity, self.payment_method).title(superior)
        # print("shuju", shuju)
        # print(len(shuju))
        for i in range(0, len(shuju)):
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


if __name__ == '__main__':
    pass

    # data = {"buyer_phone": "17777777781", "买家": 1000656, "卖家": 1000650, "平台": 10}
    # superior = {'储备池分佣': [{'个人分佣比例': 0.15}, {'省分佣比例': 0.8, '市分佣比例': 0.7, '区分佣比例': 0.6}],
    #             '支付服务费分佣': [{'个人分佣比例': None}, {'市分佣比例': 0.7, '区分佣比例': 0.6, '省分佣比例': 0.8}]}
    # # yyy = GeShiHua('公海用户', '个人焕商', '钻石会员', '易贝', 'EC-2020051318493700011645').userid(data, superior)
    # # print(yyy)
    # # print('---------')
    # ggg = GeShiHua('公海用户', '个人焕商', '钻石会员', '抵工资', 'EC-2020051318493700011645').expected_changes(Decimal('200'),
    #                                                                                             Decimal('120.00'), 0.8,
    #                                                                                             0.7, 0.6, 0.15,
    #                                                                                             disanfang_province_proportion=0.8,
    #                                                                                             disanfang_city_proportion=0.7,
    #                                                                                             disanfang_area_proportion=0.6,
    #                                                                                             disanfang_personal_proportion=None)
    # print(ggg)
    # # print('---------')
    # data = {'buyer_phone': '17777777781', '买家': '1000656', '卖家': '1000650', '平台': '10', '个人焕商': '1000650'}
    # superior = {'省代理商': '1000646', '市代理商': '1000647', '区代理商': '1000648'}
    # phone = '1000656'

    # qqq = GeShiHua("公海用户", "个人焕商", '钻石会员', '易贝', 'EC-2020051418331100011709').expected(0.8, 0.7, 0.6, 0.15, data,
    #                                                                                    superior, 17777777781,
    #                                                                                    '1000656', Decimal('100'),
    #                                                                                    Decimal('60.00'))
    #
    # print("qqq", qqq)
    # sql_data = SQL(ip).wallet_detail("EC-2020051418331100011709")
    # for i in range(0, 20):
    #     if qqq[i] == sql_data[i]:
    #         print('true')
    #         print(i)
    #     else:
    #         print("false")
    #         print(i)
    # print('---------')
    # ooo = GeShiHua("公海用户", "个人焕商", '钻石会员', '易贝', 'EC-2020051318493700011645').fanhui(superior)
    # print(ooo)

    # print('---------')
    # 公海用户,个人焕商,钻石会员,易贝,EC - 2020050915075800011067
    # 0.8,0.7,0.6,0.6
    # {'buyer_phone': '17777777781', '买家': '1000656', '卖家': '1000650', '平台': '10', '个人焕商': '1000650'}
    # {'省代理商': '1000646', '市代理商': '1000647', '区代理商': '1000648'}
    # 17777777781

    # print("-------------------------")
    # # # print(yibei_data2)
    # sql_data = SQL(ip).wallet_detail("EC-2020051220235000011607")
    # print('sql_data:', sql_data)
    # shuju = Title("公海用户", "个人焕商", "钻石会员", "易贝").title(17777777781)
    # print(len(shuju))
    # for i in range(0, len(shuju)):
    #     if qqq[i] == sql_data[i]:
    #         print('true')
    #         print(i)
    #     else:
    #         print("false")
    #         print(i)

    # ooo = GeShiHua(1, 1, '钻石会员', '易贝券').fanhui()
    # print(ooo)
    # print('---------')
    # yyy = GeShiHua(1, 1, '钻石会员', '易贝券').userid()
    # print(yyy)
    # print('---------')
    # ggg = GeShiHua(1, 1, '钻石会员', '易贝券').expected_changes()
    # print(ggg)
    # print('---------')
    # qqq = GeShiHua(1, 1, '钻石会员', '易贝券').expected()
    # print(qqq)
    #
    # if qqq == yibeiquan_data:
    #     print('true')

    # ooo = GeShiHua(1, 2, '钻石会员', '抵工资').fanhui()
    # print(ooo)
    # print('---------')
    # yyy = GeShiHua(1, 2, '钻石会员', '抵工资').userid()
    # print(yyy)
    # print('---------')
    # ggg = GeShiHua(1, 2, '钻石会员', '抵工资').expected_changes()
    # print(ggg)
    # print('---------')
    # qqq = GeShiHua(1, 2, '钻石会员', '抵工资').expected()
    # print(qqq)
    #
    # if qqq == digongzi_data2:
    #     print('true')
    #
    # ooo = GeShiHua(1, 2, '白银会员', '现金账户').fanhui()
    # print(ooo)
    # print('---------')
    # yyy = GeShiHua(1, 2, '钻石会员', '现金账户').userid()
    # print(yyy)
    # print('---------')
    # ggg = GeShiHua(1, 2, '白银会员', '现金账户').expected_changes()
    # print(ggg)
    # # # print('---------')
    # qqq = GeShiHua(1, 2, '普通会员', '现金账户').expected()
    # print(qqq)
    # print("------------")

    # print(xianjin_data2)
    # if qqq == xianjin_data2:
    #     print('true')
    # else:
    #     print('false')
