#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/10/30 15:57
# @Author :春衫
# @File :suiji.py


import random

gold = 1000000
diamond = 2000
value = 100
consume_gold = 1000
start = 1
success_rate = 101
successes_number = 0
failures_number = 0
max_start=[]
while True:
    if (gold > consume_gold) and (diamond - 270 > 0):
        a = random.randint(1, 101)
        if a in range(1,success_rate):
            print("成功")
            consume_gold += 1000
            start += 1
            success_rate -= 5
            successes_number += 1
            max_start.append(start)
        else:
            print("失败")
            failures_number += 1
            if start > 10:
                start = 10
                success_rate=56
                consume_gold = 10000
            value -= 7
            if value - 7 < 0:
                print("装备耐久不足，消耗270钻石")
                diamond -= 270
                value=80
        gold -= consume_gold
        print(f"剩余金币：{gold},剩余钻石：{diamond}")
        print(f"装备剩余耐久：{value}")
        print(f"现在锻造等级是：+{start},成功率：{success_rate}")
    else:
        print("你的金币/钻石不足")
        break
print(f"成功次数：{successes_number},失败次数：{failures_number}")
print(f"最大值是：+{max(max_start)}")