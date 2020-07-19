#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/3/19 11:09
# @Author :春衫
# @File :work.py

import random


# 3.人和机器猜拳游戏写成一个类, 有如下几个函数:
# 1)函数1:选择角色 1曹操 2张飞 3刘备
# 2)函数2:角色猜拳 1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3)函数3:电脑出拳随机产生1个1-3的数字，提示电脑出拳结果
# 4)函数4:角色和机器出拳对战,对战结束后，最后出示本局对战结果。赢、输,然后提示用户是否继续? 按y继续,按n退出。
# 5)最后结束的时候输出结果 角色蠃几局 电脑赢几局,平局几次游戏结束。

class Game():
    role_dict = {"1": "曹操", "2": "张飞", "3": "刘备"}
    first_dict = {"1": "剪刀", "2": "石头", "3": "布"}

    def get_role_name(self):  # 获取角色
        role_num = input("请选择你的角色：1曹操 2张飞 3刘备")
        print("你选择的是{0}".format(self.role_dict[str(role_num)]))
        return self.role_dict[str(role_num)]

    def get_role_first(self):  # 角色出拳
        first_num = input("请输入一个数字：1剪刀 2石头 3布")
        print("你出{0}".format(first_num))
        return int(first_num)

    def get_computer_first(self):
        first_num = random.randint(1, 3)
        print("电脑出{0}".format(first_num))
        return first_num

    def play_games(self):
        role_win = 0
        cp_win = 0
        draw = 0
        role_name = self.get_role_name()  # 选择角色
        print("{0}请出拳".format(role_name))  # 获取角色名

        while True:
            role_first = self.get_role_first()
            computer_first = self.get_computer_first()  # 电脑出拳
            print(role_name + "出拳为{0}，电脑出拳为{1}".format(self.first_dict[str(role_first)],
                                                       self.first_dict[str(computer_first)]))

            if role_first - computer_first == -2 or role_first - computer_first == 1:
                role_win += 1
                print("角色赢了")

            elif role_first - computer_first == -1 or role_first - computer_first == 2:
                cp_win += 1
                print("电脑赢了")

            elif role_first - computer_first == 0:
                draw += 1
                print("平局")

            choose = input("您是否要继续?按y继续，按n退出")
            if choose == "n":
                print("游戏结束！")
                print("角色赢了{0}局，电脑蠃了{1}局，平局{2}".format(role_win, cp_win, draw))
                break
            print("角色赢了{0}局，电脑蠃了{1}局，平局{2}".format(role_win, cp_win, draw))


if __name__ == "__main__":
    Game().play_games()

# 角色赢角色数字-机器数字结果为: -2 1
# 电脑赢角色数字-机器数字 结果为: -1 2
# 平均角色数字-机器数字结果为: 0
