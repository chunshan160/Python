#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/29 10:33
# @Author :春衫
# @File :录入客户.py

from http_request import HttpRequest


def input_user(login_phone, input_phone):
    # 登录
    global login_type
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": login_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 录入客户
    input_data = {"area": "", "city": "", "company": "大", "detailedAddress": "",
                  "headImage": "/group1/M00/07/AC/wKgAZV8zdWaAFK94AARVJeKqSr452!1280x959.jpeg", "name": "测试",
                  "partnerStatus": 0, "phone": input_phone, "position": "", "province": ""}
    input_url = "http://m.test.hobay.com.cn/ribbon-api/customer/saveCustomer"
    headers = {"login": ""}
    input_res = HttpRequest().http_request(input_url, "post", json=input_data, cookies=login_res.cookies,
                                           headers=headers, )
    print("录入客户的结果是：", input_res.json())

    # 注册
    register_url = "http://m.test.hobay.com.cn/api/app/user/register"
    register_data = {"code": "666666", "loginBindingType": "PHONE", "phone": input_phone}
    register_res = HttpRequest().http_request(register_url, "post", json=register_data, cookies=login_res.cookies,
                                              headers=headers)
    print("录入客户注册的结果是：", register_res.json())
    register_id = register_res.json()["userId"]
    print("录入客户的user_id是：", register_id)

    # 完善资料
    info_url = "http://m.test.hobay.com.cn/api/app/user/perfectUserInfo"
    info_data = {"country": "中国", "province": "青海省", "city": "西宁市", "area": "城中区"}
    info_res = HttpRequest().http_request(info_url, "post", json=info_data, cookies=register_res.cookies,
                                          headers=headers)
    print("录入客户完善资料的结果是：", info_res.json())

    # 我的客户
    MyCustomer_url = "http://m.test.hobay.com.cn/ribbon-api/customer/getQueryPageMyCustomer?status=&currentPage=1&pageSize=20"
    MyCustomer_headers = {"login": ""}
    MyCustomer_res = HttpRequest().http_request(MyCustomer_url, "get", headers=MyCustomer_headers,
                                                cookies=login_res.cookies)
    # print("我的客户中的客户有：", MyCustomer_res.json())

    # 判断绑定的我的客户是否激活
    MyCustome_data = MyCustomer_res.json()["data"]['result']
    for i in range(len(MyCustome_data)):
        if MyCustome_data[i]["phone"] == str(input_phone):
            partnerStatus = MyCustome_data[i]["partnerStatus"]
            if partnerStatus == 1:
                print(f"{input_phone}激活成功")
            else:
                print(f"{input_phone}激活失败，partnerStatus={partnerStatus}")
            break

    return register_id


def parner(login_phone, input_phone,input_user_id):
    # 登录
    global login_type
    login_url = 'http://m.test.hobay.com.cn/api/app/user/login'  # 登录
    login_data = {"loginValidateType": "CODE", "phone": login_phone, "validateValue": "666666"}
    login_res = HttpRequest().http_request(login_url, "post", json=login_data)
    print("登录结果是：", login_res.json())

    # 伙伴列表类型
    parner_type_url = "http://m.test.hobay.com.cn/api/user/partnership/getPartnerType"
    parner_typer_headers = {"login": ""}
    parner_type_res = HttpRequest().http_request(parner_type_url, "get", headers=parner_typer_headers,
                                                 cookies=login_res.cookies)
    parner_type = parner_type_res.json()["partnerStyle"]

    if parner_type == "NORMAL" or parner_type == "ADVANCED" or parner_type == "ANGEL":
        login_type = "正式个人焕商"
    elif parner_type == "PERSON":
        login_type = "非正式焕商"
    elif parner_type == "AGENT":
        login_type = "区域焕商"
    print(f"登录的用户是：{login_type}")

    # 正式焕商正式伙伴/非正式伙伴/区域焕商 搜索伙伴 都是用这个接口
    search_parner_url = f"http://m.test.hobay.com.cn/api/user/partnership/queryPageLittlePartner?name={input_phone}&pageSize=10&page=1"
    search_parner_headers = {"login": ""}
    search_parner_res = HttpRequest().http_request(search_parner_url, "get", headers=search_parner_headers,
                                                   cookies=login_res.cookies)
    # print("我的伙伴-搜索伙伴的结果是：", search_parner_res.json())
    parner_data = search_parner_res.json()["recordList"]

    # 查得出来就是绑定了，查不出来可能是待转正伙伴，也可能是没绑
    if len(parner_data) == 1:
        print("搜索查询到了一条数据")
        if parner_data[0]["id"] == str(input_user_id):
            if login_type == "正式个人焕商" or login_type == "区域焕商":
                print(parner_data[0]["validDay"])
                if parner_data[0]["validDay"] == None:
                    print(f"{input_phone}已经和{login_phone}绑定，是他的正式伙伴")
                else:
                    print("正式焕商的正式伙伴有绑定有效期，数据异常")
            elif login_type == "非正式焕商":
                if parner_data[0]["validDay"] != None:
                    print(f"{input_phone}是{login_phone}的非正式伙伴")
                else:
                    print("非正式焕商的伙伴没有绑定有效期，数据异常")
        else:
            print("搜索查询数据id对不上，数据异常")
    else:
        if login_type == "正式个人焕商":
            print(f"{input_phone}不是{login_phone}的正式伙伴")
            # 正式焕商待转正伙伴
            search_parner2_url = f"http://m.test.hobay.com.cn/api/user/partnership/queryPartnerShipBack?name={input_phone}&pageSize=10&page=1"
            search_parner2_res = HttpRequest().http_request(search_parner2_url, "get",
                                                            headers=search_parner_headers,
                                                            cookies=login_res.cookies)
            print("我的伙伴-待转正伙伴-搜索伙伴的结果是：", search_parner2_res.json())
            parner2_data = search_parner2_res.json()["recordList"]
            if len(parner2_data) == 1:
                if parner2_data[0]["id"] == int(input_user_id):
                    if parner2_data[0]["validDay"] != None:
                        print(f"{input_phone}是{login_phone}的待转正伙伴")
                    else:
                        print(f"数据异常")
                else:
                    print("数据异常")
            else:
                print(f"{input_phone}没有和{login_phone}绑定")
        else:
            print(f"{input_phone}没有和{login_phone}绑定")


if __name__ == '__main__':
    login_phone=88888888888
    input_phone=17777777718
    # input_user_id =1001363
    input_user_id=input_user(login_phone, input_phone)
    parner(login_phone, input_phone,input_user_id)