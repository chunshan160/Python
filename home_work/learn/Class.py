#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/1/17 11:07
# @Author :春衫
# @File :Class.py

# 标识符:我们自己在写代码的时候，取的名字。命名的符号。
# 项目名 project name
# 包名 package name
# 模块名  .py python文件名

# 规范:1:由字母数字下划线组成但是不能以数字开头
# 2:见名知意
# 3: 不同的字母数字之间用下划线隔开  提升你的可读性
# 4：不能用关键字 int、if、while

# 注释: #单行注释 ctr1+/
# 多行注释:成对的三个单/双引号
# 变量名=1 y=x+1求y的值
# print (你要输出的内容)   输出函数 输出内容到控制台
# Print  输出:
# print  默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号
# input  输入:
# input  从控制台里面获取一个数据，获取到的类型是字符串类型。

# 数据类型 条件语句 循环语句
# 数字:整型 浮点型
# 整型:关键字 int

# 浮点数   关键字 float
# b=10.0

# 布尔值bool boolean True False  首字母大写
# 字符串: str 成对的单引号、双引号、三引号的内容都是字符串

# type(数据)判断数据类型
# print (type(a))

# 字符串的一些使用
# s="hello!"
# 1:字符串里面元素: 单个字母、数字、汉字、单个符号都称之为一个元素
# len(数据)  统记数据的长度 print (len(s))
# 2:字符串取值:字符串名[索引值]
# 索引:从左往右 从0开始标记    从右往左 从-1开始标记


# # 字符串取多个值:切片  字符串名[索引头:索引尾:步长]  步长默认为1
# print(s[1:5:1]) #1234 取头不取尾
# print(s[:4])#0123
# print(s[3:])#3到尽
# #倒序
# print(s[-1:-7:-1])
# print(s[::-1])

# s="hello!"
# #字符串的分割 字符串.split(指定切割符号,切割次数)  返回一个列表类型的数据  列表里面的子元素都是字符串类型
# #指定的切割符被切走了。
# # print(s.split())
# print(s.split(" "))
# print(s.split("e"))
# print(s.split("l"))
# print(s.split("l",1))

#字符串的寻找  find
#s="hello!"
#print(s.find('el')  #返回索引位置 1
#找不到返回 -1



# #字符串的替换  字符串replace(指定替换值,新值,替换次数)
# s="hello!"
# # new = s.replace("o","@")
# new = s.replace("l","@",1)
# print(new)


# #字符串的去除指定字符  字符串.strip(指定字符)
# #1、默认去掉空格
# #2、只能去掉头和尾指定的字符
# s="hel!lo!"
# print(len(s))
# new = s.strip("!")
# print(len(new))


# #字符串的拼接  +  保证+左右两边的变量值类型要一致
# s_1 = "快放假啦"
# s_2 = "加油"
# s_3 = 666  #整数  str(数字)---可以强制转为str类型
# print(s_1+s_2,s_3)  #输出，不叫拼接
# print(s_1+s_2+str(s_3))
#
#
# #字符串格式化输出 % format
age=18
name="小恒星"
score = 99.9999999
# print("prton11期的"+name+",今年"+str(age)+"岁!")
#

# #格式化输出1: format 特点{}   用这个{}来占坑
# print("pyton11期的{},今年{}岁!".format(name,age))
# print("pyton11期的{1},今年{1}岁!".format(name,age))#从0开始  不填就默认顺序
#



#格式化输出2: %     %s字符串   %d数字   %f浮点数
print("pyton11期的%s,今年%d岁!"%(name,age))
print("pyton11期的%s,今年%s岁!"%(name,age))
# %s 可以填任何数据
# %d 只能填数字、整型、浮点数   只输出整数
# %f 可以填数字  会四舍五入   默认精确到小数点后六位   %.nf
print("pyton11期的%s,今年%s岁!考试考了%s"% (name, age, score))
print("pyton11期的%s,今年%s岁!考试考了%d"% (name, age, score))
#%f 可以填数字  会四舍五入   默认精确到小数点后六位   %.nf
print("pyton11期的%s,今年%s岁!考试考了%f"% (name, age, score))#考试考了100.000000
print("pyton11期的%s,今年%s岁!考试考了%.2f"% (name, age, score))#考试考了100.00


