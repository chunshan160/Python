#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/7 11:08
# @Author :春衫
# @File :123.py

import requests

login_url = 'http://wxdat.shanghailife.com.cn/rest/user/login?'
login_data = {"phone": "13120529330", "password": "hsvctnCbZqE=", "bindType": "11", "timestamp": "66346783",
              "unionID": "oiGdIwE1MJSIOEWmk6pefhy3T9sA", "openID": "oSrBLwSpNTxlLK3cPQnVaYgou5HE"}
login_res = requests.post(login_url, json=login_data)
print("登录结果：", login_res.json())


accessKey=login_res.json()['data']['accessKey']
print(accessKey)
client_url = 'http://wxdat.shanghailife.com.cn/rest/policy/list?'
client_data = {}
headers = {"X-Requested-With": accessKey}
client_res = requests.post(client_url, json=client_data, headers=headers,cookies=login_res.cookies)
print("点击基本信息结果：", client_res.json())