#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/4/10 12:33
# @Author :春衫
# @File :test_sql.py

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.101',
                     port=3306,
                     user='root',
                     passwd='iloveyou2016,./',
                     db='ecloud_orders')

# 使用cursor()方法创建一个游标对象cur （可以理解为激活数据库）
cursor = db.cursor()

# 使用execute()执行SQL语句
cursor.execute(
    'SELECT b.id,b.user_id,b.type,b.biz_type,b.changes,b.result,b.current,b.source_id,b.note,b.category from orders a, wallet_detail b where a.order_num="EC-2020042315073900009535" and a.id=b.source_id;')

# 使用fetchall()方法获取查询结果 (接收全部的返回结果)
data = cursor.fetchall()
print(data[0])
print(data[0][4])
# # SQL 更新语句
# sql = "update member set UserName='chunshan' where UserName='chunshan160';"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 使用execute()执行SQL语句
# cursor.execute("select * from member")
#
# # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
# data = cursor.fetchall()
# print(data)

# 解决游标遍历慢的方法：一行一行去遍历，而不是一下全部读取出来
db.close()
