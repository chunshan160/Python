#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/25 12:52
#@Author :春衫
#@File :ceshi.py

#coding=utf-8

"""
add_front():从队列头部加入一个元素
add_rear():从队列尾部加入一个元素
remove_front():从队列头部删除一个元素
remove_rear():从队列尾部删除一个元素
is_empty(): 判空操作
size():返回队列的大小
"""

class Double_ended_queue():
    def __init__(self):
        # 空的列表，保存队列数据
        self.list = []

    def add_front(self, item):
        # 从队列头部加入一个元素
        self.list.insert(0,item)

    def remove_front(self):
        # 从队列头部删除一个元素
        return self.list.pop(0)

    def add_rear(self, item):
        # 从队列尾部添加一个元素
        self.list.append(item)

    def remove_rear(self):
        # 从队列尾部删除一个元素
        return self.list.pop()

    def is_empty(self):
        # 判空操作
        return self.list == []

    def size(self):
        # 返回队列的大小
        return len(self.list)

    # 数据测试


if __name__ == "__main__":
    a =Double_ended_queue()
    a.add_front(1)
    a.add_front(2)
    a.add_rear(3)

    print(a.remove_front())
    print(a.remove_front())
    print(a.remove_rear())