# 列表[]  元组()   字典{}


# # #列表list 符号[]
# a=[1,0.02,"hello",[1,2,3],True]
# # #1:可以存在空列表a=[]
# # #2:列表里面可以包含任何类型的数据
# # #3:列表里面的元素  根据逗号来进行分隔
# # #4:列表里面的元素也是有索引  索引值从0开始
# # #5:获取列表里面的单个值:  列表[索引值]
# print(a[2])
# #6: 列表的切片同字符串的操作  列表名[索引头:索引尾:步长]
# print(a[::2])
# #如果你要存储的数据是同一个类型的，建议用列表

# 增删改查
# 增 append insert
# 删 pop remove
# 改 a[2] = "初心"


# #如何往列表里面增加数据
# #append  追加 一次只能添加一个数据
# a = [1, 0.02, "hello", [1, 2, 3], True]
# a.append("秦天")
# print(a)
#
# # #insert  插入数据  想放哪里就放哪   但是要指定位置  从0开始
# a.insert(1,"测试")
# print(a)

# #删除 pop()
# a.pop()#默认删除最后一个元素  传入索引值 就删除指定索引位置的元素
# print(a)#[1, 0.02, 'hello', [1, 2, 3]]
# a.pop(0)
# print(a)#[0.02, 'hello', [1, 2, 3]]


# a.remove("hello")  # 指定删除某个值
# print("a列表的值{0}".format(a))
# res = a.pop(2)  # pop函数    会返回被删除的那个元素    函数return关键字。
# print("被删除的值是{0}".format(res))

# # #修改a [索引值]=新值
# a = [1, 0.02, "hello", [1, 2, 3], True]
# a[2] = "初心"  # 赋值运算
# print("a列表的值{0}".format(a))


# #元组tuple 符号()
# a=(1, 0.02,"hello",[1,2,3], True, (4, 5, 6))
# #1:可以存在空元组 a=()
# #2:元组里面可以包含任何类型的数据  print (type (a))
# #3:元组里面的元素 根据逗号来进行分隔
# #4:元组里面的元素 也是有索引 索引值从0开始
# #5: 获取元组里面的单个值: 元组[索引值]
# #6:元组的切片同字符串的操作    元组名[索引头:索引尾:步长]
# print (a[0:5:2])


# 操作数据看的时候会存放条件
# 元组 不支持任何修改(增删查)

# a = (1,0.02,"hello",[1,2,3],True,(4,5,6),"小小")
# a[3][-1]="华华"
# print(a)
#
# #如果你的元组里面只有一个元素   要加一个逗号
# a=([1,2])
# b=([1,2],)
# print (type(a))
# print (type(b))


# 字典dict 符号{}  大据号  花括号  无序
# 1: 可以存在空字典 a={}
# 2:字典里面数据存储的方式: key:value
# 2:字典里面的value可以包含任何类型的数据
# 3:列表里面的元素   根据逗号来进行分隔  print (len(a))
# a={"class":"python11",
# "student" :119,
# "teacher":"girl",
# "t_age":20,
# "score":[99, 88.8, 100.5]}
#
# # #字典取值：字典[key]
# print(a["score"])

# # #删除  pop(key)
# # # a.pop("teacher")
# # res = a.pop("teacher")
# # print(res)
#
# # #新增  a[新key]=value   字典里面不存在的key
# a["name"]="华华"
# print(a)
#
# #修改   a[已存在的key]=新value   字典里面已存在的key
# a["t_age"]=18
# print(a)


# #运算符5大类
# #算术运算符 + - * / %
# #模运算/取余运算  判断某个数是偶数还是奇数的
# a=4
# print(a%2)#为零就是偶数


# #赋值运算符 = += -=
# a=5#赋值运算
# a+=3#a+=3 等同于a=a+3 a-=3 等同于a=a-3
# print(a)

