#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/7 15:43
# @Author :春衫
# @File :class_06day_with.py

# with open("test.txt", "w+", encoding="utf8") as f:
#     f.write("摸鱼摸鱼")

# with 后面跟的是一个上下文管理器对象

"""
上下文管理器的概念:上下文管理器是一个Python对象, 为操作提供了额外的上下文信息。这种额外的信息，在
使用with语句初始化上下文，以及完成with块中的所有代码时,采用可调用的形式。

●object.__enter__(self)
输入与此对象相关的运行时上下文。如果存在的话，with 语句将绑定该方法的返回值到该语句的as子句中指定的目标。

●object.__exit__(self, exc_type, exc_val, exc_tb)

exc_.type : #异常类型
exc_val : #异常值
exc_tb : #异常回溯追踪

退出与此对象相关的运行时上下文。参数描述导致上下文退出的异常。
如果该上下文退出时没有异常，三个参数都将为None。
如果提供了一个异常,并且该方法希望抑制该异常(即防止它被传播)，它应该返回一个真值。
否则，在退出此方法后,异常将被正常处理。
注意__exit__().方法不应该重新抛出传递进去的异常，这是调用者的责任。
"""


class MyOpen(object):
    # 文件操作的上下文管理器

    def __init__(self, file_name, open_method, encoding="utf8"):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    # 异常类型、异常信息、异常追溯
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)  # <class 'NameError'>
        print(exc_val)  # name 'name' is not defined
        print(exc_tb)  # <traceback object at 0x000002363E159F40>
        self.f.close()


with MyOpen("test.txt", "r") as f:
    content = f.read()
    # print(name)
    print(content)

# with MyOpen("test1.txt", "w") as f:
#     print(f)
