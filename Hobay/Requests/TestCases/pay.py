#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/29 0029 11:22
#@Author :dongdong
#@File :pay.py

import time
from http_request import HttpRequest

def buy(buyer_phone,seller_phone):
     # 买家登录
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": buyer_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    #已得拍接口
    haveAction_url='http://m.test.hobay.com.cn/ribbon-api/auctionOlBid/haveAction?currentPage=1&pageSize=10'
    headers={'login':''}
    haveAction_res=HttpRequest().http_request(haveAction_url,'get',headers=headers,cookies=login_res.cookies)
    print('得拍数据',haveAction_res.json())

     #找到得拍拍品
    paipin_url='http://m.test.hobay.com.cn/ribbon-api/orders/saveOrderForAuction?auctionOlBidId=1435'
    paipin_headers={'login': ''}
    paipin_res=HttpRequest().http_request(paipin_url,"get",headers=paipin_headers,cookies=login_res.cookies)
    print("得到订单id",paipin_res.json())

    # #得拍者支付拍品
    # order_url='http://m.test.hobay.com.cn/ribbon-api/orders/getOrder'
    # a = haveAction_res.json()['data']['result'][0]['orderId']
    # print(a)
    # order_id={'orderId': a}
    # headers={'login': ''}
    # order_res=HttpRequest().http_request(order_url,'get',params=order_id,headers=headers,cookies=login_res.cookies)
    # print("订单详情",order_res.json())

    #得拍者支付订单
    zhifu_url="http://m.test.hobay.com.cn/ribbon-api/batchOrders/payAllCBP"
    zhifu_headers={'login': '','payPassword': 'OH8lKuLTcZc='}
    b=paipin_res.json()['data']['tradeNum']
    print(b)
    zhifu_data={"tradeNUm":b,"payType":3,"shareWalletUserId":"","shareWalletId":""}
    zhifu_res = HttpRequest().http_request(zhifu_url, 'post',json=zhifu_data, headers=zhifu_headers,
                                            cookies=login_res.cookies)
    print("支付成功", zhifu_res.json())

     #卖家登录
    login_seller_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_seller_data = {"loginValidateType": "CODE", "phone": seller_phone, "validateValue": "666666"}
    login_seller_res = HttpRequest().http_request(login_seller_url, "post", json=login_seller_data)
    print("登录结果是：", login_seller_res.json())

    #销售订单列表接口
    sales_url = 'http://m.test.hobay.com.cn/ribbon-api/batchOrders/queryPageOrders'  # 登录
    sales_data = {'orderStatus':0,'buyOrSell':2,'type':0,'currentPage':1,'pageSize':10}
    sales_headers={'login': ''}
    sales_res = HttpRequest().http_request(sales_url, "post", data=sales_data,headers=sales_headers,cookies=login_seller_res.cookies)
    # print("销售订单列表：", sales_res.json())

    #立即发货
    fahuo_url='http://m.test.hobay.com.cn/orders/sendProduct'
    buyer_userId= login_res.json()['userId']
    orderId=paipin_res.json()['data']['orderId']
    fahou_data={'orderId':orderId,'payType':3,'buyerUserId':buyer_userId,'type':1,'logisticsCompany':'德邦物流','companyNum':'debangwuliu','logisticsNum':'123456789'}
    fahuo_headers={'login': ''}
    fahuo_res=HttpRequest().http_request(fahuo_url,'post',data=fahou_data,headers=fahuo_headers,cookies=login_seller_res.cookies)
    print('卖家发货成功',fahuo_res.json())


    # #买家登录点击采购订单
    # buyer_url='http://m.test.hobay.com.cn/ribbon-api/batchOrders/queryPageOrders'
    # buyer_data= {'orderStatus':0,'buyOrSell':2,'type':0,'currentPage':1,'pageSize':10}
    # buyer_headers={'login': ''}
    # buyer_res=HttpRequest().http_request(buyer_url,'post',data=buyer_data,headers=buyer_headers,cookies=login_res.cookies)
    # # print('采购订单',buyer_res.json())

    #确认收货
    suer_url='http://m.test.hobay.com.cn/ribbon-api/orders/recieve'
    sellerUserId=login_seller_res.json()['userId']
    suer_data={'orderId':orderId,'payType':3,'sellerUserId':sellerUserId}
    suer_headers={'login': '','payPassword': 'OH8lKuLTcZc='}
    suer_res = HttpRequest().http_request(suer_url, 'post', data=suer_data, headers=suer_headers,
                                            cookies=login_res.cookies)
    print('确认收货订单', suer_res.json())
if __name__=='__main__':
    buy(13570258645,15999951551)

