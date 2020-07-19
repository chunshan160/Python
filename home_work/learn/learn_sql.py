#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/22 14:40
# @Author :春衫
# @File :learn_sql.py

import mysql.connector

db_config = {'host': '8.129.65.165',
             'user': 'root',
             'password': '123456',
             'port': 3306,
             'database': 'future',
             'charset': 'utf8'}

# 创建一个数据库连接  **关键字参数
cnn = mysql.connector.connect(**db_config)

# 游标cursor
cursor = cnn.cursor()

# 写SQL语句
query_sql = 'select * from member where MobilePhone="13724765586"'

# 执行语句
cursor.execute(query_sql)

# 获取结果 打印结果
# res=cursor.fetchone()#type 元组
res = cursor.fetchall()  # type 列表嵌套元组

# 关闭游标
cursor.close()

# 关闭连接
cnn.close()
