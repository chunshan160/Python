#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 12:48
# @Author :春衫
# @File :recharge_service_fee.py

from decimal import *
from tools.new_round import new_round
from tools.paixu import paixu


class Dividend:

    def __init__(self, buyer_identity, seller_identity, buyer_province_proportion, buyer_city_proportion,
                 buyer_area_proportion, buyer_personal_proportion,
                 disanfang_province_proportion=None, disanfang_city_proportion=None,
                 disanfang_area_proportion=None, disanfang_personal_proportion=None):
        '''
        :param buyer_identity: 买家身份
        :param seller_identity: 卖家身份
        :param province_proportion: 省代分佣比例
        :param city_proportion: 市代分佣比例
        :param area_proportion: 区代分佣比例
        :param personal_proportion: 个人焕商分佣比例
        '''

        self.buyer_identity = buyer_identity  # 买家身份 1公海用户 2非公海用户
        self.seller_identity = seller_identity  # 卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        self.buyer_province_proportion = buyer_province_proportion  # 省代分佣比例
        self.buyer_city_proportion = buyer_city_proportion  # 市代分佣比例
        self.buyer_area_proportion = buyer_area_proportion  # 区代分佣比例
        self.buyer_personal_proportion = buyer_personal_proportion  # 个人焕商分佣比例
        # 抵工资 家人购
        self.disanfang_province_proportion = disanfang_province_proportion  # 省代分佣比例
        self.disanfang_city_proportion = disanfang_city_proportion  # 市代分佣比例
        self.disanfang_area_proportion = disanfang_area_proportion  # 区代分佣比例
        self.disanfang_personal_proportion = disanfang_personal_proportion  # 个人焕商分佣比例

    # 充值
    def recharge(self, recharge, A=0.60):
        '''
        :param recharge: 充值服务费金额
        :param proportion: 充值到账比例
        :param A: 投放储备池比例
        :return M：公海用户存入储备池金额
        '''
        M = recharge * A  # 公海用户存入储备池金额 = 充值服务费金额 * 投放储备池比例
        N2 = self.buyer_area_proportion * (recharge - M)  # 区代理商所得分佣
        N3 = (self.buyer_city_proportion - self.buyer_area_proportion) * (recharge - M)  # 市代理商所得分佣
        N4 = (self.buyer_province_proportion - self.buyer_city_proportion) * (recharge - M)  # 省代理商所得分佣
        N5 = recharge - M - N2 - N3 - N4  # 平台所得分佣

        print("充值服务费金额是：%.2f" % (recharge))
        print("存入储备池金额是：%.2f * %.2f = %.2f" % (recharge, A, M))
        print("区代理商获得的现金交易分佣是：%.2f * %.2f = %.2f" % (self.buyer_area_proportion, (recharge - M), N2))
        print("市代理商获得的现金交易分佣是：%.2f * %.2f = %.2f" % (
            (self.buyer_city_proportion - self.buyer_area_proportion), (recharge - M), N3))
        print("省代理商获得的现金交易分佣是：%.2f * %.2f = %.2f" % (
            (self.buyer_province_proportion - self.buyer_city_proportion), (recharge - M), N4))
        print("平台所得充值分佣金额是：%.2f - %.2f - %.2f - %.2f = %.2f" % ((recharge - M), N2, N3, N4, N5))
        return M

    # 支付时应出易贝/现金服务费的分佣计算
    def pay_service_fee(self, payment_method, service_fee, service_fee_ratio):
        '''

        :param payment_method: 支付方式
        :param service_fee: 服务费
        :param service_fee_ratio: 服务费比例
        :return:
        '''
        global M1, M2, M3, M4, M5, a

        # 兼容 因为这几个支付方式逻辑和下面一样，就是传参的参数名不一样而已
        if payment_method in ["抵工资", "家人购", "现金", "支付宝", "微信"]:
            self.buyer_province_proportion = self.disanfang_province_proportion  # 省代分佣比例
            self.buyer_city_proportion = self.disanfang_city_proportion  # 市代分佣比例
            self.buyer_area_proportion = self.disanfang_area_proportion  # 区代分佣比例
            self.buyer_personal_proportion = self.disanfang_personal_proportion  # 个人焕商分佣比例

        print("服务费比例是：{0}".format(service_fee_ratio))
        print("买家是：{0}，卖家是：{1}".format(self.buyer_identity, self.seller_identity))
        if payment_method in ["现金", "微信", "支付宝"]:
            shenfen = "卖家"
        elif payment_method == "抵工资":
            shenfen = "企业"
        elif payment_method == "家人购":
            shenfen = "家人"
        else:
            shenfen = "买家"

        print("交易时{0}需要支付服务费是：{1}".format(shenfen, service_fee))
        print(
            f"{shenfen}上级省代理商分佣比例是：{self.buyer_province_proportion}，{shenfen}上级市代理商分佣比例是：{self.buyer_city_proportion}，"
            f"{shenfen}上级区代理商分佣比例是：{self.buyer_area_proportion}，{shenfen}绑定的个人焕商分佣比例是：{self.buyer_personal_proportion}")

        # 处理M1
        if self.buyer_personal_proportion == None:
            M1 = 0  # 个人所得分佣
            print("{0}没有绑定个人焕商，交易时个人焕商不会获得交易服务费分佣".format(shenfen))
        else:
            M1 = service_fee * self.buyer_personal_proportion  # 个人所得分佣
            M1 = new_round(float(M1), 2)
            M1 = Decimal(str(M1)).quantize(Decimal('0.00'))
            print("个人焕商获得得的服务费分佣是：{0} * {1} = {2}".format(service_fee, self.buyer_personal_proportion, M1))

        if self.buyer_province_proportion == None and self.buyer_city_proportion == None and self.buyer_area_proportion == None:
            M2 = 0
            print("该{0}没有上级区代理商，不会获得分佣。".format(shenfen))
            M3 = 0
            print("该{0}没有上级市代理商，不会获得分佣。".format(shenfen))
            M4 = 0
            print("该{0}没有上级省代理商，不会获得分佣。".format(shenfen))

        else:
            # 买家上级个人焕商分佣比例不为None 并且 个人焕商分佣 比例 大于 最小省/市/区分佣比例
            min_proportion = paixu(self.buyer_province_proportion, self.buyer_city_proportion,
                                   self.buyer_area_proportion)
            if self.buyer_personal_proportion != None and self.buyer_personal_proportion > min_proportion:
                print("使用算法二")

                if self.buyer_area_proportion == None:
                    M2 = 0
                    print("该{0}没有上级区代理商，不会获得分佣。".format(shenfen))
                else:
                    M2 = self.buyer_area_proportion * (service_fee - M1)  # 区代理商所得分佣
                    M2 = new_round(float(M2), 2)
                    M2 = Decimal(str(M2)).quantize(Decimal('0.00'))
                    print("区代理商获得的服务费分佣是：{0} * {1} = {2}".format(self.buyer_area_proportion, (service_fee - M1), M2))

                if self.buyer_city_proportion == None:
                    M3 = 0
                    print("该{0}没有上级市代理商，不会获得分佣。".format(shenfen))
                else:
                    if self.buyer_area_proportion == None:
                        self.buyer_area_proportion = 0
                        if self.buyer_personal_proportion == None:
                            self.buyer_personal_proportion = 0
                            a = self.buyer_province_proportion
                        else:
                            a = self.buyer_city_proportion - self.buyer_personal_proportion  # 如果区代为空，那么市代分佣比例得减去个人焕商
                    else:
                        a = self.buyer_city_proportion - self.buyer_area_proportion
                    M3 = a * (service_fee - M1)  # 市代理商所得分佣
                    M3 = new_round(float(M3), 2)
                    M3 = Decimal(str(M3)).quantize(Decimal('0.00'))
                    print("市代理商获得的服务费分佣是：{0} * {1} = {2}".format(new_round(float(a), 2), (service_fee - M1), M3))

                if self.buyer_province_proportion == None:
                    M4 = 0
                    print("该{0}没有上级省代理商，不会获得分佣。".format(shenfen))
                else:
                    if self.buyer_city_proportion == None:
                        self.buyer_city_proportion = 0
                        if self.buyer_area_proportion == None:  # 市代为空 区代也为空
                            self.buyer_area_proportion = 0
                            a = self.buyer_province_proportion - self.buyer_personal_proportion
                        else:
                            a = self.buyer_province_proportion - self.buyer_area_proportion
                    else:
                        a = self.buyer_province_proportion - self.buyer_city_proportion
                    M4 = a * (service_fee - M1)  # 省代理商所得分佣
                    M4 = new_round(float(M4), 2)
                    M4 = Decimal(str(M4)).quantize(Decimal('0.00'))
                    print("省代理商获得的服务费分佣是：{0} * {1} = {2}".format(new_round(float(a), 2), (service_fee - M1), M4))

            else:
                print("使用算法一")

                if self.buyer_area_proportion == None:
                    M2 = 0
                    print("该{0}没有上级区代理商，不会获得分佣。".format(shenfen))
                else:
                    if self.buyer_personal_proportion == None:
                        a = self.buyer_area_proportion
                    else:
                        a = self.buyer_area_proportion - self.buyer_personal_proportion

                    M2 = a * service_fee  # 区代理商所得分佣
                    M2 = new_round(float(M2), 2)
                    M2 = Decimal(str(M2)).quantize(Decimal('0.00'))
                    print("区代理商获得的服务费分佣是：{0} * {1} = {2}".format(new_round(float(a), 2), service_fee, M2))

                if self.buyer_city_proportion == None:
                    M3 = 0
                    print("该{0}没有上级市代理商，不会获得分佣。".format(shenfen))
                else:
                    if self.buyer_area_proportion == None:
                        self.buyer_area_proportion = 0
                        if self.buyer_personal_proportion == None:
                            a = self.buyer_city_proportion
                        else:
                            a = self.buyer_city_proportion - self.buyer_personal_proportion  # 如果区代为空，那么市代分佣比例得减去个人焕商
                    else:
                        a = self.buyer_city_proportion - self.buyer_area_proportion

                    M3 = a * service_fee  # 市代理商所得分佣
                    M3 = new_round(float(M3), 2)
                    M3 = Decimal(str(M3)).quantize(Decimal('0.00'))
                    print("市代理商获得的服务费分佣是：{0} * {1} = {2}".format(new_round(float(a), 2), service_fee, M3))

                if self.buyer_province_proportion == None:
                    M4 = 0
                    print("该{0}没有上级省代理商，不会获得分佣。".format(shenfen))
                else:
                    if self.buyer_city_proportion == None:
                        self.buyer_city_proportion = 0
                        if self.buyer_area_proportion == None:  # 市代为空 区代也为空
                            self.buyer_area_proportion = 0
                            if self.buyer_personal_proportion == None:
                                a = self.buyer_province_proportion
                            else:
                                a = self.buyer_province_proportion - self.buyer_personal_proportion
                        else:
                            a = self.buyer_province_proportion - self.buyer_area_proportion
                    else:
                        a = self.buyer_province_proportion - self.buyer_city_proportion

                    M4 = a * service_fee  # 省代理商所得分佣
                    M4 = new_round(float(M4), 2)
                    M4 = Decimal(str(M4)).quantize(Decimal('0.00'))
                    print("省代理商获得的服务费分佣是：{0} * {1} = {2}".format(new_round(float(a), 2), service_fee, M4))

        M5 = service_fee - M1 - M2 - M3 - M4  # 平台所得分佣
        M5 = new_round(float(M5), 2)
        M5 = Decimal(str(M5)).quantize(Decimal('0.00'))
        print("平台获得的服务费分佣是：{0} - {1} - {2} - {3} - {4} = {5}".format(service_fee, M1, M2, M3, M4, M5))

        return M1, M2, M3, M4, M5

    # 储备池分佣算法
    def cash_service_fee(self, charge_amount, reserve_pool):
        '''
        :param recharge：充值金额
        :param reserve_pool: 储备池的金额
        :return:个人所得分佣、省市区、平台所得分佣
        '''

        global M1, M2, M3, M4, M5, cash_service_fee, a
        print("储备池金额是：%.2f" % (reserve_pool))
        print("----------开始计算储备池分佣----------")
        print(f"买家上级省代理商分佣比例是：{self.buyer_province_proportion}，买家上级市代理商分佣比例是：{self.buyer_city_proportion}，"
              f"买家上级区代理商分佣比例是：{self.buyer_area_proportion}，买家绑定的个人焕商分佣比例是：{self.buyer_personal_proportion}")

        M1 = charge_amount * self.buyer_personal_proportion  # 个人焕商应得金额
        M1 = new_round(float(M1), 2)
        M1 = Decimal(str(M1)).quantize(Decimal('0.00'))
        print("个人焕商获得得的现金交易分佣是：{0} * {1} = {2}".format(charge_amount, self.buyer_personal_proportion, M1))

        if self.buyer_province_proportion == None and self.buyer_city_proportion == None and self.buyer_area_proportion:
            M2 = 0
            M3 = 0
            M4 = 0
            if reserve_pool > M1:
                M5 = reserve_pool - M1
            else:
                M5 = 0
        else:
            # 储备池金额>个人焕商应得金额
            if reserve_pool > M1:


                if self.buyer_area_proportion == None:
                    M2 = 0
                    print("该买家没有上级区代理商，不会获得分佣。")
                else:
                    a = self.buyer_area_proportion * (reserve_pool - M1)  # 区代理商所得分佣
                    M2 = new_round(float(a), 2)
                    M2 = Decimal(str(M2)).quantize(Decimal('0.00'))
                    print("区代理商获得的现金交易分佣是：{0} * {1} = {2}".format(self.buyer_area_proportion, (reserve_pool - M1), M2))

                if self.buyer_city_proportion == None:
                    M3 = 0
                    print("该买家没有上级市代理商，不会获得分佣。")
                else:
                    if self.buyer_area_proportion == None:
                        self.buyer_area_proportion = 0
                        a = self.buyer_city_proportion
                    else:
                        a = self.buyer_city_proportion - self.buyer_area_proportion
                    M3 = new_round(float(a), 2)
                    M3 = M3 * float(reserve_pool - M1)  # 区代理商所得分佣
                    M3 = new_round(float(M3), 2)
                    M3 = Decimal(str(M3)).quantize(Decimal('0.00'))
                    print("市代理商获得的现金交易分佣是：{0} * {1} = {2}".format(a, (reserve_pool - M1), M3))

                if self.buyer_province_proportion == None:
                    M4 = 0
                    print("该买家没有上级省代理商，不会获得分佣。")
                else:
                    if self.buyer_city_proportion == None:
                        self.buyer_city_proportion = 0
                        if self.buyer_area_proportion == None:  # 市代为空 区代也为空
                            a = self.buyer_province_proportion
                        else:
                            a = self.buyer_province_proportion - self.buyer_area_proportion
                    else:
                        a = self.buyer_province_proportion - self.buyer_city_proportion
                    M4 = new_round(float(a), 2)
                    M4 = M4 * float(reserve_pool - M1)  # 区代理商所得分佣
                    M4 = new_round(float(M4), 2)
                    M4 = Decimal(str(M4)).quantize(Decimal('0.00'))
                    print("省代理商获得的现金交易分佣是：{0} * {1} = {2}".format(a, (reserve_pool - M1), M4))

                M5 = reserve_pool - M1 - M2 - M3 - M4  # 平台所得分佣
                M5 = new_round(float(M5), 2)
                M5 = Decimal(str(M5)).quantize(Decimal('0.00'))
                print("平台获得的现金交易分佣是：{0} - {1} - {2} - {3} - {4} = {5}".format(
                    reserve_pool, M1, M2, M3, M4, M5))

            elif reserve_pool <= M1:
                M1 = reserve_pool  # 全给个人焕商
                M2 = Decimal(str(0)).quantize(Decimal('0.00'))
                M3 = Decimal(str(0)).quantize(Decimal('0.00'))
                M4 = Decimal(str(0)).quantize(Decimal('0.00'))
                M5 = Decimal(str(0)).quantize(Decimal('0.00'))
                print(f"储备池金额小于等于个人焕商应得金额，所以储备金全部分给个人焕商，个人焕商获得的储备池分佣是：{reserve_pool}")
                print("省市区平台获得的储备池分佣全部为0")


        return M1, M2, M3, M4, M5


if __name__ == '__main__':
    pass

    uuu = Dividend("公海用户", "个人焕商", buyer_province_proportion=0.8, buyer_city_proportion=0.7, buyer_area_proportion=0.6,
                   buyer_personal_proportion=0.15).pay_service_fee(1, 0.10, 0.01)
    # print(uuu)
    print("---------------------我是分割线----------------------------")
    a = Dividend("公海用户", "个人焕商", buyer_province_proportion=0.8, buyer_city_proportion=0.7, buyer_area_proportion=0.6,
                 buyer_personal_proportion=0.15).cash_service_fee(100, 60)
    # print(a)
