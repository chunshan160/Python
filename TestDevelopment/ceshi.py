#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/4 11:44
# @Author :春衫
# @File :ceshi.py

import itertools

tianji = [1, 3, 5, 7, 9]
qiwang = [2, 4, 6, 8, 10]

result_list = []
result_list2 = []
count_num = 0

for item in itertools.product(tianji, qiwang):
    if item[0] > item[1]:
        result_list.append(item)
print(result_list)

new_list = list(itertools.product(result_list, repeat=3))  # 有重复的排列
# new_list = list(itertools.permutations(result_list, 3)) #无重复的排列
# new_list = list(itertools.combinations(result_list, 3))  # 无重复的组合
# new_list = list(itertools.combinations_with_replacement(result_list, 3)) #有重复的组合

# print(new_list)
print(len(new_list))

for data in new_list[::-1]:
    if data[0][0] == data[1][0] or data[0][0] == data[2][0] or data[1][0] == data[2][0]:
        # print("第一个",data)
        new_list.remove(data)

    elif data[0][1] == data[1][1] or data[0][1] == data[2][1] or data[1][1] == data[2][1]:
        # print("第二个",data)
        new_list.remove(data)

print(new_list)
print(len(new_list))

# for data2 in new_list[::-1]:
#     i, j, k = data2
#     if (i, j, k) in new_list and (i, k, j) in new_list and (j, i, k) in new_list and (j, k, i) in new_list and (
#     k, i, j) in new_list and (k, j, i) in new_list:
#        new_list.remove(data2)
#
# print(new_list)
# print(len(new_list))