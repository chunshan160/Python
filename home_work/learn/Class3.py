#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/3/14 16:15
# @Author :春衫
# @File :Class3.py

# #直角三角形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end='')#end=''  不换行输出
#     print("")


# # #等腰三角形
# for i in range(1,6):
#     for j in range(1,6-i):
#         print("@",end='')
#     for k in range(1,i+1):
#         print("* ",end='')
#     print("")

# #输出99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}*{1}={2} ".format(j,i,i*j),end='')
#     print("")

# 5、经典冒泡算法: 利用for循环，完成a=[1, 7, 4, 89, 34, 2]的冒泡排序。
# 冒泡排序:小的排前面，大的排后面。
# 排序，最终使得数组中的这几个数字按照从小到大的顺序排序。
# 冒泡的概念，关系到你接下来怎么写程序
# 相邻的两个元素 依次比较
# a = [1, 7, 4, 89, 34, 2]  # 冒泡算法 一般最多比较n-1趟就完成
# 1 4 7 34 2 89第一趟
# 1 4 7 2 34 89第二趟
# 1 4 2 7 34 89第三趟
# 1 2 4 7 34 89第四趟
# #冒泡排序
# for i in range(1, len(a)):
#     for j in range(0, len(a) - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)


# # 2:自动贩卖机: 只接受1元、5元、10元的纸币或硬币,最多不超过10块钱.
# # 饮料只有橙汁、椰汁、矿泉水、早餐奶.
# # 售价分别是3.5, 4, 2, 4.5写一个函数用来表示贩卖机的功能:
# # 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
# drinks = {"橙汁": 3.5, "椰汁": 4, "矿泉水": 2, "早餐奶": 4.5}
# total = 0
# while True:
#     choose = str(input("请选择你要的饮料："))
#     if choose in drinks.keys():
#         total += drinks[choose]
#         toubi = 0
#         while True:
#             money = input("请投币：")
#             if money == '1' or money == '5' or money == '10':
#                 toubi += int(money)
#                 if toubi > total:
#                     print("你刚刚购买了{0}元饮料，您已支付{1}元，找零{2}！".format(total, toubi, toubi - total))
#                     break
#                 elif toubi < total:
#                     print("你刚刚购买了{0}元饮料，您已支付{1}元，还需支付{2}！".format(total, toubi, total - toubi))
#                 else:
#                     print("你刚刚购买了{0}元饮料，您已支付{1}元，已支付完毕！".format(total, toubi))
#                     break
#             elif money == "取消":
#                 print("退出投币")
#                 break
#             else:
#                 print("你输入的选项不存在！")
#     elif choose == "取消":
#         print("退出选择饮料")
#         break
#     else:
#         print("这里没有您想要的{0}".format(choose))
#         break


#
# #类
# class Teacher():
#     name="巧明"
#     age=88
#
#     def cooking(self):  # 实例方法
#         print(self.name+"不会做蛋炒饭")
#
#     @classmethod
#     def swimming(cls,username):  # 类方法
#         print(username+"不会敲代码")
#
#     @staticmethod
#     def sing():  # 静态方法  普通函数
#         print("不会唱歌")


# #类里面方法是分为三种
#
# # # 实例方法:意味着这个方法只能实例来调用
# #实例一
# t = Teacher()  # 创建实例 隐式的传递
# t.cooking()
# #实例二
# Teacher().cooking()
# #实例三
# Teacher.cooking(t)#显示的传递 不建议使用      t.cooking()=Teacher.cooking(t)
#错误实例
# Teacher.cooking() # missing I required positional argument:' self'

#
# # 类方法: @classmethod
# t = Teacher()
# t.swimming("冬冬")
#
# Teacher().swimming("冬冬")
#
# Teacher.swimming("冬冬")
# # Teacher.swimming(t)#错误  TypeError: unsupported operand type(s) for +: 'Teacher' and 'str'
#
# # 静态方法: @staticmethod
# t = Teacher()
# t.sing()
#
# Teacher().sing()
#
# Teacher.sing()
# Teacher.sing(t)#错误  sing() takes 0 positional arguments but 1 was given



