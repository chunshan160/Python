#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:01
#@Author :春衫
#@File :coupon_good.py


'''
发布商品-本地生活
'''

# 商品主图
product_image = ("id", "com.ecloud.hobay:id/iv_add_pic")
# 选择图片
check_image = ("id", "com.ecloud.hobay:id/cb_check")
# 点击确定
btn_ok = ("id", "com.ecloud.hobay:id/btn_ok")
# 商品标题
product_title = ("id", "com.ecloud.hobay:id/et_product_title")
# 商品详情
product_description = ("id", "com.ecloud.hobay:id/et_product_desc")
# 分类
category = ("id", "com.ecloud.hobay:id/tv_select_type")
# 二级分类
second_categpry = ("id", "com.ecloud.hobay:id/tv_list_name")
# 三级分类
third_categpry = ("id", "com.ecloud.hobay:id/tv_show_name")
# 点击券类
coupon = ("id", "com.ecloud.hobay:id/tv_select_volume")
# 卡券类型
coupon_categpry = ("class_name", "android.widget.TextView")
# 价格
total_price = ("id", "com.ecloud.hobay:id/et_product_price")
# 库存
stock = ("id", "com.ecloud.hobay:id/et_product_number")
# 限购数量
limit_quantity = ("id", "com.ecloud.hobay:id/et_buy_num")
# 立即上架
submit = ("id", "com.ecloud.hobay:id/btn_immediately_publish")
# 放入仓库
storage = ("id", "com.ecloud.hobay:id/btn_into_warehouse")
# 错误提示
error_toast = ("xpath", '//*[contains(text(),"请输入商品标题")]')