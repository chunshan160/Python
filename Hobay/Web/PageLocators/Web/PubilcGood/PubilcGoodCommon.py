#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/10 13:00
#@Author :春衫
#@File :PubilcGoodCommon.py

from selenium.webdriver.common.by import By

'''
发布商品
'''

# 点击发布实物商品
entity_good = (By.XPATH, '//span[@class="btn material-btn"]')
# 点击发布本地生活
coupon_good = (By.XPATH, '//span[@class="btn business-btn"]')
# 点击发布商企服务
services_good = (By.XPATH, '//span[@class="btn service-btn"]')


'''
公共定位
'''

# 商品主图
product_image = (By.ID, "com.ecloud.hobay:id/iv_add_pic")
# 选择图片
check_image = (By.ID, "com.ecloud.hobay:id/cb_check")
# 点击确定
btn_ok = (By.ID, "com.ecloud.hobay:id/btn_ok")



# 分类
category = (By.ID, "com.ecloud.hobay:id/tv_select_type")
# 二级分类
second_category = (By.XPATH, '//div[text()="{}"]')
# 三级分类
third_category = (By.XPATH, '//li[text()="{}"]')

#限购选项
Purchase_limit=(By.XPATH,'//div[text()="默认不限购"]')
#控制按钮
Purchase_limit_button=(By.XPATH,'(//div[@class="van-radio"])[{}]')
#限购件数
limit_quantity = (By.XPATH, '//input[@placeholder="请输入限购数量"]')
#限购周期
limit_time = (By.XPATH, '//input[@placeholder="限购天数"]')

# 立即上架
submit = (By.CLASS_NAME, "submit-sell")
# 放入仓库
storage = (By.CLASS_NAME, "submit-storage")
# 错误提示
error_toast = (By.XPATH, '//*[contains(text(),"请输入商品标题")]')
