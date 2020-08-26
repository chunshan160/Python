#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/8/18 11:29
# @Author :春衫
# @File :damogu.py

import requests


def test(phone,password,openId):
    '''

    :param phone: 手机号
    :param password: 加密后的密码
    :param openId: 加密后的支付密码
    :return:
    '''

    # 投保人登录
    # phone是手机号   password是密码   不知道加密的密码会不会每天变  会的话需要每天改
    # 除非能拿到加密方式的jar包
    login_url = "http://wxdat.shanghailife.com.cn/rest/user/login?"
    login_data = {"phone": phone, "password": password, "bindType": 10, "timestamp": "29724917"}
    login_res = requests.post(login_url, json=login_data)
    print("登录结果是：", login_res.json())

    # 核保接口
    # salary 好像是个人年收入  写大点可以提高上限  有两个地方
    url = "http://wxdat.shanghailife.com.cn/rest/policy/doInsure?"
    data = {"productCode": "1025004", "productName": "上海人寿大蘑菇定期寿险", "insuranceStartPeriod": "2020-08-21",
            "insuranceEndPeriod": "2040-08-20", "signedDate": "2020-08-20", "insuYearFlag": "Y", "insuYear": "20",
            "payIntv": 0, "payEndYear": 1000, "payEndYearFlag": "Y", "insuredAmount": 100000, "faceAmount": 100000,
            "premium": "738.00", "grossPremium": "738.00", "firstPremium": "738.00", "initialPremAmt": "738.00",
            "agentNo": "0101600007", "expireProcessMode": -2,
            "applicant": {"appName": "任乐", "appSex": 1, "appBirthday": "1990-07-17", "appIDType": "0",
                          "appIDNo": "410303199007179887", "appMobile": "13120529923", "appEmail": "15615@qq.com",
                          "province": "110000", "city": "110000", "country": "110101", "appHomeAddress": "北京市市辖区东城区代发费111",
                          "appAddress": "代发费111", "idexpDate": "2020-08-20", "occupationCode": "1010001",
                          "occupationClass": "1", "relationToInsured": "00", "stature": "180", "weight": "55",
                          "salary": "500000", "socialInsuFlag": "1"}, "goodsId": "43", "unitCount": "1", "channel": "",
            "insureds": [
                {"policyLiabilities":
                    [{"riskCode": "1025004", "riskName": "优选终身寿险", "riskAmount": 100000, "riskPremium": "738.00",
                         "insuYearFlag": "Y", "insuYear": "20", "payIntv": 0, "payEndYear": 1000, "payEndYearFlag": "Y",
                         "mainRiskFlag": "1", "insuranceStartPeriod": "2020-08-21", "insuranceEndPeriod": "2040-08-20",
                         "dutiesInfo": []}], "insuRelationToApp": "00", "insuName": "任乐", "insuSex": 1,
                    "insuBirthday": "1990-07-17", "insuIDType": "0", "insuIDNo": "410303199007179887",
                    "insuMobile": "13120529923", "insuEmail": "15615@qq.com", "insuProvince": "110000",
                    "insuCity": "110000", "insuAddress": "代发费111", "insuHomeAddress": "北京市市辖区东城区代发费111",
                    "insuCountry": "110101", "idexpDate": "2020-08-20", "occupationCode": "1010001",
                    "occupationClass": "1", "health": "2", "stature": "180", "weight": "55", "salary": "500000",
                    "socialInsuFlag": "1", "occupationName": "中国共产党中央委员会地方各级党组织负责人", "insuImpartInfo": [
                    {"impartVer": "E5044", "impartCode": "E10254-21", "impartparammodle": "否",
                     "impartQuestion": "被保险人是否患有或曾经患有下列症状或体征：<br/>最近2年内单次住院7天及以上或接受手术（剖腹产、门诊手术除外）；糖尿病；血压\r\n升高（未服药时收缩压≥160mmHg或舒张压≥100mmHg）；恶性肿瘤，血友病；心绞痛，\r\n心肌梗塞，主动脉血管瘤；呼吸衰竭，肺心病；克隆氏病，溃疡性结肠炎；肝硬化；肾功能不\r\n全，尿毒症；智障或痴呆，脑出血，脑梗塞，短暂性脑缺血发作，脑瘤，癫痫；再生障碍性贫\r\n血，白血病，系统性红斑狼疮及其他自身免疫类疾病；身体畸形或残疾；艾滋病患者或艾滋病\r\n毒携带者；精神疾病；酒精或药物滥用成瘾？"},
                    {"impartVer": "E5044", "impartCode": "E10254-22", "impartparammodle": "否",
                     "impartQuestion": "（女性适用）被保险人是否已怀孕28周及以上；"},
                    {"impartVer": "E5044", "impartCode": "E10254-23", "impartparammodle": "否",
                     "impartQuestion": "被保险人过去两年内投保人寿保险或申请复效时是否被保险公司拒保、延期承保？是否正\r\n在申请或曾申请过癌症或重大疾病保险理赔？在其他保险公司已申请及已生效的寿险与意外险\r\n保额累计是否大于等于300万（航意险除外）？最近三个月内是否在超过三家以上的保险公司\r\n投保寿险或意外险？"},
                    {"impartVer": "E5044", "impartCode": "E10254-24", "impartparammodle": "否",
                     "impartQuestion": "被保险人是否有危险嗜好或从事危险活动，如赛车，滑翔翼，滑翔机，飞行伞，跳伞，攀\r\n岩（室内攀岩除外），潜水（浮潜除外），滑水，跳水，马术比赛，拳击，武术或特技表演等\r\n运动？"}],
                    "smokeFlag": "N"}], "saleChannel": None, "beneficiaries": [], "renewalPaymentInfo": None,
            "lcTaxpayer": {"taxpayerType": 1, "firstname": "", "lastname": "", "taxBirthday": "", "birthProvince": "",
                           "birthCity": "", "birthAddressCN": "", "birthAddressEN": "", "currentAddress": "", "taxNo": "",
                           "reason": "", "remark": "", "lcTaxpayeroptionvalue": [], "num1": "", "num2": "", "num3": ""}
            }

    res = requests.post(url, json=data, cookies=login_res.cookies)
    print("核保结果是：", res.json())

    #支付订单
    #openId：加密后的支付密码（感觉）     orderNo：订单ID
    #同理 如果密码每天都变，那就只能每天抓一次当前的加密过的支付密码来改
    orderNo = res.json()["data"]["partnerOrderId"]
    url3 = "http://wxdat.shanghailife.com.cn/rest/pay/orderPay?"
    data3 = {"openId": openId, "orderNo": orderNo}
    res3 = requests.post(url3, json=data3, cookies=login_res.cookies)
    print("支付订单的结果是：", res3.json())

    # 承保的结果是
    url4 = f"http://wxdat.shanghailife.com.cn/rest/policy/queryPayStatus?orderNo={orderNo}"
    res4 = requests.get(url4, cookies=login_res.cookies)
    print("承保结果是：", res4.json())

if __name__ == '__main__':
    phone = 13120529922
    password = "tEk2d+LCpoE="
    openId = "oSrBLwSpNTxlLK3cPQnVaYgou5HE"
    test(phone,password,openId)
