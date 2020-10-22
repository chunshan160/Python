#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/15 11:45
# @Author :春衫
# @File :ratio.py

from Common.fengyong.sql.platform_promotion_ratio import platform_promotion_ratio
from Common.fengyong.sql.user_grade_apply import user_grade_ratio
from Common.fengyong.sql.user_special_ratio import user_special_ratio
from Common.fengyong.sql.user_sale_special_ratio import user_sale_special_ratio
from Common.user_log import UserLog

my_logger = UserLog()

def ratio(ip, user_id):

    global user_special_buy_cbp_ratio, user_special_buy_cash_ratio, user_special_sale_cash_ratio, platform_promotion_buy_cbp_ratio, platform_promotion_buy_cash_ratio, platform_promotion_sale_cash_ratio, buy_cbp_ratio, buy_cash_ratio, sale_cash_ratio

    # 查询用户的等级，获取等级支付费率费率
    user_grade_ratio_data = user_grade_ratio(ip, user_id)
    user_grade_buy_cbp_ratio = user_grade_ratio_data[0]
    user_grade_buy_cash_ratio = user_grade_ratio_data[1]
    user_grade_sale_cash_ratio = user_grade_ratio_data[2]
    my_logger.info(f"用户等级采购易贝费率是：{user_grade_buy_cbp_ratio}，现金费率是：{user_grade_buy_cash_ratio}，销售现金费率是：{user_grade_sale_cash_ratio}")

    # 查询用户的临时采购费率
    user_special_ratio_data = user_special_ratio(ip, user_id)
    user_sale_special_ratio_data=user_sale_special_ratio(ip, user_id)
    if user_special_ratio_data != None:
        user_special_buy_cbp_ratio = user_special_ratio_data[0]
        user_special_buy_cash_ratio = user_special_ratio_data[1]
        my_logger.info(f"设置的临时采购易贝费率是：{user_special_buy_cbp_ratio}，现金费率是：{user_special_buy_cash_ratio}")

    # 查询用户的临时销售费率
    if user_sale_special_ratio_data !=None:
        user_special_sale_cash_ratio = user_sale_special_ratio_data
        my_logger.info(f"销售现金费率是：{user_special_sale_cash_ratio}")

    # 查询是否有活动费率
    platform_promotion_ratio_data = platform_promotion_ratio(ip)
    if platform_promotion_ratio_data != None:
        platform_promotion_buy_cbp_ratio = platform_promotion_ratio_data[0]
        platform_promotion_buy_cash_ratio = platform_promotion_ratio_data[1]
        platform_promotion_sale_cash_ratio = platform_promotion_ratio_data[2]
        my_logger.info(f"设置的活动采购易贝费率是：{user_special_buy_cbp_ratio}，现金费率是：{user_special_buy_cash_ratio}，销售现金费率是：{user_special_sale_cash_ratio}")

    # 根据情况判断最终使用的费率
    # 只设置了临时费率
    if user_special_ratio_data != None and platform_promotion_ratio_data == None:
        my_logger.info("只设置了临时费率")

        # 只设置了临时采购费率
        if user_special_buy_cbp_ratio != None and user_special_sale_cash_ratio == None:
            my_logger.info("只设置了临时采购费率")
            my_logger.info("采购费率按照后台设置的临时采购费率")
            buy_cbp_ratio = user_special_buy_cbp_ratio
            buy_cash_ratio = user_special_buy_cash_ratio
            my_logger.info("销售费率按照会员等级")
            sale_cash_ratio = user_grade_sale_cash_ratio

        # 只设置了临时销售费率
        elif user_special_buy_cbp_ratio == None and user_special_sale_cash_ratio != None:
            my_logger.info("只设置了临时销售费率")
            my_logger.info("采购费率按照会员等级")
            buy_cbp_ratio = user_grade_buy_cbp_ratio
            buy_cash_ratio = user_grade_buy_cash_ratio
            my_logger.info("销售费率按照后台设置的临时销售费率")
            sale_cash_ratio = user_special_sale_cash_ratio

        else:
            my_logger.info("设置了临时采购+销售费率")
            my_logger.info("采购费率按照后台设置的临时采购费率")
            buy_cbp_ratio = user_special_buy_cbp_ratio
            buy_cash_ratio = user_special_buy_cash_ratio
            my_logger.info("销售费率按照后台设置的临时销售费率")
            sale_cash_ratio = user_special_sale_cash_ratio

    # 只设置活动费率
    elif user_special_ratio_data == None and platform_promotion_ratio_data != None:
        my_logger.info("只设置活动费率")

        # 只设置了活动采购费率
        if platform_promotion_buy_cbp_ratio != None and platform_promotion_sale_cash_ratio ==None:
            my_logger.info("只设置了活动采购费率")
            my_logger.info("采购费率按照会员等级的采购费率和活动的采购费率做对比，谁低取谁")
            buy_cbp_ratio = min(user_grade_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
            buy_cash_ratio = min(user_grade_buy_cash_ratio, platform_promotion_buy_cash_ratio)
            my_logger.info("销售费率按照会员等级")
            sale_cash_ratio = user_grade_sale_cash_ratio

        # 只设置了活动销售费率
        elif platform_promotion_buy_cbp_ratio == None and platform_promotion_sale_cash_ratio !=None:
            my_logger.info("只设置了活动销售费率")
            my_logger.info("采购费率按照会员等级")
            buy_cbp_ratio = user_grade_buy_cbp_ratio
            buy_cash_ratio = user_grade_buy_cash_ratio
            my_logger.info("销售费率按照会员等级的销售费率和活动的销售费率做对比，谁低取谁")
            sale_cash_ratio = min(user_grade_sale_cash_ratio, platform_promotion_sale_cash_ratio)

        else:
            my_logger.info("设置了活动采购+销售费率")
            my_logger.info("采购费率按照按照会员等级的采购费率和活动的采购费率做对比，谁低取谁")
            buy_cbp_ratio = min(user_grade_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
            buy_cash_ratio = min(user_grade_buy_cash_ratio, platform_promotion_buy_cash_ratio)
            my_logger.info("销售费率按照按照会员等级的销售费率和活动的销售费率做对比，谁低取谁")
            sale_cash_ratio = min(user_grade_sale_cash_ratio, platform_promotion_sale_cash_ratio)

    # 设置了临时费率和活动费率
    elif user_special_ratio_data != None and platform_promotion_ratio_data != None:
        my_logger.info("设置了临时费率和活动费率")

        # 只设置了临时采购费率和活动采购费率
        if user_special_buy_cbp_ratio != None and platform_promotion_buy_cbp_ratio != None:
            my_logger.info("只设置了临时采购费率和活动采购费率")
            my_logger.info("采购费率按照临时采购费率和活动的采购费率做对比，谁低取谁")
            buy_cbp_ratio = min(user_special_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
            buy_cash_ratio = min(user_special_buy_cash_ratio, platform_promotion_buy_cash_ratio)
            my_logger.info("销售费率按照会员等级")
            sale_cash_ratio = user_grade_sale_cash_ratio

        # 只设置了临时采购费率和活动销售费率
        elif user_special_buy_cbp_ratio != None and platform_promotion_buy_cash_ratio != None:
            my_logger.info("只设置了临时采购费率和活动销售费率")
            my_logger.info("采购费率按照会员等级")
            buy_cbp_ratio = user_grade_buy_cbp_ratio
            buy_cash_ratio = user_grade_buy_cash_ratio
            my_logger.info("销售费率按照会员等级的销售费率和活动的销售费率做对比，谁低取谁")
            sale_cash_ratio = min(user_grade_sale_cash_ratio, platform_promotion_sale_cash_ratio)

        # 只设置了临时销售费率和活动采购费率
        elif user_special_sale_cash_ratio != None and platform_promotion_buy_cbp_ratio != None:
            my_logger.info("只设置了临时销售费率和活动采购费率")
            my_logger.info("采购费率按照会员等级的采购费率和活动的采购费率做对比，谁低取谁")
            buy_cbp_ratio = min(user_grade_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
            buy_cash_ratio = min(user_grade_buy_cash_ratio, platform_promotion_buy_cash_ratio)
            my_logger.info("销售费率按照后台设置的临时销售费率")
            sale_cash_ratio = user_special_sale_cash_ratio

        # 只设置了临时销售费率和活动销售费率
        elif user_special_sale_cash_ratio != None and platform_promotion_sale_cash_ratio != None:
            my_logger.info("只设置了临时销售费率和活动销售费率")
            my_logger.info("采购费率按照会员等级")
            buy_cbp_ratio = user_grade_buy_cbp_ratio
            buy_cash_ratio = user_grade_buy_cash_ratio
            my_logger.info("销售费率按照临时销售费率和活动的销售费率做对比，谁低取谁")
            sale_cash_ratio = min(user_special_sale_cash_ratio, platform_promotion_sale_cash_ratio)

        # 设置了临时采购+销售费率和活动采购+销售费率
        else:
            my_logger.info("设置了临时采购+销售费率和活动采购+销售费率")
            my_logger.info("采购费率按照临时采购费率和活动的采购费率做对比，谁低取谁")
            buy_cbp_ratio = min(user_special_buy_cbp_ratio, platform_promotion_buy_cbp_ratio)
            buy_cash_ratio = min(user_special_buy_cash_ratio, platform_promotion_buy_cash_ratio)
            my_logger.info("销售费率按照临时销售费率和活动的销售费率做对比，谁低取谁")
            sale_cash_ratio = min(user_special_sale_cash_ratio, platform_promotion_sale_cash_ratio)

    # 没有设置临时费率和活动费率
    else:
        my_logger.info("没有设置临时费率和活动费率")
        my_logger.info("采购费率按照会员等级")
        buy_cbp_ratio = user_grade_buy_cbp_ratio
        buy_cash_ratio = user_grade_buy_cash_ratio
        my_logger.info("销售费率按照会员等级")
        sale_cash_ratio = user_grade_sale_cash_ratio

    my_logger.info(f"最终使用的采购易贝费率是：{float(buy_cbp_ratio)}，现金费率是：{float(buy_cash_ratio)}，销售现金费率是：{float(sale_cash_ratio)}")
    return float(buy_cbp_ratio), float(buy_cash_ratio), float(sale_cash_ratio)


if __name__ == '__main__':
    a = ratio("192.168.0.102", 1000504)
    print(a)
