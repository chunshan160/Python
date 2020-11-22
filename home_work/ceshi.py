#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/9/24 17:07
# @Author :春衫
# @File :ceshi.py

def different(str1, str2):
    str11 = str1.split(' ')
    str22 = str2.split(' ')
    list1 = []
    list2 = []
    dic1 = {"周杰伦": "周董", "王力宏": "力宏", "李荣浩": "李荣浩", "李健": "李健", "蔡依林": "蔡妍",
            "房东的猫": "猫", "薛之谦": "谦谦",
            "孙燕姿": "孙燕姿", "韩红": "韩红", "郁可唯": "郁可唯"}
    for i in str11:
        if i not in str22:
            if dic1[i] not in str22:
                list1.append(i)
            else:
                list2.append(i)

    print('str1 中所有 str2 中不存在的人名:{}'.format(list1))
    print('str1 中所有 str2 中存在的人名:{}'.format(list2))#这个是1有2也有的数据
    print('-------------------------------------------------------------')
    for j in list2:
        #只要我把1有2也有的数据从2里面删除，剩下来的就是2有1没有的
        if dic1[j] in str22:
            str22.remove(dic1[j])
    print('str2 中所有 str1 中不存在的人名:{}'.format(str22))


str1 = '周杰伦 王力宏 李荣浩 李健 蔡依林 房东的猫 薛之谦 孙燕姿 韩红 郁可唯'
str2 = '李荣浩 谦谦 韩红 蔡妍 猫 力宏 周董 张惠妹 苏打绿 黄龄'
different(str1, str2)
