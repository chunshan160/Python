#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/5/22 14:40
# @Author :春衫
# @File :learn_sql.py

import mysql.connector
from tools import project_path
from tools.read_config import ReadConfig


class DoMysql:

    def do_mysql(self,query_sql,state='all'):#query 查询语句

        db_config = eval(ReadConfig().read_config(project_path.case_config_path,'DB','db_config'))

        # 创建一个数据库连接  **关键字参数
        cnn = mysql.connector.connect(**db_config)

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
    query_sql= 'select max(MobilePhone) from member where MobilePhone="13724765586";'
    res=DoMysql().do_mysql(query_sql)
    print(res)