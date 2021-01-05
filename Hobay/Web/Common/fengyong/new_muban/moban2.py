#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/8 21:47
# @Author :春衫
# @File :title.py

from decimal import *
from Web.Common import DoExcel
from Web.Common.fengyong.sql.wallet_detail import wallet_detail
from Web.Common import test_data_path
from Web.Common import qushe
from Web.Common import chulidata
from Web.Common.fengyong.new_muban.calculate_commission import calculate_commission
from Web.Common import UserLog

my_logger = UserLog()
test_data = DoExcel().get_data(test_data_path)


class MoBan:

    def __init__(self, buyer_identity, seller_identity, member_level, payment_method, order):
        '''

        :param buyer_identity:  买家身份 1公海用户 2非公海用户
        :param seller_identity:  卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        :param member_level: 会员等级
        :param payment_method:支付方式
        :param order: 订单号
        :return:交易流水 tuple
        '''

        self.buyer_identity = buyer_identity
        self.seller_identity = seller_identity
        self.member_level = member_level
        self.payment_method = payment_method
        self.order = order

    def moban(self, data, superior, ip, calculation, second_payagent_ratio,
              bind_buyer_relationship_data, bind_payer_relationship_data=None, reserve_fund=None):
        '''

        Parameters
        ----------
        data：Excel数据
        superior：注册地省市区id
        ip：数据库IP
        calculation：一级分佣计算结果
        order：订单号
        second_payagent_ratio：二级分佣比例
        bind_buyer_relationship_data：买家绑定关系
        bind_payer_relationship_data：出钱方绑定关系 因为易贝、易贝券支付不需要他，所以默认为None
        reserve_fund：储备池 已绑定，所以可能没有储备池，默认为None

        Returns：分佣模板
        -------

        '''
        global payment_method_data, pay_cbp_service_fee, pay_cash_service_fee, reserve_fund_personal_commission, reserve_fund_area_commission, reserve_fund_city_commission, reserve_fund_province_commission, reserve_fund_platform_commission, service_fee_personal_commission, service_fee_area_commission, service_fee_city_commission, service_fee_province_commission, service_fee_platform_commission, reserve_fund_bing_sales, Identity, reserve_fund_agent, first_region_commission, reserve_fund_template, service_fee_bind_area_id, service_fee_bind_city_id, service_fee_bind_province_id, service_fee_bing_sales, service_fee_agent, template1, service_fee_template, seller_income_amount

        buyer_id = data['买家']
        seller_id = data['卖家']
        platform_id = data['平台']

        order_detail = wallet_detail(ip, self.order)  # 支付数据

        goods_price = (order_detail[0])[3]  # 读取的商品价格

        if self.payment_method != "易贝券":
            if self.payment_method in ["现金", "微信", "支付宝"]:
                pay_cash_service_fee = (calculation[0])[1]  # 卖家需要支付的现金服务费
                seller_income_amount = goods_price * -1 - pay_cash_service_fee  # 卖家实际应收到的金额

            elif self.payment_method in ["易贝", "抵工资", "家人购"]:
                pay_cbp_service_fee = (calculation[0])[1]  # 买家应出易贝服务费
                pay_cash_service_fee = (calculation[0])[2]  # 买家应出现金服务费

        if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):

            reserve_fund_personal_commission = (calculation[1])[0]  # 储备池买家上级个人焕商分佣
            reserve_fund_area_commission = (calculation[1])[1]  # 储备池买家上级区代理商分佣
            reserve_fund_city_commission = (calculation[1])[2]  # 储备池买家上级市代理商分佣
            reserve_fund_province_commission = (calculation[1])[3]  # 储备池买家上级省代理商分佣
            reserve_fund_platform_commission = (calculation[1])[4]  # 储备池平台分佣

            if self.payment_method != "易贝券":
                service_fee_personal_commission = (calculation[2])[0]  # 易贝服务费买家上级个人焕商分佣
                service_fee_area_commission = (calculation[2])[1]  # 易贝服务费买家上级区代理商分佣
                service_fee_city_commission = (calculation[2])[2]  # 易贝服务费买家上级市代理商分佣
                service_fee_province_commission = (calculation[2])[3]  # 易贝服务费买家上级省代理商分佣
                service_fee_platform_commission = (calculation[2])[4]  # 易贝服务费平台分佣
        else:
            if self.payment_method != "易贝券":
                service_fee_personal_commission = (calculation[1])[0]  # 易贝服务费买家上级个人焕商分佣
                service_fee_area_commission = (calculation[1])[1]  # 易贝服务费买家上级区代理商分佣
                service_fee_city_commission = (calculation[1])[2]  # 易贝服务费买家上级市代理商分佣
                service_fee_province_commission = (calculation[1])[3]  # 易贝服务费买家上级省代理商分佣
                service_fee_platform_commission = (calculation[1])[4]  # 易贝服务费平台分佣

        if self.payment_method == "易贝":
            payment_method_data = "易贝"
        elif self.payment_method == "易贝券":
            payment_method_data = "易贝券"
        elif self.payment_method == "抵工资":
            payment_method_data = "抵工资"
        # 因为家人购文案不叫家人购，而是叫亲情
        elif self.payment_method == "家人购":
            payment_method_data = "亲情"
        elif self.payment_method == "现金":
            payment_method_data = "现金"
        elif self.payment_method == "微信":
            payment_method_data = "微信"
        elif self.payment_method == "支付宝":
            payment_method_data = "支付宝"

        # 生成易贝、抵工资、家人购流水模板
        if self.payment_method in ['易贝', '抵工资', '家人购']:

            if self.payment_method == "易贝":

                reserve_fund_bind_personal_id = superior[0]['个人焕商']
                reserve_fund_bind_area_id = superior[1]['区代理商']
                reserve_fund_bind_city_id = superior[1]['市代理商']
                reserve_fund_bind_province_id = superior[1]['省代理商']
                service_fee_bind_personal_id = superior[0]['个人焕商']
                service_fee_bind_area_id = superior[1]['区代理商']
                service_fee_bind_city_id = superior[1]['市代理商']
                service_fee_bind_province_id = superior[1]['省代理商']

                start_template = [
                    (buyer_id, 2, 3, goods_price, None, None, f'{payment_method_data}购买商品：扣除买家订单易贝金额', 1),
                    (buyer_id, 2, 1, pay_cbp_service_fee * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费', 1),
                    (buyer_id, 2, 1, pay_cash_service_fee * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家现金服务费', 3),
                    (platform_id, 2, 3, goods_price * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家订单易贝金额转入平台', 1),
                    (platform_id, 2, 1, pay_cbp_service_fee, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费转入平台', 1),
                    (platform_id, 2, 1, pay_cash_service_fee, None, None,
                     f'{payment_method_data}购买商品：扣除买家现金服务费转入平台', 3),
                    (platform_id, 2, 3, goods_price, None, None, f'{payment_method_data}购买商品：订单易贝金额从平台转出', 1),
                    (
                        seller_id, 2, 3, goods_price * -1, None, None,
                        f'{payment_method_data}购买商品:扣除买家订单易贝金额转给卖家',
                        1)]

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    reserve_fund_template = [(buyer_id, 2, 9, reserve_fund * -1, None, None, '购买商品：扣除买家储备金', 11),
                                             (reserve_fund_bind_personal_id, 2, 10, reserve_fund_personal_commission,
                                              None, None,
                                              '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (
                                                 reserve_fund_bind_area_id, 2, 10, reserve_fund_area_commission, None,
                                                 None,
                                                 '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (
                                                 reserve_fund_bind_city_id, 2, 10, reserve_fund_city_commission, None,
                                                 None,
                                                 '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (reserve_fund_bind_province_id, 2, 10, reserve_fund_province_commission,
                                              None, None,
                                              '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (platform_id, 2, 10, reserve_fund_platform_commission, None, None,
                                              '购买商品：代理商分佣金额（激励金）收入',
                                              2)]

                service_fee_template = [
                    (platform_id, 2, 1, pay_cbp_service_fee * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润(服务费)总金额支出',
                     1),
                    (service_fee_bind_personal_id, 2, 2, service_fee_personal_commission, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                    (service_fee_bind_area_id, 2, 2, service_fee_area_commission, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                    (service_fee_bind_city_id, 2, 2, service_fee_city_commission, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                    (service_fee_bind_province_id, 2, 2, service_fee_province_commission, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                    (platform_id, 2, 2, service_fee_platform_commission, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1)]

            # 抵工资 家人购
            else:

                service_fee_bind_personal_id = superior['支付服务费分佣'][0]['个人焕商']
                service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
                service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
                service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']
                reserve_fund_bind_personal_id = superior['储备池分佣'][0]['个人焕商']
                reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
                reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
                reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']
                payer_id = data['出钱方']

                start_template = [
                    (payer_id, 2, 3, goods_price, None, None, f'{payment_method_data}购买商品：扣除买家订单易贝金额', 1),
                    (payer_id, 2, 1, pay_cbp_service_fee * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费', 1),
                    (payer_id, 2, 1, pay_cash_service_fee * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家现金服务费', 3),
                    (platform_id, 2, 3, goods_price * -1, None, None,
                     f'{payment_method_data}购买商品：扣除买家订单易贝金额转入平台', 1),
                    (platform_id, 2, 1, pay_cbp_service_fee, None, None,
                     f'{payment_method_data}购买商品：扣除买家易贝服务费转入平台', 1),
                    (platform_id, 2, 1, pay_cash_service_fee, None, None,
                     f'{payment_method_data}购买商品：扣除买家现金服务费转入平台', 3),
                    (
                        platform_id, 2, 3, goods_price, None, None, f'{payment_method_data}购买商品：订单易贝金额从平台转出',
                        1),
                    (seller_id, 2, 3, goods_price * -1, None, None,
                     f'{payment_method_data}购买商品:扣除买家订单易贝金额转给卖家', 1)]

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    reserve_fund_template = [(buyer_id, 2, 9, reserve_fund * -1, None, None, '购买商品：扣除买家储备金', 11),
                                             (reserve_fund_bind_personal_id, 2, 10, reserve_fund_personal_commission,
                                              None, None,
                                              '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (reserve_fund_bind_area_id, 2, 10, reserve_fund_area_commission, None,
                                              None, '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (reserve_fund_bind_city_id, 2, 10, reserve_fund_city_commission, None,
                                              None, '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (reserve_fund_bind_province_id, 2, 10, reserve_fund_province_commission,
                                              None, None,
                                              '购买商品：代理商分佣金额（激励金）收入', 2),
                                             (platform_id, 2, 10, reserve_fund_platform_commission, None, None,
                                              '购买商品：代理商分佣金额（激励金）收入',
                                              2)]

                if self.payment_method == "抵工资":
                    service_fee_template = [
                        (platform_id, 2, 1, pay_cbp_service_fee * -1, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润(服务费)总金额支出', 1),
                        (service_fee_bind_personal_id, 2, 2, service_fee_personal_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                        (service_fee_bind_area_id, 2, 2, service_fee_area_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                        (service_fee_bind_city_id, 2, 2, service_fee_city_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                        (service_fee_bind_province_id, 2, 2, service_fee_province_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1),
                        (platform_id, 2, 2, service_fee_platform_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费分润', 1)]
                # 家人购
                else:
                    service_fee_template = [
                        (platform_id, 2, 1, pay_cbp_service_fee * -1, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润(服务费)总金额支出',
                         1),
                        (service_fee_bind_personal_id, 2, 2, service_fee_personal_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1),
                        (service_fee_bind_area_id, 2, 2, service_fee_area_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1),
                        (service_fee_bind_city_id, 2, 2, service_fee_city_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1),
                        (service_fee_bind_province_id, 2, 2, service_fee_province_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1),
                        (platform_id, 2, 2, service_fee_platform_commission, None, None,
                         f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1)]

        # 生成易贝券流水模板
        elif self.payment_method == "易贝券":

            reserve_fund_bind_personal_id = superior[0]['个人焕商']
            reserve_fund_bind_area_id = superior[1]['区代理商']
            reserve_fund_bind_city_id = superior[1]['市代理商']
            reserve_fund_bind_province_id = superior[1]['省代理商']

            start_template = [
                (buyer_id, 2, 3, goods_price, None, None, f'{payment_method_data}支付购物商品费用：扣除买家订单易贝金额', 10),
                (platform_id, 2, 3, goods_price * -1, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家订单易贝金额转入平台', 1),
                (platform_id, 2, 3, goods_price, None, None, f'{payment_method_data}支付购物商品费用：订单易贝金额从平台转出', 1),
                (
                    seller_id, 2, 3, goods_price * -1, None, None,
                    f'{payment_method_data}支付购物商品费用:扣除买家订单易贝金额转给卖家',
                    1)]

            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                reserve_fund_template = [(buyer_id, 2, 9, reserve_fund * -1, None, None, '购买商品：扣除买家储备金', 11),
                                         (reserve_fund_bind_personal_id, 2, 10, reserve_fund_personal_commission, None,
                                          None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_area_id, 2, 10, reserve_fund_area_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_city_id, 2, 10, reserve_fund_city_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_province_id, 2, 10, reserve_fund_province_commission, None,
                                          None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (platform_id, 2, 10, reserve_fund_platform_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2)]

        # 生成现金账户、微信、支付宝流水模板
        else:

            service_fee_bind_personal_id = superior['支付服务费分佣'][0]['个人焕商']
            service_fee_bind_area_id = superior['支付服务费分佣'][1]['区代理商']
            service_fee_bind_city_id = superior['支付服务费分佣'][1]['市代理商']
            service_fee_bind_province_id = superior['支付服务费分佣'][1]['省代理商']
            reserve_fund_bind_personal_id = superior['储备池分佣'][0]['个人焕商']
            reserve_fund_bind_area_id = superior['储备池分佣'][1]['区代理商']
            reserve_fund_bind_city_id = superior['储备池分佣'][1]['市代理商']
            reserve_fund_bind_province_id = superior['储备池分佣'][1]['省代理商']

            start_template = [
                (buyer_id, 2, 3, goods_price, None, None, f'{payment_method_data}支付购物商品费用：扣除买家订单金额（现金）', 2),
                (platform_id, 2, 3, seller_income_amount, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家订单金额（现金）转入平台(卖家实际应收到的金额)', 2),
                (platform_id, 2, 1, pay_cash_service_fee, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除卖家（现金）服务费转入平台', 2),
                (platform_id, 2, 3, seller_income_amount * -1, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家订单金额（现金）转从平台(卖家实际应收到的金额)转出', 2),
                (seller_id, 2, 3, goods_price * -1, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家订单金额（现金）转给卖家(全部)', 2),
                (seller_id, 2, 1, pay_cash_service_fee * -1, None, None,
                 f'{payment_method_data}支付购物商品费用：从卖家现金账户扣除（现金）服务费', 2)]

            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                reserve_fund_template = [(buyer_id, 2, 9, reserve_fund * -1, None, None, '购买商品：扣除买家储备金', 11),
                                         (reserve_fund_bind_personal_id, 2, 10, reserve_fund_personal_commission, None,
                                          None, '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_area_id, 2, 10, reserve_fund_area_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_city_id, 2, 10, reserve_fund_city_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (reserve_fund_bind_province_id, 2, 10, reserve_fund_province_commission, None,
                                          None, '购买商品：代理商分佣金额（激励金）收入', 2),
                                         (platform_id, 2, 10, reserve_fund_platform_commission, None, None,
                                          '购买商品：代理商分佣金额（激励金）收入', 2)]

            service_fee_template = [
                (platform_id, 2, 1, pay_cash_service_fee * -1, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润(服务费)总金额支出', 2),
                (service_fee_bind_personal_id, 2, 2, service_fee_personal_commission, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润', 2),
                (service_fee_bind_area_id, 2, 2, service_fee_area_commission, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润', 2),
                (service_fee_bind_city_id, 2, 2, service_fee_city_commission, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润', 2),
                (service_fee_bind_province_id, 2, 2, service_fee_province_commission, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润', 2),
                (platform_id, 2, 2, service_fee_platform_commission, None, None,
                 f'{payment_method_data}支付购物商品费用：扣除买家现金服务费分润', 2)]

        # 二级分佣——储备池
        # 只有这两种情况才会有储备池分佣 有储备池分佣才会走二级分佣流程

        if self.payment_method in ["易贝", "易贝券"]:
            Identity = "买家"
        elif self.payment_method == "抵工资":
            Identity = "企业"
        elif self.payment_method == "家人购":
            Identity = "家人"
        elif self.payment_method == "现金":
            Identity = "卖家"

        if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
            # 判断是否走二级分佣
            my_logger.info("----------开始判断这笔交易储备金是否需要走二级分佣----------")

            reserve_fund_second_payagent_ratio = second_payagent_ratio['储备金二级分佣比例']

            # 查询买家是否绑定销售/业务焕商/TCO
            # 是销售/业务焕商/TCO邀请进来的用户才会走二级分佣，None代表不是由销售/业务焕商/TCO邀请进来
            # 并且还得满足使用的分佣比例不为None 为None说明：
            # 1、买家注册地没有区域焕商并且平台没有设置二级分佣比例。
            # 2、买家注册地有区域焕商，但是区域焕商都没有设置二级分佣比例
            if bind_buyer_relationship_data != None and reserve_fund_second_payagent_ratio != None:

                # 买家绑定上级的身份 可能是销售，也可能是业务焕商
                if "业务焕商" in bind_buyer_relationship_data or "销售" in bind_buyer_relationship_data:

                    if "业务焕商" in bind_buyer_relationship_data:
                        reserve_fund_bing_sales = "业务焕商"
                    elif "销售" in bind_buyer_relationship_data:
                        reserve_fund_bing_sales = "销售"

                    my_logger.info(f"买家由{reserve_fund_bing_sales}邀请进来,"
                                   f"该{reserve_fund_bing_sales}的id是：{bind_buyer_relationship_data[reserve_fund_bing_sales]}")

                    if bind_buyer_relationship_data['买家上级的上级id'] != None:
                        my_logger.info(
                            f"买家上级{reserve_fund_bing_sales}是由{bind_buyer_relationship_data['买家上级的上级身份']}邀请进来的,"
                            f"该上级的上级id是：{bind_buyer_relationship_data['买家上级的上级id']}")
                    else:
                        my_logger.info(f"买家上级{reserve_fund_bing_sales}不是由销售/业务焕商邀请进来的")

                    if "TCO" in bind_buyer_relationship_data:
                        my_logger.info(f"买家有上级TCO，该TCO的id是：{bind_buyer_relationship_data['TCO']}")
                    else:
                        my_logger.info(f"买家没有上级TCO")
                else:
                    reserve_fund_bing_sales = None
                    my_logger.info(f"买家不是由销售/业务焕商邀请进来的")


                if "TCO" and ("业务焕商" or "销售") in bind_buyer_relationship_data:
                    my_logger.info(f"{Identity}是由{reserve_fund_bing_sales}邀请进来的，并且有TCO管理,设置了二级分佣比例，所以交易储备金需要走二级分佣")
                else:
                    if "业务焕商" or "销售" in bind_buyer_relationship_data:
                        my_logger.info(
                            f"{Identity}是由{reserve_fund_bing_sales}邀请进来的，并且设置了二级分佣比例，所以交易储备金需要走二级分佣")
                    else:
                        my_logger.info(f"{Identity}有TCO管理，并且设置了二级分佣比例，所以交易储备金需要走二级分佣")

                my_logger.info("----------这笔交易储备金分佣需要走二级分佣流程----------")
                my_logger.info("----------开始计算储备金二级分佣----------")

                if reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_area_id:
                    reserve_fund_agent = "区代理商"
                elif reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_city_id:
                    reserve_fund_agent = "市代理商"
                elif reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_province_id:
                    reserve_fund_agent = "省代理商"

                my_logger.info(
                    f"这笔订单储备金二级分佣使用是{reserve_fund_agent}{reserve_fund_second_payagent_ratio['agent_id']}的分佣比例，"
                    f"{reserve_fund_agent}销售分佣比例是：{reserve_fund_second_payagent_ratio['sales_ratio']}，"
                    f"{reserve_fund_agent}TCO分佣比例是：{reserve_fund_second_payagent_ratio['tco_ratio']}，"
                    f"{reserve_fund_agent}业务焕商分佣比例是：{reserve_fund_second_payagent_ratio['free_sales_ratio']}")

                # 买家注册地区域焕商一级分佣金额
                if reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_area_id:
                    first_region_commission = reserve_fund_area_commission
                    my_logger.info(
                        f"需要进行储备金二级分佣的区代理商是：{reserve_fund_bind_area_id}，该区代理商一级分佣应得金额是：{first_region_commission}")
                elif reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_city_id:
                    first_region_commission = reserve_fund_city_commission
                    my_logger.info(
                        f"需要进行储备金二级分佣的市代理商是：{reserve_fund_bind_city_id}，该市代理商一级分佣应得金额是：{first_region_commission}")
                elif reserve_fund_second_payagent_ratio['agent_id'] == reserve_fund_bind_province_id:
                    first_region_commission = reserve_fund_province_commission
                    my_logger.info(
                        f"需要进行储备金二级分佣的省代理商是：{reserve_fund_bind_province_id}，该省代理商一级分佣应得金额是：{first_region_commission}")
                elif reserve_fund_second_payagent_ratio['agent_id'] == platform_id:
                    first_region_commission = reserve_fund_platform_commission
                    my_logger.info(f"需要进行储备金二级分佣的是平台，平台一级分佣应得金额是：{first_region_commission}")

                # 计算储备金二级分佣，返回绑定销售id和分佣、销售绑定的销售id和分佣、绑定的TCOid和分佣

                reserve_fund_commission = calculate_commission(reserve_fund_second_payagent_ratio,
                                                               bind_buyer_relationship_data,
                                                               first_region_commission)


                # 储备池买家绑定的上级TCOid
                reserve_fund_bing_TCO_id = reserve_fund_commission[0]
                # 储备池买家绑定的上级TCO二级分佣
                reserve_fund_bing_TCO_commission = reserve_fund_commission[1]
                if reserve_fund_bing_TCO_id != None:
                    my_logger.info(f"储备池买家绑定的上级TCOid是：{reserve_fund_bing_TCO_id}，"
                                   f"该TCO获得的二级分佣是：{reserve_fund_bing_TCO_commission}")
                    if reserve_fund_bing_TCO_commission == Decimal('0.00'):
                        my_logger.info("储备池买家绑定的上级TCO获得分佣等于0.00，舍去流水明细")
                        reserve_fund_bing_TCO_id = None
                else:
                    my_logger.info("买家没有绑定上级TCO")

                # 储备池买家绑定的上级销售id
                reserve_fund_bing_sales_id = reserve_fund_commission[2]
                # 储备池买家绑定的上级销售二级分佣
                reserve_fund_bing_sales_commission = reserve_fund_commission[3]
                if reserve_fund_bing_sales_id != None:
                    my_logger.info(f"储备池买家绑定的上级{reserve_fund_bing_sales}id是：{reserve_fund_bing_sales_id}，"
                                   f"该{reserve_fund_bing_sales}获得的二级分佣是：{reserve_fund_bing_sales_commission}")
                    if reserve_fund_bing_sales_commission == Decimal('0.00'):
                        my_logger.info(f"储备池买家绑定的上级{reserve_fund_bing_sales}获得分佣等于0.00，舍去流水明细")
                        reserve_fund_bing_sales_id = None
                else:
                    my_logger.info(f"储备池买家没有绑定上级销售/业务焕商，所以销售/业务焕商不会获得二级分佣")

                sales_bing_sales_identity = bind_buyer_relationship_data["买家上级的上级身份"]

                # 储备池买家上级销售绑定的销售id
                reserve_fund_sales_bing_sale_id = reserve_fund_commission[4]
                # 储备池买家上级销售绑定的销售二级分佣
                reserve_fund_sales_bing_sale_commission = reserve_fund_commission[5]
                if reserve_fund_bing_sales_id != None and reserve_fund_sales_bing_sale_id != None:
                    my_logger.info(
                        f"储备池买家上级{reserve_fund_bing_sales}绑定的上级{sales_bing_sales_identity}id是：{reserve_fund_sales_bing_sale_id}，"
                        f"该{sales_bing_sales_identity}获得的二级分佣是：{reserve_fund_sales_bing_sale_commission}")

                if reserve_fund_sales_bing_sale_commission == Decimal(
                        '0.00') and reserve_fund_sales_bing_sale_id != None:
                    my_logger.info(f"储备池买家上级{reserve_fund_bing_sales}绑定的{sales_bing_sales_identity}获得分佣等于0.00，舍去流水明细")
                    reserve_fund_sales_bing_sale_id = None

                # 分给销售、上级销售绑定的销售、TCO后，该省/市/区实际获得的分佣金额
                finally_reserve_fund_commission = reserve_fund_commission[6]

                my_logger.info(
                    f"二级分佣是拿{reserve_fund_agent}的钱来分，该{reserve_fund_agent}最终实际获得的分佣金额是：{first_region_commission} - "
                    f"{reserve_fund_bing_TCO_commission} - {reserve_fund_bing_sales_commission} - "
                    f"{reserve_fund_sales_bing_sale_commission} = {finally_reserve_fund_commission}")

                if reserve_fund_bing_sales == "销售":
                    reserve_fund_bing_sales_text = "销售员"
                else:
                    reserve_fund_bing_sales_text = "业务焕商"

                # 如果使用的二级分佣比例是区代的
                if reserve_fund_agent == "区代理商":

                    new_reserve_fund_template = [
                        (reserve_fund_bind_area_id, 2, 10, finally_reserve_fund_commission, None, None,
                         '购买商品：代理商分佣金额（激励金）收入', 2),
                        (reserve_fund_bing_TCO_id, 2, 11, reserve_fund_bing_TCO_commission,
                         None, None, 'TCO分佣金额（现金）收入', 2),
                        (reserve_fund_bing_sales_id, 2, 11,
                         reserve_fund_bing_sales_commission, None, None, f'{reserve_fund_bing_sales_text}分佣金额（现金）收入',
                         2),
                        (reserve_fund_sales_bing_sale_id, 2, 11,
                         reserve_fund_sales_bing_sale_commission, None, None,
                         f'{sales_bing_sales_identity}分佣金额（现金）收入', 2)]

                    reserve_fund_template = reserve_fund_template[
                                            :2] + new_reserve_fund_template + reserve_fund_template[3:]

                # 如果使用的二级分佣比例是市代的
                elif reserve_fund_agent == "市代理商":

                    new_reserve_fund_template = [
                        (reserve_fund_bind_city_id, 2, 10, finally_reserve_fund_commission, None, None,
                         '购买商品：代理商分佣金额（激励金）收入', 2),
                        (reserve_fund_bing_TCO_id, 2, 11,
                         reserve_fund_bing_TCO_commission,
                         None, None, 'TCO分佣金额（现金）收入', 2),
                        (reserve_fund_bing_sales_id, 2, 11,
                         reserve_fund_bing_sales_commission, None, None,
                         f'{reserve_fund_bing_sales_text}分佣金额（现金）收入', 2),
                        (reserve_fund_sales_bing_sale_id, 2, 11,
                         reserve_fund_sales_bing_sale_commission, None, None,
                         f'{sales_bing_sales_identity}分佣金额（现金）收入', 2)]

                    reserve_fund_template = reserve_fund_template[
                                            :3] + new_reserve_fund_template + reserve_fund_template[4:]

                # 如果使用的二级分佣比例是省代的
                elif reserve_fund_agent == "省代理商":

                    new_reserve_fund_template = [
                        (reserve_fund_bind_province_id, 2, 10, finally_reserve_fund_commission, None, None,
                         '购买商品：代理商分佣金额（激励金）收入', 2),
                        (reserve_fund_bing_TCO_id, 2, 11,
                         reserve_fund_bing_TCO_commission,
                         None, None, 'TCO分佣金额（现金）收入', 2),
                        (reserve_fund_bing_sales_id, 2, 11,
                         reserve_fund_bing_sales_commission, None, None,
                         f'{reserve_fund_bing_sales_text}分佣金额（现金）收入', 2),
                        (reserve_fund_sales_bing_sale_id, 2, 11,
                         reserve_fund_sales_bing_sale_commission, None, None,
                         f'{sales_bing_sales_identity}分佣金额（现金）收入', 2)]

                    reserve_fund_template = reserve_fund_template[
                                            :4] + new_reserve_fund_template + reserve_fund_template[5:]
            else:
                if bind_buyer_relationship_data == None:
                    my_logger.info(f"----------{Identity}不是由销售/业务焕商/TCO邀请进来的，储备金不走二级分佣流程----------")
                else:
                    my_logger.info(f"----------{Identity}是由销售/业务焕商邀请进来，但是没有可用的储备金二级分佣比例，所以储备金不走二级分佣流程----------")

        else:
            my_logger.info("----------买家卖家不绑定，没有储备池，这笔交易不分佣----------")

        # 二级分佣——支付服务费
        my_logger.info("----------开始判断这笔交易服务费是否需要走二级分佣----------")
        service_fee_second_payagent_ratio = second_payagent_ratio['支付服务费二级分佣比例']

        if service_fee_second_payagent_ratio != None:
            if service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_area_id:
                service_fee_agent = "区代理商"
            elif service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_city_id:
                service_fee_agent = "市代理商"
            elif service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_province_id:
                service_fee_agent = "省代理商"
            else:
                service_fee_agent = "平台"

        # 易贝服务费不需要支付服务费，所以不会走服务费的二级分佣
        if self.payment_method != "易贝券":

            # 因为这几种支付方式，服务费是看出钱的人注册区域，而不是买家注册区域 传值改变 兼容
            if self.payment_method in ["抵工资", "家人购", "现金", "微信", "支付宝"]:
                bind_relationship_data = bind_payer_relationship_data
            else:
                bind_relationship_data = bind_buyer_relationship_data

            # 是销售/业务焕商/TCO邀请进来的用户才会走二级分佣，None代表不是由销售/业务焕商/TCO邀请进来
            # 并且还得满足使用的分佣比例不为None 为None说明：
            # 1、买家注册地没有区域焕商并且平台没有设置二级分佣比例。
            # 2、买家注册地有区域焕商，但是区域焕商都没有设置二级分佣比例
            if bind_relationship_data != None and service_fee_second_payagent_ratio != None:

                if "业务焕商" in bind_buyer_relationship_data or "销售" in bind_buyer_relationship_data:

                    if "业务焕商" in bind_buyer_relationship_data:
                        service_fee_bing_sales = "业务焕商"
                    elif "销售" in bind_buyer_relationship_data:
                        service_fee_bing_sales = "销售"

                    my_logger.info(f"买家由{service_fee_bing_sales}邀请进来,"
                                   f"该{service_fee_bing_sales}的id是：{bind_buyer_relationship_data[service_fee_bing_sales]}")

                    if bind_buyer_relationship_data['买家上级的上级id'] != None:
                        my_logger.info(
                            f"买家上级{service_fee_bing_sales}是由{bind_buyer_relationship_data['买家上级的上级身份']}邀请进来的,"
                            f"该上级的上级id是：{bind_buyer_relationship_data['买家上级的上级id']}")
                    else:
                        my_logger.info(f"买家上级{service_fee_bing_sales}不是由销售/业务焕商邀请进来的")

                    if "TCO" in bind_buyer_relationship_data:
                        my_logger.info(f"买家有上级TCO，该TCO的id是：{bind_buyer_relationship_data['TCO']}")
                    else:
                        my_logger.info(f"买家没有上级TCO")
                else:
                    service_fee_bing_sales = None
                    my_logger.info(f"买家不是由销售/业务焕商邀请进来的")


                if "TCO" and ("业务焕商" or "销售") in bind_buyer_relationship_data:
                    my_logger.info(f"{Identity}是由{service_fee_bing_sales}邀请进来的，并且有TCO管理,设置了二级分佣比例，所以交易服务费需要走二级分佣")
                else:
                    if "业务焕商" in bind_buyer_relationship_data or "销售" in bind_buyer_relationship_data:
                        my_logger.info(
                            f"{Identity}是由{service_fee_bing_sales}邀请进来的，并且设置了二级分佣比例，所以交易服务费需要走二级分佣")
                    else:
                        my_logger.info(f"{Identity}有TCO管理，并且设置了二级分佣比例，所以交易服务费需要走二级分佣")

                my_logger.info("----------这笔交易服务费分佣需要走二级分佣流程----------")
                my_logger.info("----------开始计算交易服务费二级分佣----------")

                my_logger.info(f"这笔订单服务费二级分佣使用{service_fee_agent}{service_fee_second_payagent_ratio['agent_id']}的分佣比例，"
                               f"{service_fee_agent}销售分佣比例是：{service_fee_second_payagent_ratio['sales_ratio']}，"
                               f"{service_fee_agent}TCO分佣比例是：{service_fee_second_payagent_ratio['tco_ratio']}，"
                               f"{service_fee_agent}业务焕商分佣比例是：{service_fee_second_payagent_ratio['free_sales_ratio']}")

                # 出钱方注册地区域焕商一级分佣金额
                if service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_area_id:
                    first_region_commission = service_fee_area_commission
                    my_logger.info(
                        f"需要进行交易服务费二级分佣的区代理商是：{service_fee_bind_area_id}，该区代理商一级分佣应得金额是：{first_region_commission}")
                elif service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_city_id:
                    first_region_commission = service_fee_city_commission
                    my_logger.info(
                        f"需要进行交易服务费二级分佣的市代理商是：{service_fee_bind_city_id}，该区代理商一级分佣应得金额是：{first_region_commission}")
                elif service_fee_second_payagent_ratio['agent_id'] == service_fee_bind_province_id:
                    first_region_commission = service_fee_province_commission
                    my_logger.info(
                        f"需要进行交易服务费二级分佣的省代理商是：{service_fee_bind_province_id}，该区代理商一级分佣应得金额是：{first_region_commission}")
                elif service_fee_second_payagent_ratio['agent_id'] == platform_id:
                    first_region_commission = service_fee_platform_commission
                    my_logger.info(f"需要进行交易服务费二级分佣的是平台，平台一级分佣应得金额是：{first_region_commission}")

                # 计算服务费二级分佣，返回绑定销售id和分佣、销售绑定的销售id和分佣、绑定的TCOid和分佣
                service_fee_commission = calculate_commission(service_fee_second_payagent_ratio,
                                                              bind_relationship_data,
                                                              first_region_commission)

                # 服务费出钱方上级TCOid
                service_fee_bing_TCO_id = service_fee_commission[0]
                # 服务费出钱方上级TCO二级分佣
                service_fee_bing_TCO_commission = service_fee_commission[1]

                my_logger.info(f"交易服务费买家绑定的上级TCOid是：{service_fee_bing_TCO_id}，"
                               f"该TCO获得的二级分佣是：{service_fee_bing_TCO_commission}")
                if service_fee_bing_TCO_commission == Decimal('0.00'):
                    service_fee_bing_TCO_id = None
                    my_logger.info("服务费出钱方上级TCO获得分佣等于0.00，舍去流水明细")

                # 服务费出钱方绑定的上级销售id
                service_fee_bing_sales_id = service_fee_commission[2]
                # 服务费出钱方绑定的上级销售二级分佣
                service_fee_bing_sales_commission = service_fee_commission[3]
                if service_fee_bing_sales_id != None:
                    my_logger.info(f"买家绑定的上级{service_fee_bing_sales}id是：{service_fee_bing_sales_id}，"
                                   f"该{service_fee_bing_sales}获得的服务费二级分佣是：{service_fee_bing_sales_commission}")
                else:
                    my_logger.info(f"买家没有没有绑定的上级销售/业务焕商，不会获得分佣")

                if service_fee_bing_sales_commission == Decimal('0.00'):
                    my_logger.info(f"服务费出钱方绑定的上级{service_fee_bing_sales}获得分佣等于0.00，舍去流水明细")
                    service_fee_bing_sales_id = None

                # 上级销售绑定销售身份 可能是销售，也可能是业务焕商
                sales_bing_sales_identity = bind_relationship_data["买家上级的上级身份"]

                # 服务费出钱方上级销售绑定的销售id
                service_fee_sales_bing_sales_id = service_fee_commission[4]
                # 服务费出钱方上级销售绑定的销售二级分佣
                service_fee_sales_bing_sales_commission = service_fee_commission[5]
                if service_fee_bing_sales_id != None and service_fee_sales_bing_sales_id != None:
                    my_logger.info(
                        f"买家上级{service_fee_bing_sales}绑定的上级{sales_bing_sales_identity}id是：{service_fee_sales_bing_sales_id}，"
                        f"该{sales_bing_sales_identity}获得的服务费二级分佣是：{service_fee_sales_bing_sales_commission}")

                if service_fee_sales_bing_sales_commission == Decimal(
                        '0.00') and service_fee_sales_bing_sales_id != None:
                    my_logger.info(f"服务费出钱方上级{service_fee_bing_sales}绑定的{sales_bing_sales_identity}获得分佣等于0.00，舍去流水明细")
                    service_fee_sales_bing_sales_id = None

                # 分给销售、上级销售绑定的销售、TCO后，该省/市/区实际获得的分佣金额
                finally_service_fee_commission = service_fee_commission[6]

                my_logger.info(
                    f"二级分佣是拿{service_fee_agent}的钱来分，该{service_fee_agent}最终实际获得的分佣金额是：{first_region_commission} - "
                    f"{service_fee_bing_TCO_commission} - {service_fee_bing_sales_commission} - "
                    f"{service_fee_sales_bing_sales_commission} = {finally_service_fee_commission}")

                if self.payment_method != "现金":
                    title = "易贝"
                else:
                    title = "现金"

                if self.payment_method in ["易贝", "抵工资", "家人购"]:
                    text = 1
                else:
                    text = 2

                # 如果使用的二级分佣比例是区代的
                if service_fee_agent == "区代理商":

                    # 家人购多了两个 进行 两个字，没办法只能区别处理
                    if self.payment_method in ["易贝", "抵工资"]:
                        template1 = [(service_fee_bind_area_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}购买商品：扣除买家{title}服务费分润', 1)]

                    elif self.payment_method == "家人购":
                        template1 = [(service_fee_bind_area_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1)]

                    elif self.payment_method in ["现金", "微信", "支付宝"]:
                        template1 = [(service_fee_bind_area_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}支付购物商品费用：扣除买家{title}服务费分润', 2)]

                    template2 = [(service_fee_bing_TCO_id, 2, 11, service_fee_bing_TCO_commission, None, None,
                                  f'TCO分佣金额（{title}）收入', text),
                                 (service_fee_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{service_fee_bing_sales}分佣金额（{title}）收入', text),
                                 (service_fee_sales_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{title}分佣金额（{sales_bing_sales_identity}）收入', text)]

                    new_service_fee_template = template1 + template2
                    service_fee_template = service_fee_template[:2] + new_service_fee_template + service_fee_template[
                                                                                                 3:]

                # 如果使用的二级分佣比例是市代的
                elif service_fee_agent == "市代理商":

                    # 家人购多了两个 进行 两个字，没办法只能区别处理
                    if self.payment_method in ["易贝", "抵工资"]:
                        template1 = [(service_fee_bind_city_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}购买商品：扣除买家{title}服务费分润', 1)]

                    elif self.payment_method == "家人购":
                        template1 = [(service_fee_bind_city_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1)]

                    elif self.payment_method in ["现金", "微信", "支付宝"]:
                        template1 = [(service_fee_bind_city_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}支付购物商品费用：扣除买家{title}服务费分润', 2)]

                    template2 = [(service_fee_bing_TCO_id, 2, 11, service_fee_bing_TCO_commission, None, None,
                                  f'TCO分佣金额（{title}）收入', text),
                                 (service_fee_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{service_fee_bing_sales}分佣金额（{title}）收入', text),
                                 (service_fee_sales_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{title}分佣金额（{sales_bing_sales_identity}）收入', 2)]

                    new_service_fee_template = template1 + template2
                    service_fee_template = service_fee_template[:3] + new_service_fee_template + service_fee_template[
                                                                                                 4:]

                # 如果使用的二级分佣比例是省代的
                elif service_fee_agent == "省代理商":

                    # 家人购多了两个 进行 两个字，没办法只能区别处理
                    if self.payment_method in ["易贝", "抵工资"]:
                        template1 = [(service_fee_bind_province_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}购买商品：扣除买家{title}服务费分润', 1)]

                    elif self.payment_method == "家人购":
                        template1 = [(service_fee_bind_province_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1)]

                    elif self.payment_method in ["现金", "微信", "支付宝"]:
                        template1 = [(service_fee_bind_province_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}支付购物商品费用：扣除买家{title}服务费分润', 2)]

                    template2 = [(service_fee_bing_TCO_id, 2, 11, service_fee_bing_TCO_commission, None, None,
                                  f'TCO分佣金额（{title}）收入', text),
                                 (service_fee_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{service_fee_bing_sales}分佣金额（{title}）收入', text),
                                 (service_fee_sales_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{title}分佣金额（{sales_bing_sales_identity}）收入', 2)]

                    new_service_fee_template = template1 + template2
                    service_fee_template = service_fee_template[:4] + new_service_fee_template + service_fee_template[
                                                                                                 5:]

                # 如果使用的二级分佣比例是平台的
                elif service_fee_agent == "平台":

                    # 家人购多了两个 进行 两个字，没办法只能区别处理
                    if self.payment_method in ["易贝", "抵工资"]:
                        template1 = [(platform_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}购买商品：扣除买家{title}服务费分润', 1)]

                    elif self.payment_method == "家人购":
                        template1 = [(platform_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{payment_method_data}购买商品：扣除买家易贝服务费进行分润', 1)]

                    elif self.payment_method in ["现金", "微信", "支付宝"]:
                        template1 = [(platform_id, 2, 2, finally_service_fee_commission, None, None,
                                      f'{self.payment_method}支付购物商品费用：扣除买家{title}服务费分润', 2)]

                    template2 = [(service_fee_bing_TCO_id, 2, 11, service_fee_bing_TCO_commission, None, None,
                                  'TCO分佣金额（{title}）收入', text),
                                 (service_fee_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{service_fee_bing_sales}分佣金额（{title}）收入', text),
                                 (service_fee_sales_bing_sales_id, 2, 11, service_fee_bing_sales_commission, None, None,
                                  f'{title}分佣金额（{sales_bing_sales_identity}）收入', 2)]

                    new_service_fee_template = template1 + template2
                    service_fee_template = service_fee_template[:5] + new_service_fee_template + service_fee_template[
                                                                                                 6:]
            else:
                if bind_relationship_data == None:
                    if self.payment_method == "现金":
                        my_logger.info("----------卖家不是由销售/业务焕商/TCO邀请进来的，交易服务费不走二级分佣流程----------")
                    elif self.payment_method == "抵工资":
                        my_logger.info("----------企业不是由销售/业务焕商/TCO邀请进来的，交易服务费不走二级分佣流程----------")
                    elif self.payment_method == "家人购":
                        my_logger.info("----------家人不是由销售/业务焕商/TCO邀请进来的，交易服务费不走二级分佣流程----------")
                    else:
                        my_logger.info("----------买家不是由销售/业务焕商/TCO邀请进来的，交易服务费不走二级分佣流程----------")
                else:
                    my_logger.info("----------买家是由销售/业务焕商邀请进来，但是没有可用的二级分佣比例，所以交易服务费不走二级分佣流程----------")
        else:
            my_logger.info("----------使用易贝券支付不需要支付服务费，不会走二级分佣流程----------")

        if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
            if self.payment_method == "易贝券":
                payment_data = start_template + reserve_fund_template
            else:

                payment_data = start_template + reserve_fund_template + service_fee_template
        else:
            if self.payment_method != "易贝券":
                payment_data = start_template + service_fee_template
            else:
                payment_data = start_template

        # 把ID=None的行去掉 ID=None代表不会有分佣明细
        payment_data = qushe(payment_data)

        # 把钱包变化之前的值、变化之后的值替换回去
        payment_data = chulidata(payment_data, ip, self.order)

        return payment_data

    def expected_moban(self, ip, data, superior, reserve_fund, calculation_data, transaction_second_payagent_ratio,
                       bind_buyer_relationship_data, bind_payer_relationship_data=None):

        if self.payment_method in ["易贝", "易贝券"]:
            expected_moban = MoBan(self.buyer_identity, self.seller_identity, self.member_level,
                                   self.payment_method, self.order).moban(data,
                                                                          superior,
                                                                          ip, calculation_data,
                                                                          transaction_second_payagent_ratio,
                                                                          bind_buyer_relationship_data,
                                                                          reserve_fund=reserve_fund)
        else:
            expected_moban = MoBan(self.buyer_identity, self.seller_identity, self.member_level,
                                   self.payment_method, self.order).moban(data,
                                                                          superior,
                                                                          ip, calculation_data,
                                                                          transaction_second_payagent_ratio,
                                                                          bind_buyer_relationship_data,
                                                                          bind_payer_relationship_data,
                                                                          reserve_fund=reserve_fund)

        return expected_moban


if __name__ == '__main__':
    # superior = [{'个人焕商': 1000650}, {'省代理商': 1000646, '市代理商': 1000647, '区代理商': 1000648}]
    superior = {'储备池分佣': [{'个人焕商': 1000650}, {'省代理商': None, '市代理商': None, '区代理商': None}],
                '支付服务费分佣': [{'个人焕商': None}, {'市代理商': 103554, '区代理商': 1000029, '省代理商': 1000246}]}

    # proportion = {'个人分佣比例': Decimal('0.15'), '省分佣比例': Decimal('0.80'), '市分佣比例': Decimal('0.70'),
    #               '区分佣比例': Decimal('0.60')}
    proportion = {'储备池分佣': {'个人分佣比例': Decimal('0.15'), '省分佣比例': None, '市分佣比例': None, '区分佣比例': None},
                  '支付服务费分佣': {'市分佣比例': Decimal('0.70'), '区分佣比例': Decimal('0.60'), '省分佣比例': Decimal('0.80'),
                              '个人分佣比例': None}}

    buyer_province_proportion = proportion['储备池分佣']['省分佣比例']
    buyer_city_proportion = proportion['储备池分佣']['市分佣比例']
    buyer_area_proportion = proportion['储备池分佣']['区分佣比例']
    buyer_personal_proportion = proportion['储备池分佣']['个人分佣比例']

    disanfang_province_proportion = proportion['支付服务费分佣']['省分佣比例']
    disanfang_city_proportion = proportion['支付服务费分佣']['市分佣比例']
    disanfang_area_proportion = proportion['支付服务费分佣']['区分佣比例']
    disanfang_personal_proportion = proportion['支付服务费分佣']['个人分佣比例']

    reserve_fund = {'charge_amount': Decimal('300'), 'reserve_fund': Decimal('183.00')}

    charge_amount = reserve_fund['charge_amount']
    reserve_fun = reserve_fund['reserve_fund']

    ip = "192.168.0.101"

    data = {"buyer_phone": "17777777781", "seller_phone": 17777777776, "disanfang_phone": 13724765586, "买家": 1000656,
            "出钱方": 1000166, "卖家": 1000650, "平台": 10}

    calculation = ((Decimal('10.00'), Decimal('0.10'), Decimal('0.30')),
                   (Decimal('45.00'), Decimal('82.80'), Decimal('13.80'), Decimal('13.80'), Decimal('27.60')),
                   (Decimal('0.02'), Decimal('0.05'), Decimal('0.01'), Decimal('0.01'), Decimal('0.01')))

    order = "EC-2020060418121600012693"
    a = MoBan("公海用户", "个人焕商", "钻石会员", "抵工资", "EC-2020060418121600012693").moban(data,
                                                                                superior,
                                                                                ip, calculation,
                                                                                order, reserve_fun)
    print(a)
