#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2019/12/28 13:48
# @Author :春衫
# @File :PublishGoodspage_Locators.py




# 公共
class PubilcGood:

    def pubilc_good(self):

        # 首页点击发布商品
        publish_goods = (MobileBy.ID, '//i[@class="cart-icon"]')
        # 点击发布实物商品
        entity_good = (MobileBy.ID, '//span[@class="btn material-btn"]')
        # 点击发布本地生活
        coupon_good = (MobileBy.ID, '//span[@class="btn business-btn"]')
        # 点击发布商企服务
        services_good = (MobileBy.ID, '//span[@class="btn service-btn"]')


        # 上传图片的脚本
        path = ('D:\Pycharm_workspace\web_test\image.exe')
        # 立即上架
        submit = (MobileBy.ID, '//div[@class="submit-sell"]')
        # 放入仓库
        storage = (MobileBy.ID, '//div[@class="submit-storage"]')


    # 实物类
    def entity_good(self):
        # 商品主图
        product_image = (MobileBy.ID, '//form[@class="upload-box"]')
        # 商品标题
        product_title = (MobileBy.ID, '//textarea[@placeholder="输入商品标题"]')
        # 商品描述
        product_detail = (MobileBy.ID, '//label[text()="商品描述"]//parent::div')
        # 商品详情内容
        product_description = (MobileBy.ID, '//textarea')
        # 商品详情图片
        product_description_image = (MobileBy.ID, 'upload-btn')
        # 完成按钮
        finish = (MobileBy.ID, 'fin-btn')
        # 品相
        quality = (MobileBy.ID, '//label[text()="品相"]//parent::div')
        # 品相-全新
        quality_new = (MobileBy.ID, '//*[contains(text(),"全新")]//span')
        # 分类
        category = (MobileBy.ID, '//label[text()="分类"]//parent::div')
        # 二级分类
        second_categpry = (MobileBy.ID, '//div[text()="大家电2"]')
        # 三级分类
        third_categpry = (MobileBy.ID, '//li[text()="电视"]')
        # 商品类型
        product_type = (MobileBy.ID, '//label[text()="商品类型"]//parent::div')
        # 商品类型-易贝商品
        product_type_select = (MobileBy.ID, '//*[contains(text(),"易贝商品")]//span')
        # 规格
        specification = (MobileBy.ID, '//*[contains(text(),"规格")]//parent::div')
        # 规格_1_2
        property_1 = (MobileBy.ID, 'id_0')
        property_2 = (MobileBy.ID, 'id_0_0')
        # 规格图片
        specification_image = (MobileBy.ID, '//*[contains(text(),"上传图片")]')
        # 下一步
        next = (MobileBy.ID, '//*[contains(text(),"下一步")]')
        # 进货价
        purchase_price = (MobileBy.ID, 'skuTb_id_0')
        # 销售价
        sell_price = (MobileBy.ID, 'skuTb_id_1')
        # 库存
        stock = (MobileBy.ID, 'skuTb_id_2')
        # 确定按钮
        determine = (MobileBy.ID, '//div[@class="fin-btn"]//div[contains(text(),"确定")]')
        # 运费
        fare = (MobileBy.ID, '//label[text()="运费"]//parent::div')
        # 运费-包邮
        fare_manner = (MobileBy.ID, '//*[contains(text(),"包邮")]//span')
        # 限购数量
        limit_quantity = (MobileBy.ID, '//input[@placeholder="默认不限"]')
        # 上传图片的脚本
        path = ('D:\Pycharm_workspace\web_test\image.exe')
        # 立即上架
        submit = (MobileBy.ID, '//div[@class="submit-sell"]')
        # 放入仓库
        storage = (MobileBy.ID, '//div[@class="submit-storage"]')


    def coupon_good(self):
        # 商品主图
        product_image = (MobileBy.ID, '//form[@class="upload-box"]')
        # 商品标题
        product_title = (MobileBy.ID, '//textarea[@placeholder="请输入标题"]')
        # 商品详情
        product_description = (MobileBy.ID, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
        # 分类
        categpry = (MobileBy.ID, '//label[text()="分类"]//parent::div')
        # 二级分类
        second_categpry = (MobileBy.ID, '//div[text()="酒水"]')
        # 三级分类
        third_categpry = (MobileBy.ID, '//li[text()="红酒"]')
        # 点击券类
        coupon = (MobileBy.ID, '//label[text()="券类"]//parent::div')
        # 卡券类型
        coupon_categpry = (MobileBy.ID, '//li[text()="代金券"]')
        # 确认按钮
        determine = (MobileBy.ID, '//div[contains(text(),"确认")]')
        # 总价
        total_price = (MobileBy.ID, '//input[@placeholder="商品总价"]')
        # 库存
        stock = (MobileBy.ID, '//input[@placeholder="商品库存"]')
        # 限购数量
        limit_quantity = (MobileBy.ID, '//input[@placeholder="默认不限"]')
        # 上传图片的脚本
        path = ('D:\Pycharm_workspace\web_test\image.exe')
        # 立即上架
        submit = (MobileBy.ID, '//div[@class="submit-sell"]')
        # 放入仓库
        storage = (MobileBy.ID, '//div[@class="submit-storage"]')


    def services_good(self):
        # 商品主图
        product_image = (MobileBy.ID, '//form[@class="upload-box"]')
        # 商品标题
        product_title = (MobileBy.ID, '//textarea[@placeholder="请输入标题"]')
        # 商品详情
        product_description = (MobileBy.ID, '//textarea[@placeholder="商品描述，请详细介绍您所出的服务内容"]')
        # 分类
        categpry = (MobileBy.ID, '//label[text()="分类"]//parent::div')
        # 二级分类
        second_categpry = (MobileBy.ID, '//div[text()="设计"]')
        # 三级分类
        third_categpry = (MobileBy.ID, '//li[text()="广告设计"]')
        # 总价
        total_price = (MobileBy.ID, '//input[@placeholder="商品总价"]')
        # 预付款
        subsist = (MobileBy.ID, '//input[@placeholder="预先支付的款项"]')
        # 库存
        stock = (MobileBy.ID, '//input[@placeholder="商品库存"]')
        # 限购数量
        limit_quantity = (MobileBy.ID, '//input[@placeholder="默认不限"]')
        # 上传图片的脚本
        path = ('D:\Pycharm_workspace\web_test\image.exe')
        # 立即上架
        submit = (MobileBy.ID, '//div[@class="submit-sell"]')
        # 放入仓库
        storage = (MobileBy.ID, '//div[@class="submit-storage"]')
