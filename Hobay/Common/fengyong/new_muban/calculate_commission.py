#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/16 13:40
# @Author :春衫
# @File :calculate_commission.py


from decimal import *
from Common.fengyong.new_muban.get_two_float import get_two_float


def calculate_commission(second_payagent_ratio, bind_relationship_data, first_region_commission):
    '''

    Parameters
    ----------
    second_payagent_ratio：使用的二级分佣比例
    bind_relationship_data：绑定关系
    first_region_commission：一级所得分佣

    Returns：绑定的TCOid和分佣、上级销售id和分佣、销售上级销售id和分佣、最终所得分佣
    -------

    '''

    if second_payagent_ratio != None:

        if "业务焕商" or "销售" in bind_relationship_data:

            if "业务焕商" in bind_relationship_data:
                bing_sales_id = bind_relationship_data["业务焕商"]
                bing_sales_commission = second_payagent_ratio['free_sales_ratio'] * first_region_commission

            elif "销售" in bind_relationship_data:
                bing_sales_id = bind_relationship_data["销售"]
                bing_sales_commission = second_payagent_ratio['sales_ratio'] * first_region_commission
        else:
            bing_sales_id = None
            bing_sales_commission = Decimal('0.00')

        if bind_relationship_data.__contains__("TCO"):
            bing_TCO_id = bind_relationship_data["TCO"]
            bing_TCO_commission = second_payagent_ratio['tco_ratio'] * first_region_commission
        else:
            bing_TCO_id = None
            bing_TCO_commission = Decimal('0.00')

        if bind_relationship_data["买家上级的上级id"] != None:
            sales_bing_sales_id = bind_relationship_data["买家上级的上级id"]
            bing_sales_commission = bing_sales_commission / 2
            sales_bing_sale_commission = bing_sales_commission
        else:
            sales_bing_sales_id = None
            sales_bing_sale_commission = Decimal('0.00')

        bing_sales_commission = Decimal(get_two_float(bing_sales_commission, 2))
        sales_bing_sales_commission = Decimal(get_two_float(sales_bing_sale_commission, 2))
        bing_TCO_commission = Decimal(get_two_float(bing_TCO_commission, 2))

        finally_service_fee_commission = first_region_commission - bing_TCO_commission - bing_sales_commission - sales_bing_sales_commission
        finally_service_fee_commission = Decimal(get_two_float(finally_service_fee_commission, 2))
        return bing_TCO_id, bing_TCO_commission, bing_sales_id, bing_sales_commission, sales_bing_sales_id, sales_bing_sales_commission, finally_service_fee_commission

    else:
        return None


if __name__ == '__main__':
    second_payagent_ratio = {'agent_id': 1000348, 'sales_ratio': Decimal('0.30'), 'tco_ratio': Decimal('0.30'), 'free_sales_ratio': Decimal('0.00')}
    bind_relationship_data = {'销售': 1000519, 'TCO': 1000520, '买家上级的上级id': 1000515, '买家上级的上级身份': '销售'}
    first_region_commission = Decimal('5.00')
    a = calculate_commission(second_payagent_ratio, bind_relationship_data, first_region_commission)
    print(a)
