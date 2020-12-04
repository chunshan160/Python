#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/24 17:07
# @Author :春衫
# @File :ceshi.py
import grequests
import requests

login_url = 'http://m.dev1.hobay.com.cn/api/app/user/login'  # 登录
login_data = {"loginValidateType":"PASSWORD","phone":"13724765586","validateValue":"qaz123"}
login_res = requests.post(login_url, json=login_data)
print("登录结果是：", login_res.json())

url3="http://m.dev1.hobay.com.cn/ribbon-api/product/no_getProductById?id=1077969"
res3=requests.get(url3,headers={"login":""},cookies=login_res.cookies)
print(res3.json())

version=res3.json()['results']['result']['version']
print(version)


product_data={"id":1077969,"_id":1077969,"taskId":None,"name":None,"title":"焕友圈评论","parentCategoryId":100,"parentCategory":{"id":100,"_id":100,"name":"大家电","imageUrl":"","parentId":1,"tagId":0,"score":40,"status":1,"orders":None,"circulate":1,"deleted":None},"categoryId":101,"category":{"name":"电视","id":101},"firstCategory":1,"conditions":1,"price":1,"discountPrice":None,"companyId":None,"companyName":None,"companyLogo":None,"companySalesNum":10,"brandId":None,"address":None,"remark":"已有商品复制进云仓","putaway":1,"deliveryWay":None,"afterSaleGuarantee":None,"freight":1,"description":"11111","userId":1000166,"createTime":1606204905045,"updateUser":-1,"updateTime":1606204922955,"recommend":None,"orders":0,"status":1,"reviewStatus":"REVIEW_PASS","renqi":10,"sales":0,"sellWay":0,"cardType":0,"companyReview":None,"discount":None,"collection":None,"virtual":None,"lat":23.151759,"lon":113.407572,"distance":None,"locationName":None,"province":"广东省","city":"广州市","area":"天河区","version":3,"limitBuyQty":"","limitBuyPeriod":"","productAttribute":{"dateManufactureStart":0,"dateManufactureEnd":0,"manufacturer":"","brand":"","placeOrigin":"","productionLicenseUmber":"","qualityGuaranteePeriod":0},"productImages":[{"id":79345,"_id":79345,"productId":1077969,"orders":0,"imageUrl":"/group1/M00/07/6E/wKgAZl2tIdWAShoHAAAlwUXpyvg47!391x258.jpeg"}],"productDetailImages":[],"specificationWithStockSkus":[{"id":None,"_id":None,"name":"白","attribute":None,"specificationNameSort":0,"productStockSkus":[{"id":982672,"_id":982672,"productStockId":360239,"specificationId":1285,"value":"白","productId":1077969,"name":"白","specificationNameSort":0,"imageUrl":"/group1/M00/07/6E/wKgAZl2tIdWAShoHAAAlwUXpyvg47!391x258.jpeg","qtyVisible":1}]}],"productStockWithStockImages":[{"appTag":0,"price":1,"productStockImage":{"imageUrl":"/group1/M00/07/6E/wKgAZl2tIdWAShoHAAAlwUXpyvg47!391x258.jpeg"},"productStockSkuWithSpecifications":[{"specification":{"name":"白"},"value":"白","id":982672}],"qty":99,"buyingPrice":"1","usableQty":99,"id":360239}],"productStocts":[{"id":360239,"_id":360239,"productId":1077969,"qty":99,"usableQty":99,"price":1,"updateTime":None,"createTime":1606204905072,"discountPrice":None,"buyingPrice":None,"swapTime":None,"deleted":"false","swap":"false"}],"barterCircle":-1,"startTime":None,"endTime":None,"barterCircleTitle":None,"barterCircleId":None,"valid":1,"currentSystemTime":1606204983190,"minPrice":1,"maxPrice":1,"mainStorageId":2434,"storageTitle":None,"updateLimitTime":1606204905045,"sourceType":"HOBAY","productType":None,"productTitle":"焕友圈评论","categoryName":"电视","isPublish":"false","skuEdit":1}

url="http://m.dev1.hobay.com.cn/ribbon-api/product/editProduct"
# res=requests.post(url, json=product_data,headers={"login":""},cookies=login_res.cookies)
req_list = [grequests.post(url, json=product_data,headers={"login":""},cookies=login_res.cookies) for i in range(5)]
res_list = grequests.map(req_list)
print(res_list)



