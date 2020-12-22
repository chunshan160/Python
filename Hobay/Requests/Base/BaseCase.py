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
                requestHeader = self.regexReplace(caseInfo)
                caseInfo['requestHeader'] = requestHeader

            if caseInfo['Url'] != None:
                url = self.regexReplace(caseInfo)
                caseInfo['requestHeader'] = url

            if caseInfo['inputParams'] != None:
                inputParams = self.regexReplace(caseInfo)
                caseInfo['expected'] = inputParams

            if caseInfo['expected'] != None:
                expected = self.regexReplace(caseInfo)
                caseInfo['expected'] = expected

        return caseInfoList

    def regexReplace(self, sourceStr):
        # 对四块做参数化处理（请求头、接口地址、参数输入、期望返回结果）
        while re.search('{{(.*?)}}', sourceStr):
            key = re.search('{{(.*?)}}', sourceStr).group(0)
            print(key)
            value = re.search('{{(.*?)}}', sourceStr).group(1)
            print(value)
            new_value = gl().get_value(value)
            print("保存的新值：", value)
            data = sourceStr.replace(key, new_value)

        return data


if __name__ == '__main__':
    s = '{"mobile_phone": "{{mobile_phone}}","pwd": "{{pwd}}"}'
    res = BaseCase().regexReplace(s)
    print(res)
