#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/22 14:40
# @Author :春衫
# @File :learn_sql.py

import pymysql
from Requests.tools.project_path import db_config_path
from Requests.tools.read_config2 import ReadConfig


class DoMysql:

    def do_mysql(self,query_sql,state='all'):#query 查询语句

        # db_config = eval(ReadConfig().read_config(case_config_path,'DB','db_config'))
        db_config=ReadConfig().read_config(db_config_path)
        # 创建一个数据库连接  **关键字参数
        cnn = pymysql.connect(**db_config)
        # 游标cursor
        cursor = cnn.cursor()

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果 打印结果
        if state==1:
            res=cursor.fetchone()#type 元组
        else:
            res = cursor.fetchall()  # type 列表嵌套元组

        # 关闭游标
        cursor.close()

        # 关闭连接
        cnn.close()

        return res

if __name__ == '__main__':
    query_sql= 'SELECT mobile_phone FROM member ORDER BY id DESC LIMIT 1;'
    res=DoMysql().do_mysql(query_sql)
    print(res)