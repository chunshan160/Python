#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/3/14 12:25
# @Author :春衫
# @File :Class2.py

import os

# 删除删除文件也是一级一级的删除不推荐大家一次删除
# 拓展-: Python 可否强制删除
# os.mkdir( "Alisa/rict ")
# os.rmdir("Alisa”)
# 0SError: [WinError 145]目录不是空的。:'Alisa'

# 拓展二:怎么去新建文件open删除文件?

# # 路径的获取1  获取当前工作目录   具体到最后一级目录
# path = os.getcwd()
# print("1获取到的当前路径是:{0}".format(path))
#
# # 路径获取2   获取当前文件所在的绝对路径   具体到模块名
# path_2 = os.path.realpath(__file__)
# print("2获取到的当前路径是:{0}".format(path_2))
#
# # 第三个知识点:如何拼接路径
# new_path_1 = os.getcwd() + "\python11"  # "\\python1"
# print(new_path_1)
# os.mkdir(new_path_1)

# join  更高级的拼接路径
# new_path_2 = os.path.join(os.getcwd(), "python777", "sub_1")
# print(new_path_2)
# os.mkdir(new_path_2)

a = os.listdir("D:\Pycharm_workspace\web_test")  # 获取当前路径下的目录列表,返回列表格式数据
print(a)

# 判断是文件还是目录
# print(os.path.isfile(os.getcwd()))  # 返回值布尔值
# print(os.path.isdir(os.getcwd()))  # 返回值布尔值 dir directory

# # 怎么去判断文件是否存在呢? 返回布尔值
# print(os.path.exists("E:\2018Python课件&代码\code\python_11\class_1013\class_03.py"))

# 罗列出当前路径的所有文件和目录
# print(os.listdir(os.getcwd()))


# #拓展题:
# #给定一个路径，请打印出所有的路径(直至这个路径下没有目录为止)
# #思路:递归函数写成一个函数
# #相当于打印所有路径出来
# for path in os.listdir(os.getcwd()):
#     if os.path.isdir(path):
#         os.listdir(os.path.join(os.getcwd(), path))  # 这步不影响结果
#         print("{0}还需要做进一步处理".format(path))
#     else:
#         print("这个是已经穷尽的路径", os.path.join(os.getcwd(), path))#打印文件所在的目录，然后加上文件名


# 异常处理
# 1、try...expect...
# 1:处理某个错误 #2:处理某种类型的错误 #3:有错就抓

# try:  # 警蔡
#     os.mkdir("Alisa")  # FileExistsError #嫌疑人
# # except FileExistsError:  # except 警力出动
# # except OSError:#FileExistsError(子)也属于OSError(父)中的一种
# # except Exception: # Exception  异常  只要异常都抓起来
# except:  # 有错就抓
#     print("抓捕归案，等待进一步处理")

# #既要抓 还要有处罚措施
# try:
#     os.rmdir("Alisa")#OSError
# except Exception as e:#把错误抓起来 存到变量e里面去 error
#     print("抓捕归案，等待进一步处理")
#     print("你犯的错是：{0}".format(e))
#     #拿一个小本本记下来
#     file=open("error.txt","a+",encoding="utf-8")
#     file.write(str(e))
#     file.close()#关闭文件
# finally:#不管上面怎么都执行
#     print("我就是这么厉害！！！啦啦啦")

# 2、try...expect...finally
# 2、try...expect...else##try报错else就不运行 反之运行  你好我也好