# 比较、逻辑、成员运算符返回都是布尔值

# #比较运算符>、>=、<、<=、!=（不等于）、==（恒等于）
# #6种比较关系
# #比较结果返回的值是布尔值True False
# # a=10
# # b=5
# # print (a>=b)

# print("get"=="GET")
# print("get".upper()=="GET")#大写
# print("get"=="GET".lower())#小写


# #逻辑运算符and or 拓展: not
# #逻辑运算结果返回的值是布尔值True False
# #and and的左右两边结果都为真才为真 只要有一个为假就为假
# #真真为真 and
#
# #or or的左右两边结果都为假才为假   只要有一个为真 就为真
# #假假为假 or
#
# a=10
# b=5
# print(a>11 or b>6)


# #成员运算符in not in
# #返回值也是布尔值True Falsei这两种情况
# # s="hello"
# # l=[1,2,3]
# # print(3 in l)
#
# d = {"age":18,"name":"捡鸭蛋"}
# print("18" in d)
# print("age" in d)#字典 是判断key


# #控制语句分支分流循环语句 for while
# #判断语句if.elif..else 关键字
# #1、if  1、条件语句(比较 逻辑 成员均可)   2、空数据==FaIse   非空数据==True
# age=20
# if age>18:#当if后面的语句满足条件运算结果是True 那就会执行他的子语句
#     print("恭喜你，你成年了!")


# #2: 一个条件语句里面只能有一个if和一个else else后面不能加条件
# #if 条件语句:
#     #子语句
# #eIse:
#     #子语句
# age=17
# if age>18:
#     print("恭喜你，你成年了!")
# else:
#     print("加油长大")

# #3、if后面 非空 非零 成立表达式 都为True
# #if 条件语句:
#     #子语句
# #elif 条件语句:
#     #子语句
# #eIse:
#     #子语句
# age=-20
# if age>=18:
#     print("恭喜你，你成年了! ")
# elif age<18:
#     print("加油长大，小屁孩! ")
# else:
#     print("你的年龄输入有误,不能为负数")

# #input()函数 从控制台获取一个数据  获取的数据都是字符串类型
# age=print(type(input("请输入你的年龄: ")))
# age=int(input("请输入你的年龄: "))
# if age>=18:
#      print("恭喜你，你成年了! ")
# elif 18>age>=0:
#      print("加油长大，小屁孩! ")
# else:
#      print("你的年龄输入有误,不能为负数")

# #判断是不是数字，再比较年龄
# age = input("请输入你的年龄: ")
# if age.isdigit():
#     if int(age)>=18:
#         print("恭喜你，你成年了! ")
#     elif 18>int(age)>=0:
#         print("加油长大，小屁孩! ")
# else:
#      print("你的年龄输入有误,请输入大于0的数字")


# #if语句是对不同情况的处理
# #3、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣。
# #如果购买金额大于100元会给20%折扣。
# #编写--程序，询问购买价格，再显示出折扣(%10或20%)和最终价格。
# total=input("请输入购买总金额：")
# if total.isdigit():
#     if int(total)<50:
#         print("不好意思，你没法享受折扣")
#         print("您需要支付{0}元".format(total))
#     elif 50<=int(total)<=100:
#         print("您将享受10%折扣")
#         print("您需要支付{0}元".format(int(total)*0.9))
#     else:
#         print("您将享受20%折扣")
#         print("您需要支付%.2f元"%(int(total)*0.8))
# else:
#      print("您输入有误,请输入大于0的数字")

# #4、生成随机整数,从1-9取出来。然后输入一个数字,来猜。如果大于，则打印bigger，小了则打印less，如果相等则打印equal。
# import random
# num_1=random.randint(1, 9) #两边都包含
# num_2=int(input("请输入你的数字: "))
# print("随机数是:{0}".format(num_1))
# if num_2>num_1:
#     print("bigger")
# elif num_2 < num_1:
#     print("less")
# else:
#     print("equal")


