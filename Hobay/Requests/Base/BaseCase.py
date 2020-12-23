#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/27 17:05
# @Author :春衫
# @File :BaseCase.py

import re
from Requests.data.GlobalEnvironment import GlobalEnvironment as gl
from Requests.tools.do_sql import DoMysql


class BaseCase:

    def paramsReplace(self, caseInfoList):
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        for caseInfo in caseInfoList:
            # 如果数据是为空的，没有必要去进行参数化的处理
            if caseInfo['requestHeader'] != None:
                requestHeader = self.regexReplace(caseInfo['requestHeader'])
                caseInfo['requestHeader'] = eval(requestHeader)

            if caseInfo['url'] != None:
                url = self.regexReplace(caseInfo['url'])
                caseInfo['url'] = url

            if caseInfo['inputParams'] != None:
                inputParams = self.regexReplace(caseInfo['inputParams'])
                caseInfo['inputParams'] = eval(inputParams)

            if caseInfo['expected'] != None:
                expected = self.regexReplace(caseInfo['expected'])
                caseInfo['expected'] = eval(expected)

        return caseInfoList

    def regexReplace(self, sourceStr):

        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        while re.search('{{(.*?)}}', str(sourceStr)):
            key = re.search('{{(.*?)}}', str(sourceStr)).group(0)
            value = re.search('{{(.*?)}}', str(sourceStr)).group(1)
            new_value = str(gl().get_value(value))
            sourceStr = str(sourceStr).replace(key, new_value)

        return sourceStr

    def get_phone(self):
        sql = 'SELECT mobile_phone FROM member ORDER BY id DESC LIMIT 1;'
        res = DoMysql().do_mysql(sql)
        mobile_phone = eval(res[0][0])
        gl().set_value("mobile_phone", str(mobile_phone + 1))
        gl().set_value("mobile_phone1", str(mobile_phone + 2))
        gl().set_value("mobile_phone2", str(mobile_phone + 3))


if __name__ == '__main__':
    s = [{'caseId': 1, 'interface': 'register', 'title': '正常注册-管理员，昵称10位',
          'requestHeader': '{"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}',
          'method': 'POST', 'url': '/member/register',
          'inputParams': '{\n  "mobile_phone": "{{mobile_phone}}",\n  "pwd": "lemon123456",\n  "type":"0",\n  "reg_name":"管理员用户lemon"\n}',
          'expected': '{\n  "code": 0,\n  "msg": "OK",\n  "data.mobile_phone": "{{mobile_phone}}"\n}',
          'sheet_name': 'register'},
         {'caseId': 2, 'interface': 'register', 'title': '正常注册-普通用户，type为空，密码8位',
          'requestHeader': '{"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}',
          'method': 'POST', 'url': '/member/register',
          'inputParams': '{\n  "mobile_phone": "{{mobile_phone+1}}",\n  "pwd": "lemon666",\n  "type":"",\n  "reg_name":"tudou"\n}',
          'expected': '{\n  "code": 0,\n  "msg": "OK",\n  "data.mobile_phone": "{{mobile_phone}}"\n}',
          'sheet_name': 'register'},
         {'caseId': 3, 'interface': 'register', 'title': '正常注册-普通用户，昵称为空，密码16位',
          'requestHeader': '{"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}',
          'method': 'POST', 'url': '/member/register',
          'inputParams': '{\n  "mobile_phone": "{{mobile_phone+1}}",\n  "pwd": "lemon12345678901",\n  "type":"1",\n  "reg_name":""\n}',
          'expected': '{\n  "code": 0,\n  "msg": "OK",\n  "data.mobile_phone": "{{mobile_phone}}"\n}',
          'sheet_name': 'register'}]
    gl()._init()
    res = BaseCase().paramsReplace(s)
    print(res)
