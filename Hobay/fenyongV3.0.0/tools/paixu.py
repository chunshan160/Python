#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/18 14:33
# @Author :春衫
# @File :paixu.py

from tools.quchong import quchong

#获取最小的省/市/区分佣比例
def paixu(province_proportion, city_proportion, area_proportion):
    '''

    :param province_proportion: 省分佣比例
    :param city_proportion: 市分佣比例
    :param area_proportion: 区分佣比例
    :return: 最小的分佣比例
    '''

    if province_proportion == None:
        province_proportion = 0
    if city_proportion == None:
        city_proportion = 0
    if area_proportion == None:
        area_proportion = 0

    proportion = [province_proportion, city_proportion, area_proportion]
    proportion=quchong(proportion,0)
    min_proportion = min(proportion)
    return min_proportion

if __name__ == '__main__':
    a=paixu(None,None,None)
    print(a)
