#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/21 11:08
#@Author :春衫
#@File :123.py

# -*- coding: utf-8 -*-
import requests
import json
from urllib import parse
# import quotes



def  GtgLogin(UserName,phone,CurrentAddress):
    print("开始请求")
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Referer': 'http://61.183.175.130/sunxf/gtghj/index.html',
         'X - Requested - With': 'XMLHttpRequest',
         'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    postUrl = 'http://61.183.175.130/sunxf/gtghj/do/write.php?action=save'
    data='{"FromName":"gtghj","UserName":"%s","UserSex":"1","UserPhoneNo":"%s","UserMailbox":"","CurrentAddress":"test城","LetterTitle":"test。","IsPublic1":"1"}'%(UserName,phone)

    post_data1= {'json':data}
    ###### 转换x-www-form-urlencoded
    Data =parse.urlencode(post_data1)
    r = requests.post(postUrl, data=Data, headers=header)
    print( r.text.encode("utf-8").decode("unicode_escape"))


if __name__ == "__main__":
    GtgLogin('刘先生','1111','武汉市高新技术开发区佛祖岭和昌光谷未来城C区')