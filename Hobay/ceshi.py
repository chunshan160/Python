#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/16 15:16
# @Author :春衫
# @File :ceshi.py

# !/bin/user/python
# coding: UTF-8

# from jira import JIRA

import xlwt

import os

path = os.getcwd()


# 输入jira账号和密码

def input_user():
    # 主流程开始

    username = input('请输入用户名: ')

    password = input('输入密码: ')

    if username == '' or password == '':
        print('用户名和密码不能为空')

    return username, password


# 获取jira缺陷数据

def jira_data_repair():
    # options = {
    #
    #     'verify': False,
    #
    #     'server': 'http://10.10.67.25/jira/browse/KITAS-362?jql=project%20%3D%20KITAS%20ORDER%20BY%20created%20DESC'}
    #
    # jira = JIRA(options=options, basic_auth=('os_wangjuan', '123456'))
    #
    # issues = jira.search_issues('project = KITAS ORDER BY created DESC')
    issues="lala"
    # 写excel

    workbook = xlwt.Workbook(encoding='utf-8')

    worksheet = workbook.add_sheet('test')

    total = 0

    # 获取缺陷信息

    for u in issues:
        # print u #打印缺陷的key值

        # 写入内容

        worksheet.write(total, 0, str(u))

        total = total + 1

        # 保存excel

    workbook.save('1123.xls')
jira_data_repair()