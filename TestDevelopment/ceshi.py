#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 11:44
# @Author :春衫
# @File :ceshi.py

def lower_to_capital(dict_info):
    new_dict = {}
    # for i, j in dict_info.items():
    #     new_dict[i.upper()] = j

    for i, j in list(dict_info.items()):
        dict_info.pop(i)
        dict_info[i.upper()] = j
    
    return dict_info


if __name__ == '__main__':
    before_dict = {'abc': 'python', 'def': 'java', 'ghi': 'c#', 'jkl': 'go'}
    print(lower_to_capital(before_dict))