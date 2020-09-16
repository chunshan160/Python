#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 11:45
# @Author :春衫
# @File :ratio.py

from Common.fengyong.sql.platform_promotion_ratio import platform_promotion_ratio
from Common.fengyong.sql.user_grade_apply import user_grade_ratio
from Common.fengyong.sql.user_special_ratio import user_special_ratio


def ratio(ip, user_id):
    global user_special_buy_cbp_ratio, user_special_buy_cash_ratio, user_special_sale_cash_ratio, platform_promotion_buy_cbp_ratio, platform_promotion_buy_cash_ratio, platform_promotion_sale_cash_ratio, buy_cbp_ratio, buy_cash_ratio, sale_cash_ratio

    # 查询用户的等级，获取等级支付服务费费率
    user_grade_ratio_data = user_grade_ratio(ip, user_id)
    user_grade_buy_cbp_ratio = user_grade_ratio_data[0]
    user_grade_buy_cash_ratio = user_grade_ratio_data[1]
    user_grade_sale_cash_ratio = user_grade_ratio_data[2]

    # 查询用户是否有临时费率
    user_special_ratio_data = user_special_ratio(ip, user_id)
    if user_special_ratio_data != None:
        user_special_buy_cbp_ratio = user_special_ratio_data[0]
        user_special_buy_cash_ratio = user_special_ratio_data[1]
        user_special_sale_cash_ratio = user_special_ratio_data[2]

    # 查询是否有活动费率
    platform_promotion_ratio_data = platform_promotion_ratio(ip)
    if platform_promotion_ratio_data != None:
        platform_promotion_buy_cbp_ratio = platform_promotion_ratio_data[0]
        platform_promotion_buy_cash_ratio = platform_promotion_ratio_data[1]
        platform_promotion_sale_cash_ratio = platform_promotion_ratio_data[2]

    # 根据三种情况判断最终使用的费率
    # 没有临时费率和活动费率，直接使用会员等级费率
    if user_special_ratio_data == None and platform_promotion_ratio_data == None:
        print("没有临时费率和活动费率，直接使用会员等级费率")
        buy_cbp_ratio = user_grade_buy_cbp_ratio
        buy_cash_ratio = user_grade_buy_cash_ratio
        sale_cash_ratio = user_grade_sale_cash_ratio

    # 有临时费率并且活动费率为空，直接使用临时费率
    elif user_special_ratio_data != None and platform_promotion_ratio_data == None:
        print("有临时费率并且活动费率为空，直接使用临时费率")
        buy_cbp_ratio = user_special_buy_cbp_ratio
        buy_cash_ratio = user_special_buy_cash_ratio
        sale_cash_ratio = user_special_sale_cash_ratio

    # 没有临时费率并且有活动费率，取会员等级和活动最低费率
    elif user_special_ratio_data == None and platform_promotion_ratio_data != None:
        print("没有临时费率并且有活动费率，取会员等级和活动最低费率")
        buy_cbp_ratio = min(user_grade_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
        buy_cash_ratio = min(user_grade_buy_cash_ratio, platform_promotion_buy_cash_ratio)
        sale_cash_ratio = min(user_grade_sale_cash_ratio, platform_promotion_sale_cash_ratio)

    # 有临时费率并且有活动费率，取临时和活动最低费率
    elif user_special_ratio_data != None and platform_promotion_ratio_data != None:
        print("有临时费率并且有活动费率，取临时和活动最低费率")
        buy_cbp_ratio = min(user_special_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
        buy_cash_ratio = min(user_special_buy_cash_ratio, platform_promotion_buy_cash_ratio)
        sale_cash_ratio = min(user_special_sale_cash_ratio, platform_promotion_sale_cash_ratio)

    return buy_cbp_ratio, buy_cash_ratio, sale_cash_ratio


if __name__ == '__main__':
    a = ratio("192.168.0.101", 1000166)
    print(a)
