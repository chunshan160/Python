#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/27 17:05
# @Author :春衫
# @File :BaseCase.py

import re
from Requests.data.GlobalEnvironment import GlobalEnvironment as gl


class BaseCase:

    def paramsReplace(self, caseInfoList):
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        for caseInfo in caseInfoList:
            # 如果数据是为空的，没有必要去进行参数化的处理
            if caseInfo['requestHeader'] != None:
                requestHeader = self.regexReplace(caseInfo['requestHeader'])
                caseInfo['requestHeader'] = requestHeader


            if caseInfo['url'] != None:
                url = self.regexReplace(caseInfo['url'])
                caseInfo['url'] = url

            if caseInfo['inputParams'] != None:
                inputParams = self.regexReplace(caseInfo['inputParams'])
                caseInfo['inputParams'] = inputParams

            if caseInfo['expected'] != None:
                expected = self.regexReplace(caseInfo['expected'])
                caseInfo['expected'] = expected

        return caseInfoList

    def regexReplace(self, sourceStr):
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        while re.search('{{(.*?)}}', str(sourceStr)):
            key = re.search('{{(.*?)}}', str(sourceStr)).group(0)
            value = re.search('{{(.*?)}}', str(sourceStr)).group(1)
            new_value = gl().get_value(value)
            data = str(sourceStr).replace(key, new_value)
            sourceStr = data

        return sourceStr


if __name__ == '__main__':
    s = [{'caseId': 1, 'interface': 'login', 'title': '正常登录',
          'requestHeader': {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'},
          'method': 'POST', 'url': '/member/login',
          'inputParams': {'mobile_phone': '{{mobile_phone}}', 'pwd': '{{pwd}}'},
          'expected': {'code': 0, 'msg': 'OK', 'data.mobile_phone': '{{mobile_phone}}'}, 'sheet_name': 'login'}]
    res = BaseCase().paramsReplace(s)
    print(res)