# 循环for while 关键字
# pyrthon for循环语法:
# for 变量名 in 某个数据类型: (数据类型包含:字符串 列表 元组 字典 集合等)
# 代码块
# in? 成员运算符in
# for 循环的循环次数 由数据的元素个数决定
# s="hello"
# l=[1,2,3]
# d={" age" :18, "name":"捡鸭蛋"}#字典类型的数据 是遍历访问的是key
# for a in d: #for循环遍历s.里面的元素然后赋值给item
#     print(d)
#     # print (d[a])

# L = [5, 6, 9, 3, 7]
# # 请你利用for循环完成列表里面的所有数据的相加
# sum = 0  # 存储我们的和
# for item in L:
#     sum = sum + item
# # print (item)
# # sum=L[O]+L[1]+L[2]+L[3]+L[4]
# print("所有值的和: {0}".format(sum))

# d = {" age": 18, "name": "捡鸭蛋"}
# print(d.values())  # 获取字典里面的所有value值
# print(d.keys())  # 获取字典里面的所有key值
# # for item in d:#遍历的是key  字典[key]
# #print(d[item])
# for item in d.values():
#     print(item)


# # 1、 一个足球队在寻找年龄在10岁到12岁的小女孩(包括10岁和12岁)加入。
# #编写一个程序，询问用户的性别(m表示男性，f表示女性)和年龄，
# #然后显示一条消息指出这个人是否可以加入球队，询问10次后,
# #输出满足条件的总人数。
#
# sum=0#总人数初始值
# for item in [1,2,3,4,5,6,7,8,9,10]:
#     age=int(input("请问你多大了？"))
#     sex=input("请问你的性别？")
#     if 10<=age<=12 and sex=="f":
#         print("恭喜你，符合加入我们足球队的条件")
#         sum=sum+1#符合条件就加1  赋值运算
#     else:
#         print("很遗憾，你不满足我们的条件")
# print("符合条件的人数是：{0}".format(sum))


# #range函数   生成整数序列
# #range函数range(m,n,k)  m头,n尾,k步长，取头不取尾
# range(1,5,1)#1 2 3 4
# range(1,6,2)#1 3 5
#
#
# print(list(range(1,5,1)))
# print(list(range(1,6,2)))
# print(list(range(1,3)))
# print(list(range(8)))#只有一个值的话   头默认为0  从0开始
# for item in range(3):#0 1 2
#     print("循环次数")


# L=[5,6,9,3,7]
# #请利用for循环  根据L的索引值，打印出每个元素的值
# for i in range(5):#0 1 2 3 4
#     print(L[i])


# sum=0
# for i in range(1,101):
# 	sum=sum+i
# print("所有值的和:{0}".format(sum))
#
# #嵌套循环#请把列表里面的每一个元素 单独打印出来
# L=[["monica","生生","小黄","冷夜"],["helen","不想睡","心动"]]
#
# for item in L:#每循环一次拿到一个子列表赋值给item
# 	for a in item:
# 		print("学生的名字是:",a)


# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# # * * * * * *
# for i in range(6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# # 一个班级有一个花名册，存在列表里面。
# # 你从控制台输入一个名字，如果这个名字在花名册里面，
# # 就打印这个用户名正确 如果不存在 那就报错
# #i j k n m  用来表示数字类型的变量
#
# name = ["huahua", "ta", "tingting", "kaka"]
# username = input("请输入你的名字:")
# if username in name:  # 成员运算符
#     print("用户名正确!")
# else:
#     print("用户名不正确!")

# while 控制循环
# 语法：
# while 条件表达式：#逻辑 成员 比较 空数据 布尔值  参照if语句
# 代码块

# 执行规律：首先判断while后面的表达式是否成立
# 如果为True  那就执行代码块  执行完毕之后，继续判断，继续执行  直到为False结束
# 否则  不进入代码块
# 防止代码进入死循环：加一个变量来控制循环次数
# 空数据为False
# while True  一直循环，进入死循环，除非有break
# a=1#初始值
# while a<=10:
#     print("现在是输入的第{0}次".format(a))
#     print("打工是不可能的，这辈子都不可能打工的！")
#     a=a+1

