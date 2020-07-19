#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/6/12 12:43
# @Author :春衫
# @File :XunZhao.py

from decimal import *


def xunzhao(data):
    '''

    Parameters
    ----------
    data：省市区平台二级分佣比例

    Returns
    -------

    '''

    if len(data) == 3:
        area_ratio = data[2]
        city_ratio = data[1]
        province_ratio = data[0]

        if area_ratio['sales_ratio'] == Decimal('0.00') and area_ratio['tco_ratio'] == Decimal('0.00') and \
                area_ratio['free_sales_ratio'] == Decimal('0.00'):
            if city_ratio['sales_ratio'] == Decimal('0.00') and city_ratio['tco_ratio'] == Decimal('0.00') and \
                    city_ratio['free_sales_ratio'] == Decimal('0.00'):
                if province_ratio['sales_ratio'] == Decimal('0.00') and province_ratio['tco_ratio'] == Decimal(
                        '0.00') and province_ratio['free_sales_ratio'] == Decimal('0.00'):
                    return None
                else:
                    return province_ratio
            else:
                return city_ratio
        else:
            return area_ratio

    elif len(data) == 2:
        city_ratio = data[1]
        province_ratio = data[0]

        if city_ratio['sales_ratio'] == Decimal('0.00') and city_ratio['tco_ratio'] == Decimal('0.00') and \
                city_ratio[
                    'free_sales_ratio'] == Decimal('0.00'):
            if province_ratio['sales_ratio'] == Decimal('0.00') and province_ratio['tco_ratio'] == Decimal(
                    '0.00') and province_ratio[
                'free_sales_ratio'] == Decimal('0.00'):
                return None
            else:
                return province_ratio
        else:
            return city_ratio
    else:
        if data!=():
            ratio = data[0]
            if ratio['sales_ratio'] == Decimal('0.00') and ratio['tco_ratio'] == Decimal(
                    '0.00') and ratio[
                'free_sales_ratio'] == Decimal('0.00'):
                return None
            else:
                return data
        else:
            return None


if __name__ == '__main__':
    data = {'TCO': 1000649, '买家上级的上级': None}

    a = xunzhao(data)
    print(a)