# 实例方法self 类方法cls  静态方法(普通方法) 实例和类名都可以直接调用
# 2: 不同点:静态方法和类方法 不可以调用类里面的属性值 如果你要参数请自己传递参数




# Python类中的self到底是干啥的
# Python编写类的时候，每个函数参数第一个参数都是self，一开始我不管它到底是干嘛的，只知道必须要写上。后来对Python渐渐熟悉了一点，再回头看self的概念，似乎有点弄明白了。
#
# 首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
#
# self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗（为了和其他编程语言统一，减少理解难度），不要搞另类，大家会不明白的。
#
# 下例中将self改为myname一样没有错误：

# class Person():
#     def __init__(myname,name):
#         myname.name=name
#     def sayhello(myname):
#         print ('My name is:',myname.name)
# p1=Person("华华")
# p1.sayhello()
# print (p1)
# # self指的是类实例对象本身(注意：不是类本身)。
#
# class Person():
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print ('My name is:',self.name)
# p2=Person('Bill')
# print (p2)
# # # 在上述例子中，self指向Person的实例p2。 为什么不是指向类本身呢，如下例子：
# #
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print ('My name is:',self.name)
# p3=Person('Bill')
# p4 = Person('Apple')
# print (p3)
# # 如果self指向类本身，那么当有多个实例对象时，self指向哪一个呢？
# #
# # 总结
# #
# # self在定义时需要定义，但是在调用时会自动传入。
# #
# # self的名字并不是规定死的，但是最好还是按照约定是用self
# #
# # self总是指调用时的类的实例









# 初始化函数: def __init__ (self,参数1， 参数2，参数3)
# __init__ 函数,是两个下划线!经常会写错,写成__int__(self) ,这样会报错!
# 用法:
# def __init__ (self,a,b)
#     self.a=a
#     self.b=b
#     self.c= 10
# 注意:
# 1 )初始化里面做的是初始化操作,可以带参数也可以不带参数。
# 2 )跟普通函数-样,可以带默认参数。
# 3 )初始化函数里面可以有赋值好了的属性值。
# 4 )每次创造一 个实例,需要传递跟初始化函数参数个数一致的值。
# 5)每个实例都自动调用初始化函数,需要传递对应的参数。
# 6)初始化参数的写法要注意，怎么把参数赋值给self.参数名。 参数名字不一定要一致，但是赋值要正确。
# 7)初始化函数无返回值。

# class Teacher():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def cooking(self):  # 实例方法
#         print(self.name + "不会做蛋炒饭")
#
#     def coding(self):  # 实例方法
#         print(self.name + "不会敲代码")
#
#     @classmethod
#     def swimming(cls):  # 类方法
#         print("不会游泳")
#
#     @staticmethod
#     def sing():  # 静态方法  普通函数
#         print("不会唱歌")


# # 初始化函数
# t1 = Teacher("华华", "18")
# t2 = Teacher("毛毛", "20")
# t3 = Teacher("小简", "19")
# t4 = Teacher("星星", "16")
# t1.swimming()
# t2.cooking()
# t3.coding()
# t4.sing()


# 什么时候用初始化函数？
# 想用就用
# 如果某个属性值是多个函数共用的 就可以用初始化函数

class Teacher():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play_game(self, game_name):
        return (self.name + "会玩{0}".format(game_name))

    def coding(self, lines, language="python"):  # 实例方法
        print(self.name + "会敲{0}代码,写了{1}行代码".format(language, lines))

    def cooking(self, *args):  # 实例方法
        for item in args:
            print(self.name + "会做{0}".format(item))

#
t1 = Teacher("巧明", "18")
# t1.coding(1000)
# t1.cooking("蛋炒饭", "小炒肉", "方便面")
print(t1.play_game("王者荣耀"))


