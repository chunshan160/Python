#!/usr/bin/env python.txt
# -*- coding:utf-8 -*-
# @Time :2020/4/10 12:48
# @Author :春衫
# @File :recharge_service_fee.py


class Dividend:

    def __init__(self, province, city, area, personal, province_proportion=None, city_proportion=None,
                 area_proportion=None,
                 personal_proportion=None):
        '''
        :param province_proportion: 省代分佣比例
        :param city_proportion: 市代分佣比例
        :param area_proportion: 区代分佣比例
        :param personal_proportion: 个人焕商分佣比例
        '''
        # if province_proportion == None:
        #     self.province_proportion = 0
        # else:
        self.province = province  # 省代分佣比例
        self.city = city  # 市代分佣比例
        self.area = area  # 区代分佣比例
        self.personal = personal  # 个人焕商分佣比例
        self.province_proportion = province_proportion  # 省代分佣比例
        self.city_proportion = city_proportion  # 市代分佣比例
        self.area_proportion = area_proportion  # 区代分佣比例
        self.personal_proportion = personal_proportion  # 个人焕商分佣比例

    # 充值
    def recharge(self, recharge, proportion=2.8, A=0.65):
        '''
        :param recharge: 充值服务费金额
        :param proportion: 充值到账比例
        :param A: 投放储备池比例
        :return M：公海用户存入储备池金额
        '''
        R1 = recharge * proportion  # 服务费余额 = 充值服务费金额 * 充值到账比例
        M = recharge * A  # 公海用户存入储备池金额 = 充值服务费金额 * 投放储备池比例

        N2 = self.area_proportion * (recharge - M)  # 区代焕商所得分佣
        N3 = (self.city_proportion - self.area_proportion) * (recharge - M)  # 市代焕商所得分佣
        if self.province_proportion == None:
            N4 = 0
        else:
            N4 = (self.province_proportion - self.city_proportion) * (recharge - M)  # 省代焕商所得分佣
        N5 = (recharge - M) - N2 - N3 - N4  # 平台所得分佣

        print("充值服务费金额是：%.4f" % (recharge))
        print("充值到账比例是：%.4f" % (proportion))
        print("服务费余额是：%.4f * %.4f = %.4f" % (recharge, proportion, R1))
        print("存入储备池金额是：%.4f * %.4f = %.4f" % (recharge, A, M))
        print("区代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (self.area, self.area_proportion, (recharge - M), N2))
        print("市代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (
        self.city, (self.city_proportion - self.area_proportion), (recharge - M), N3))
        if self.province_proportion == None:
            print("没有省代")
        else:
            print("省代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (self.province,
                                                             (self.province_proportion - self.city_proportion),
                                                             (recharge - M), N4))
        print("平台所得充值分佣金额是：%.4f - %.4f - %.4f - %.4f = %.4f" % (recharge - M, N2, N3, N4, N5))
        return M

    # 支付时应出易贝服务费分佣
    def yibei_service_fee(self, service_fee, service_fee_ratio):
        '''
        :param service_fee: 买家需要支付易贝服务费
        :param service_fee_ratio:支付的易贝服务费费率(会员等级)
        '''

        # global M1, M2, M3, M4, M5
        if self.personal_proportion <= self.area_proportion:  # 个人焕商分佣比例小于等于区代分佣比例  也就是算法一
            print("使用算法一")
            M1 = service_fee * self.personal_proportion  # 个人所得分佣
            M2 = (self.area_proportion - self.personal_proportion) * service_fee  # 区代焕商所得分佣
            M3 = (self.city_proportion - self.area_proportion) * service_fee  # 市代焕商所得分佣
            if self.province_proportion == None:
                M4 = 0
            else:
                M4 = (self.province_proportion - self.city_proportion) * service_fee  # 省代焕商所得分佣
            M5 = service_fee - M1 - M2 - M3 - M4  # 平台所得分佣
            print("服务费比例是：%.4f" % (service_fee_ratio))
            print("买家需要支付易贝服务费是：%.4f" % (service_fee))
            print(
                "个人焕商%.0f获得得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.personal, service_fee, self.personal_proportion, M1))
            print("区代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.area,
                                                              (self.area_proportion - self.personal_proportion),
                                                              service_fee, M2))
            print("市代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.city,
                                                              (self.city_proportion - self.area_proportion),
                                                              service_fee, M3))
            if self.province_proportion == None:
                print("没有省代")
            else:
                print("省代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.province,
                                                                  (self.province_proportion - self.city_proportion),
                                                                  service_fee, M4))
            print("平台获得的易贝服务费分佣是：%.4f - %.4f - %.4f - %.4f - %.4f=%.4f" % (service_fee, M1, M2, M3, M4, M5))

        elif self.personal_proportion > self.area_proportion:  # 个人焕商分佣比例大于区代分佣比例  也就是算法一
            print("使用算法二")
            M1 = service_fee * self.personal_proportion  # 个人所得分佣
            M2 = self.area_proportion * (service_fee - M1)  # 区代焕商所得分佣
            M3 = (self.city_proportion - self.area_proportion) * (service_fee - M1)  # 市代焕商所得分佣
            if self.province_proportion == None:
                M4 = 0
            else:
                M4 = (self.province_proportion - self.city_proportion) * (service_fee - M1)  # 省代焕商所得分佣
            M5 = service_fee - M1 - M2 - M3 - M4  # 平台所得分佣

            print("服务费比例是：%.4f" % (service_fee_ratio))
            print("买家需要支付易贝服务费是：%.4f" % (service_fee))
            print(
                "个人焕商%.0f获得得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.personal, service_fee, self.personal_proportion, M1))
            print("区代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.area, self.area_proportion, (service_fee - M1), M2))
            print("市代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.city,
                                                              (self.city_proportion - self.area_proportion),
                                                              (service_fee - M1), M3))
            if self.province_proportion == None:
                print("没有省代")
            else:
                print("省代焕商%.0f获得的易贝服务费分佣是：%.4f * %.4f = %.4f" % (self.province,
                                                                  (self.province_proportion - self.city_proportion),
                                                                  (service_fee - M1), M4))
            print("平台获得的易贝服务费分佣是： %.4f - %.4f - %.4f - %.4f - %.4f=%.4f " % (service_fee, M1, M2, M3, M4, M5,))

    # 储备池分佣算法
    def cash_service_fee(self, recharge, reserve_pool, service_fee, service_fee_ratio):
        '''
        :param recharge：充值金额
        :param reserve_pool: 储备池的金额
        :param service_fee: 分佣的服务费金额
        :param service_fee_ratio: 现金服务费比例
        :return:个人所得分佣
        '''
        # global M1, M2, M3, M4, M5
        personal_deserved = recharge * self.personal_proportion  # 个人焕商应得金额
        if reserve_pool > personal_deserved:  # 储备池金额>个人焕商应得金额
            print("计算储备池分佣")
            M2 = self.area_proportion * (reserve_pool - personal_deserved)  # 区代焕商所得分佣
            M3 = (self.city_proportion - self.area_proportion) * (reserve_pool - personal_deserved)  # 市代焕商所得分佣
            if self.province_proportion == None:
                M4 = 0
            else:
                M4 = (self.province_proportion - self.city_proportion) * (reserve_pool - personal_deserved)  # 省代焕商所得分佣
            M5 = reserve_pool - personal_deserved - M2 - M3 - M4  # 平台所得分佣
            print("服务费比例是：%.4f" % (service_fee_ratio))
            print("买家需要支付服务费是：%.4f" % (service_fee))
            print("储备池金额是：%.4f" % (reserve_pool))
            print("个人焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (
            self.personal, recharge, self.personal_proportion, personal_deserved))
            print("区代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (
            self.area, self.area_proportion, (reserve_pool - personal_deserved), M2))
            print("市代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (self.city,
                                                             (self.city_proportion - self.area_proportion),
                                                             (reserve_pool - personal_deserved), M3))
            if self.province_proportion == None:
                print("没有省代")
            else:
                print(
                    "省代焕商%.0f获得的现金交易分佣是：%.4f * %.4f = %.4f" % (self.province,
                                                               (self.province_proportion - self.city_proportion),
                                                               (reserve_pool - personal_deserved), M4))
            print("平台获得的现金交易分佣是： %.4f - %.4f - %.4f - %.4f - %.4f=%.4f " % (
                reserve_pool, personal_deserved, M2, M3, M4, M5))

        elif reserve_pool <= personal_deserved:
            personal_deserved = reserve_pool  # 全给个人焕商
            print("个人焕商%.0f获得得的现金交易分佣是：%.4f" % (personal_deserved))

        return personal_deserved


if __name__ == '__main__':
    print("---------------------我是分割线----------------------------")
    Dividend(province_proportion=0.8, city_proportion=0.7, area_proportion=0.6,
             personal_proportion=0.5).cash_service_fee(1000, 500, 10, 0.03)
