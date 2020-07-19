#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/1/9 16:23
#@Author :春衫
#@File :SuperShop.py



class SC:
    #首页商超标签，为了左右滑动寻找商超
    home_sc_label = ("id",'//div[@class="van-swipe"]')
    home_sc = ("id",'//span[text()="焕焕商超"]')
    #底部的焕焕商超
    sc_all = ("id",'//p[text()="焕焕商超"]/..')
    #文本这么难定位，唯一图片总行了吧
    sc_select = ("id",'//img[@data-src="http://image.test.hobay.com.cn/group1/M00/07/6A/wKgAZV33HnaAY5rnAAV0hNc1ReM562!1035x525.png"]')
    #加入按钮
    sc_join = ("id",'//img[@src="/vuespa/static/img/super-add.60a654f.png"]')
    #选择商品 [1]提供已有商品   [2]选择需求商品    [3]所在地区
    provide_good = ("id",'//div[@class="van-cell van-cell--clickable van-hairline"]')
    #选择第一个 暂时没好的思路
    #或许可以搜索一个【唯一】商品标题的商品，再选择第一个
    #先这样吧
    good_name = ("id",'//input[@placeholder="输入关键字"]')
    good = ("id",'//div[@class="product-list border-bottom"]')
    confirm = ("id",'//input[@value="确认"]')
    #货品价值
    goods_value = ("id",'//div[@class="van-cell van-hairline"]')
    #所在地区
    location = ("id",'//div[@id="larea"]')
    determine = ("id",'//div[@class="area_btn larea_finish"]')
    sign_up_now = ("id",'//button[text()="立即报名"]')