# class Teacher():
#
#     def __init__(self, name, age=23):#实例方法，一般不传动态参数和关键字参数
#
#         self.name = name
#         self.age = age
#         self.height=180
#
#     def teacher_info(self):
#         print(" {0}老师，今年{1}岁，身高{2},可以嫁人了! ".format(self.name, self.age,self.height))
#
#     def cooking(self, *args):  # 实例方法
#         for item in args:
#             print(self.name + "会做{0}".format(item))
#
#     def teacher_1(self, *args):
#         self.cooking(*args)  # 每个传参都运行一次  小白会做海鲜汤   小白会做老火靓汤
#
#     def teacher_2(self, *args):
#         self.cooking(args)#已元组形式输出   小白会做('海鲜汤', '老火靓汤')
#
# t2=Teacher("小白")
# t2.teacher_1("海鲜汤","老火靓汤")
# t2.teacher_2("海鲜汤","老火靓汤")


# # 继承
#
# class RobotOne:  # 第一代机器人
#     def __init__(self, year, name):
#         self.year = year
#         self.name = name
#
#     def walking_on_ground(self):  #
#         print(self.name + "只能在平地上行走，有障碍物就会摔倒")
#
#     def robot_info(self):
#         print("{0}年产生的机器人{1},是中国研发的".format(self.year, self.name))


#
#
# # 继承
# class RobotTwo(RobotOne):  ##第二代机器人继承于第一代机器人的类
#
#     def walking_on_ground(self):  # 子类里面的函数名 与父类函数名重复的时候，就叫 重写
#         print(self.name + "可以在平地上行走")
#
#     def walking_avoid_block(self):  # 类的拓展   父类里没有的
#         # 我想在父类的函数里面 调用父类的一个函数
#         self.robot_info()
#         print(self.name + "可以避开障碍物")


# # 第二代机器人
# # 继承的类 是否要用到初始化函数 请看是否从父类里面继承
# # 1:爸爸有的 我都有 可以直接拿过来用
# # 2: 爸爸有 我也有 那就用自己的
# r2 = RobotTwo("1990", "小王")
# r2.robot_info()
# r2.walking_on_ground()
# r2.walking_avoid_block()


# 多继承和超继承
# C:多继承: python支持多继承，同时可以继承多个类。(了解即可)
# 经典类的搜索方式是按照“从左至右，深度优先”的方式去查找属性。

# D:超继承:如果你的重写了父类里面的一个方法，然后又想调用父类里面的一些方法，可以用超继承，我们在单元测试里面会看到这个操作。
# 不用去重写复制代码，轻轻松松可以做到更多继承。(了解会用即可) -super(子类名，self) ,根据子类找到父类。
#
# class D(A):
#     def run(self):
#         print("我的下面是超继承")
#         super(D, self).run()
#         print("我的上面是超继承!!!")
#         t2 = D()
#         t2.run()


# 知识点 多继承  继承多个父类
# 第三代机器人

# # 第一代机器人
# class RobotOne:  # 第一代机器人
#     def __init__(self, year, name):
#         self.year = year
#         self.name = name
#
#     def walking_on_ground(self):  #
#         print(self.name + "只能在平地上行走，有障碍物就会摔倒")
#
#     def robot_info(self):
#         print("{0}年产生的机器人{1},是中国研发的".format(self.year, self.name))
#
#
# # 为了多继承写的一个第二代机器人
# class RobotTwo():  # 第二代机器人
#
#     def __init__(self, name):
#         self.name = name
#
#     def walking_on_ground(self):  # 子类里面的函数名 与父类函数名重复的时候，就叫 重写
#         print(self.name + "可以在平地上行走")
#
#     def walking_avoid_block(self):  # 类的拓展   父类里没有的
#         print(self.name + "可以避开障碍物")
#
#
# # 第三代机器人
# class RobotThree(RobotOne, RobotTwo):  # 第三代机器人 继承于 第一代和第二代机器人 的类
# # class RobotThree(RobotTwo, RobotOne):
#     def jump(self):
#         print(self.name + "可以单膝跳跃")
#
#
# r3 = RobotThree("1990", "大王")
# # r3 = RobotThree("大王")
# r3.jump()
# r3.walking_on_ground()
# # 具有两个父类的属性和方法  如果两个父类具有同名方法的时候  就近原则
#
# # 疑问  没有传递year参数 调用robot_year就会报错怎么办?  暂时没办法解决
# r3.robot_info()
#
# #多继承的子类具有两个父类的属性和方法  如果两个父类具有同名方法的时候
# #子类调用函数就近原则 初始化函数也包括在内
