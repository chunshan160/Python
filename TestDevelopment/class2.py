#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/8 16:49
# @Author :春衫
# @File :class2.py

import itertools

def race(qiwang, tianji):
    tianji_l = list(itertools.permutations(tianji, len(tianji))) # 用迭代获取田忌所有派遣马匹的方式(['13579',5])
    result = [] # 全部赛果
    for i in tianji_l:  # 遍历所有的赛马方式
        result_1 = [] # 一轮的比赛结果
        for horses in zip(i, qiwang): # 一轮比拼中，双方马匹对阵情况,i为tianji(i是从tianji_l获取的)
            if horses[0] < horses[1]:   #如果田忌的马值比齐王的小
                result_1.append('lose')   #那这一轮就是田忌输
            else:
                result_1.append('win')  #反之，这一轮就是田忌赢
        if result_1.count('win') >= 3:  #如果这一轮赢三次及以上
            result.append('win')  #田忌就赢了，将赢了的追加到result里面
    return len(result)

if __name__ == '__main__':
    tian = [1, 3, 5, 7, 9]
    qi = [2, 4, 6, 8, 10]
    all_result = race(qi, tian)
    print(all_result)