# #利用while循环实现1-100的整数相加
# sum=0#初始值
# a=1#循环的起始值
# while a<=100:
#     sum=sum+a
#     a=a+1
# print("求和的结果是:",sum)

# # while与if语句搭配使用break continue
# # 1.一个足球队在寻找年龄在10岁到12岁的小女孩(包括10岁和12岁)加入。
# # 编写一个程序，询问用户的性别(m表示男性，f表示女性)和年龄，
# # 然后显示一条消息指出这个人是否可以加入球队，询问10次后，
# # 输出满足条件的总人数。
# i = 10  # 记录询问次数
# count = 0  # 记录符合条件的人数
# while i > 0:
#     sex = input("请输入你的性别：")
#     if sex == "f":
#         i -= 1  # 询问次数减1
#         age = int(input("请输入你的年龄:"))
#         if 10 <= age <= 12:
#             print("恭喜你可以加入足球队")
#             count += 1
#         else:
#             print("很遗憾不满足加入条件")
#     else:
#         print("很遗憾不满足加入条件")
#         i -= 1
#     # if i==0:
#     #     break#结束循环，跳出循环
#     # else:
#     #     continue#结束本轮循环，继续下一轮

# 2、输入num为四位数，对其按照如下的规则进行加密:
# 1)每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2)将该数的第1位和第4为互换，第二位和第三位互换
# 3)最后合起来作为加密后的整数输出

# num = input("请输入4位数字:")
#
# d = []
# for i in str(num):
#     d.append(str((int(i) + 5) % 10))
# d.reverse()
# print(d)
# c = int(''.join(d))#用‘’把列表里的分隔符替换掉
# print(c)


# # 例如: passwd={"admin":"123321","user1":"123456"}
# # 1、设计一个登陆程序，不同的用户名和对应密码存在一个字典里面，输入正确的用户和密码去登录。
# # 2、首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名。
# # 3、当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入。
# # 4、如果密码输入错误超过三次，中断程序运行。
# # 5、当输入密码错误时，提示还有几次机会。
# # 6、用户名和密码都输入成功的时候，提示登录成功!

#
# menber = {"admin": "123321", "user1": "123456"}
#
# while True:
#     sum = 3
#     username = input("请输入用户名:")
#     if username in menber.keys():
#         while sum >= 0:
#             if sum > 0:
#                 pwd = input("请输入密码：")
#                 if pwd == menber[username]:
#                     print("登陆成功")
#                     break
#                 elif sum > 0:
#                     sum -= 1
#                     print("密码错误，请重新输入！你还有{}次机会!".format(sum))
#             else:
#                 print("错误次数超过三次，停止运行")
#                 break
#         break
#     elif username not in menber.keys() or username == "":
#         print("请输入正确的用户名")

# Python内置函数
# 试错
# print input len type str int float list range
# pop append insert keys split replace strip
# remove clear
# 总结一下函数的特点:
# 可以重复使用
# 函数的语法:def关键字
# 函数名命名的规范: 小写字母  不能以数字开头 不同的字母之间用下划线隔开
# def函数名(参数1，参数2，参数3):
# 函数体:你希望这个函数去给你实现什么功能?

# 调用：函数名（）

# # def da_lao(name):#形参/位置参数
# #     print("{0}是大佬".format(name))
# def da_lao(name="都"):#默认参数
#     print("{0}是大佬".format(name))
#
# # 调用函数
# da_lao("冬冬")
# da_lao("水仙哥")
# da_lao()

# # #动态参数/不定长参数 *args arguments  贪婪
# #有*号就显示在一块，没*号显示列表
# def make_sandwich (*args) :
#     all=""
#     for item in args:
#         all+=item
#         all+="、"
#     print("您的三明治包含了"+all)
#
# make_sandwich("生菜","鸡蛋""培根","牛肉","吐司")

# def add_all_num(*L,a):
#     print(L) #元组
#     sum=0
#     for item in L:
#         sum+=item
#     print("和为",sum)
#     print("a的值",a)
#
# add_all_num(1,2,3,4,5,6,a=7)


