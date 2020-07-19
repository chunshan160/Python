# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # @Time :2020/3/16 10:05
# # @Author :春衫
# # @File :lianxi.py
#
# # #直角三角形
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print("*",end="")
# #     print("")
#
#
# # #等腰三角形
# # for i in range (1,6):
# #     for j in range(1,6-i):
# #         print(" ",end="")
# #     for a in range(1,i+1):
# #         print("* ",end="")
# #     print("")
#
# # #九九乘法表
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("{0}*{1}={2} ".format(i,j,i*j),end="")
# #     print("")
#
# # # 2:自动贩卖机: 只接受1元、5元、10元的纸币或硬币,最多不超过10块钱.
# # # 饮料只有橙汁、椰汁、矿泉水、早餐奶.
# # # 售价分别是3.5, 4, 2, 4.5写一个函数用来表示贩卖机的功能:
# # # 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
drinks = {"橙汁": 3.5, "椰汁": 4, "矿泉水": 2, "早餐奶": 4.5}
total = 0
while True:
    choose = input("请选择你要购买的饮料：")
    if choose in drinks.keys():
        total += drinks[choose]
    elif choose == "取消":
        print("退出选择饮料")
        break
    else:
        print("这里没有您想要的{0}".format(choose))
        break

toubi = 0
while True:
    money = input("请投币：")
    if money == '1' or money == '5' or money == '10':
        toubi += int(money)
        if toubi > total:
            print("你刚刚购买了{0}元饮料，您已支付{1}元，找零{2}！".format(total, toubi, toubi - total))
            break
        elif toubi < total:
            print("你刚刚购买了{0}元饮料，您已支付{1}元，还需支付{2}！".format(total, toubi, total - toubi))
        else:
            print("你刚刚购买了{0}元饮料，您已支付{1}元，已支付完毕！".format(total, toubi))
            break
    elif money == "取消":
        print("退出投币")
        break
    else:
        print("你输入的选项不存在！")
#
#
# role_dict = {"1": "曹操", "2": "张飞", "3": "刘备"}
# print(role_dict[str(1)])
#
# import random
#
#
# role_dict = {"1": "曹操", "2": "张飞", "3": "刘备"}
# first_dict = {"1": "剪刀", "2": "石头", "3": "布"}
#
# def get_role_name(self):  # 获取角色
#     role_num = input("请选择你的角色：1曹操 2张飞 3刘备")
#     print(role_dict[str(role_num)])
#
# def get_role_first(self):  # 角色出拳
#     first_num = input("请输入一个数字：1剪刀 2石头 3布")
#     print(int(first_num))
#
# def get_computer_first(self):
#     first_num = random.randint(1, 3)
#     print("电脑出{0}".format(first_num))
#     print(first_num)
#
# def play_games(self):
#     role_win = 0
#     cp_win = 0
#     draw = 0
#     role_name = get_role_name()
#     print("{0}请出拳".format(role_name))  # 获取角色名
#
# first_num = input("请输入一个数字：1剪刀 2石头 3布")
# print(int(first_num))
# role_name = get_role_name()
# role_first = get_role_first()  # 角色出拳
# computer_first = get_computer_first()  # 电脑出拳
# print(role_dict[str(1)], first_dict[str(2)])
#
#
# class Game():
#     role_dict = {"1": "曹操", "2": "张飞", "3": "刘备"}
#     first_dict = {"1": "剪刀", "2": "石头", "3": "布"}
#
#     def get_role_name(self):  # 获取角色
#         role_num = input("请选择你的角色：1曹操 2张飞 3刘备")
#         # if role_num=="1" or role_num=="2" or role_num=="3":
#         return self.role_dict[str(role_num)]
#         # else:
#         #     print("请输入正确的数字")
#
#     def get_role_first(self):  # 角色出拳
#         first_num = input("请输入一个数字：1剪刀 2石头 3布")
#         # if first_num=="1" or first_num=="2" or first_num=="3":
#         print("你出{0}".format(first_num))
#         return int(first_num)
#         # else:
#         #     print("请输入正确的数字")
#
#     def get_computer_first(self):
#         first_num = random.randint(1, 3)
#         print("电脑出{0}".format(first_num))
#         return first_num
#
#     def play_games(self):
#         role_win = 0
#         cp_win = 0
#         draw = 0
#         role_name = self.get_role_name()  # 选择角色
#         print("{0}请出拳".format(role_name))  # 获取角色名
#
#         while True:
#             role_first = self.get_role_first()#用户出拳
#             computer_first = self.get_computer_first()  # 电脑出拳
#             print(role_name + "出拳为{0}，电脑出拳为{1}".format(self.first_dict[str(role_first)],
#                                                        self.first_dict[str(computer_first)]))
#
#             if role_first - computer_first == -2 or role_first - computer_first == 1:
#                 role_win += 1
#                 print("角色赢了")
#
#             elif role_first - computer_first == -1 or role_first - computer_first == 2:
#                 cp_win += 1
#                 print("电脑赢了")
#
#             elif role_first - computer_first == 0:
#                 draw += 1
#                 print("平局")
#
#             choose = input("您是否要继续?按y继续，按n退出")
#             if choose == "n":
#                 print("游戏结束！")
#                 print("角色赢了{0}局，电脑蠃了{1}局，平局{2}".format(role_win, cp_win, draw))
#                 break
#             print("角色赢了{0}局，电脑蠃了{1}局，平局{2}".format(role_win, cp_win, draw))
#
#
# if __name__ == "__main__":
#     Game().play_games()
#
#
#
# # a = int(input('a = '))
# # b = int(input('b = '))
# # print('%d + %d = %d' % (a, b, a + b))
# # print('%d - %d = %d' % (a, b, a - b))
# # print('%d * %d = %d' % (a, b, a * b))
# # print('%d / %d = %f' % (a, b, a / b))
# # print('%d // %d = %d' % (a, b, a // b))
# # print('%d %% %d = %d' % (a, b, a % b))
# # print('%d ** %d = %d' % (a, b, a ** b))


# print("Hello,{0},成绩提升了{1:.1f}%".format('小明', 17.125))
#
#



