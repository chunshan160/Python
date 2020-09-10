#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/8 21:47
# @Author :春衫
# @File :title.py

from tools.cishu import CiShu


class Title:

    def __init__(self, buyer_identity, seller_identity, payment_method):
        self.buyer_identity = buyer_identity  # 买家身份 1公海用户 2非公海用户
        self.seller_identity = seller_identity  # 卖家身份 1个人焕商 2区域代理 3公海用户 4非公海用户
        self.payment_method = payment_method

    def title(self, superior):
        global personal, personal1, personal2, fenrun

        # 储备池分给了几个人 服务费分给了几个人
        cishu = CiShu().cishu(self.payment_method, superior)

        b = ['购买商品：扣除买家储备金']
        for i in range(0, cishu[0]):
            fenrun = ('购买商品：代理商分佣金额（激励金）收入')
            b.append(fenrun)

        if self.payment_method in ['易贝', '抵工资', '家人购']:

            # 因为家人购文案不加家人购，而是叫亲情
            if self.payment_method == "家人购":
                self.payment_method = "亲情"

            a = ['{0}购买商品：扣除买家订单易贝金额'.format(self.payment_method),
                 '{0}购买商品：扣除买家易贝服务费'.format(self.payment_method),
                 '{0}购买商品：扣除买家现金服务费'.format(self.payment_method),
                 '{0}购买商品：扣除买家订单易贝金额转入平台'.format(self.payment_method),
                 '{0}购买商品：扣除买家易贝服务费转入平台'.format(self.payment_method),
                 '{0}购买商品：扣除买家现金服务费转入平台'.format(self.payment_method),
                 '{0}购买商品：订单易贝金额从平台转出'.format(self.payment_method),
                 '{0}购买商品:扣除买家订单易贝金额转给卖家'.format(self.payment_method)]

            if self.payment_method == '易贝':

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    c = ['{0}购买商品：扣除买家易贝服务费分润(服务费)总金额支出'.format(self.payment_method)]
                    for i in range(0, cishu[0]):
                        fenrun = ('{0}购买商品：扣除买家易贝服务费分润'.format(self.payment_method))
                        c.append(fenrun)
                    payment_method_data = a + b + c

                else:
                    c = ['{0}购买商品：扣除买家易贝服务费分润(服务费)总金额支出'.format(self.payment_method)]
                    for i in range(0, cishu[0]):
                        fenrun = ('{0}购买商品：扣除买家易贝服务费分润'.format(self.payment_method))
                        c.append(fenrun)
                    payment_method_data = a + c

            else:  # 抵工资 家人购

                if self.payment_method == "抵工资":
                    c = ['抵工资购买商品：扣除买家易贝服务费分润(服务费)总金额支出']
                    for i in range(0, cishu[1]):
                        fenrun = ('抵工资购买商品：扣除买家易贝服务费分润')
                        c.append(fenrun)
                else:
                    c = ['亲情购买商品：扣除买家易贝服务费进行分润(服务费)总金额支出']
                    for i in range(0, cishu[1]):
                        fenrun = ('亲情购买商品：扣除买家易贝服务费进行分润')
                        c.append(fenrun)

                if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                        self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                    payment_method_data = a + b + c

                else:
                    payment_method_data = a + c


        elif self.payment_method == "易贝券":
            a = ['{0}支付购物商品费用：扣除买家订单易贝金额'.format(self.payment_method),
                 '{0}支付购物商品费用：扣除买家订单易贝金额转入平台'.format(self.payment_method),
                 '{0}支付购物商品费用：订单易贝金额从平台转出'.format(self.payment_method),
                 '{0}支付购物商品费用:扣除买家订单易贝金额转给卖家'.format(self.payment_method)]
            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                payment_method_data = a + b
            else:
                payment_method_data = a


        else:  # 现金、微信、支付宝
            a = ['{0}支付购物商品费用：扣除买家订单金额（现金）'.format(self.payment_method),
                 '{0}支付购物商品费用：扣除买家订单金额（现金）转入平台(卖家实际应收到的金额)'.format(self.payment_method),
                 '{0}支付购物商品费用：扣除卖家（现金）服务费转入平台'.format(self.payment_method),
                 '{0}支付购物商品费用：扣除买家订单金额（现金）转从平台(卖家实际应收到的金额)转出'.format(self.payment_method),
                 '{0}支付购物商品费用：扣除买家订单金额（现金）转给卖家(全部)'.format(self.payment_method),
                 '{0}支付购物商品费用：从卖家现金账户扣除（现金）服务费'.format(self.payment_method)]

            if (self.buyer_identity == "公海用户" and self.seller_identity == "个人焕商") or (
                    self.buyer_identity == "公海用户" and self.seller_identity == "非焕商且已绑定个人焕商"):
                c = ['{0}支付购物商品费用：扣除买家现金服务费分润(服务费)总金额支出'.format(self.payment_method)]
                for i in range(0, cishu[1]):
                    fenrun = ('{0}支付购物商品费用：扣除买家现金服务费分润'.format(self.payment_method))
                    c.append(fenrun)
                payment_method_data = a + b + c

            else:
                c = ['{0}支付购物商品费用：扣除买家现金服务费分润(服务费)总金额支出'.format(self.payment_method)]
                for i in range(0, cishu[1]):
                    fenrun = ('{0}支付购物商品费用：扣除买家现金服务费分润'.format(self.payment_method))
                    c.append(fenrun)
                payment_method_data = a + c

        return payment_method_data


if __name__ == '__main__':
    data = {"buyer_phone": "17777777781", "买家": 1000656, "卖家": 1000650, "平台": 10, "个人焕商": 1000650}
    a = Title("公海用户", "区域焕商", "易贝").title(data)
    print(a)