# 关键字参数 key-value **kwargs key word 必须加**
# 在函数里面体现为字典
# def kw_function(**kwargs) :
# print (kwargs)
#
# kw_function(x=1, y=2)

# def add_all_num(a=7, *L, **kwargs):
#     print(L)  # 元组
#     sum = 0
#     for item in L:
#         sum += item
#     print("和为", sum)
#     print("a的值", a)
#     print("kwargs", kwargs)
#
#
# add_all_num(1, 2, 3, 4, 5, 6, x=1, y=2)

# #利用range函数请求出任意整数相加功能  写成一个函数
# def add_numbers(m,n,k=1):
#     sum=0
#     for i in range(m,n,k):
#         sum=sum+i
#     print("求和的值是:{0}".format(sum))
#
# add_numbers(1,5)
# #第一步:先用代码实现功能  还可以选取一组数据来证明自己的diamante是否正确
# #第二步:变成函数 加def
# #第三步:想办法提高代码的复用性


# def add_num(m, k, n):  # 形参位置参数
#     sum = 0
#     for i in range(m, n, k):  # 1 10 2 #1 3 5 7 9
#         sum += i
#     print("最后的结果值: {0}".format(sum))
#
#
# # 按顺序赋值
# add_num(1, 2, 10)  # 实际参数
# # 指定了参数的
# add_num(m=1, k=10, n=2)  # 实际参数
#


# 怎么用
# 1:自己写的怎么导入 #一层一层的剥开
# import class_ 1009. function_ 1
# class_ 1009. function_ 1. add_ num(1, 101)
#
# 2: Prthon自带的或者是后面安装的第三方库怎么引用-->简单点
# 1) import   2) from ... import
# import email. mime. python_ math
# 一层一层的剥开
# email. mime. python_ math. add(I, 11)
# from email. mime import python_ math#推荐大家使用


# if __name__ == "__main__":  # 主程序的执行入口  只有当你在当前模块下面执行的时候才会执行
#     pass

# from class_1009.function_1 import * #模块名  导入所有def


# #file txt xml html --->
# #mode打开这个文件的模式
# read write append
# #r（只读） w（只写） a（追加）
# #r+  w+  a+

# # #rb rb+  wb wb+  ab ab+  做单元测试的时候
# file = open(" python11. txt","r+",encoding="utf-8")
# res=file.read()#读5个字符
# file.write("我爱贼妈")
# print (res)

# 1: file文件open之后 默认是r 只读模式 如果你要写入内容报错: io. UnsupportedOperation:
# 2: r+ 可读可写 先写的话从头开始覆盖 写读光标之后的内容 读写跟着光标走
# 3:如果要写入中文要注意编码格式
# 4: w只写  硬要去读就会报错 io.UinsupportedOperation: not readable
# 5:w+ 可读可写 不管是w还是w+ 如果文件存在就直接清空 再重写
# 如果文件不存在则新建一个文件 然后写
# 6: a追加
# 如果文件存在 就直接追加写在后面  如果不存在 则新建一个文件写


# #重点掌握两种r a
# file=open(" python13. txt"," r" , encoding="utf-8")
# # print(file. read()) 读取所有内容
# # print (file. readline())按行读取
# # print (file. readline())
# print (file. readlines())#读取多行返回的是列表
# # file_ 2=open( "python13. txt,""a "， encoding="utf-8")
# # print(file_ 2. write(”20181011 file操作"))


# #3: 写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和。
# # j_ sum=0
# # o_sum=0
# # for i in range(0, 101) :
# #     if i%2==0:
# #         j_sum+=i
# #     else:
# #         o_sum+=i
# # print("偶数和", o_sum)
# # print("奇数和", j_sum)
#
# j_sum=0
# o_sum=0
# for i in range(0, 101,2):
#     o_sum+=i
# for i in range(1, 101,2):
#     j_sum+=i
# print("偶数和", o_sum)
# print("奇数和", j_sum)
