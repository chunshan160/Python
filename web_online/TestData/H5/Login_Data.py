# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 22:49
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : login_datas.py.py
# @Software: PyCharm

# 正常用例 -手机格式正确
Success_data = {"username": "13724765586", "password": "syfms160"}

# 异常用例 -手机号格式不对
PhoneError_data = [
    {"username": "137247655", "check": "手机号格式错误"},
    {"username": "", "check": "请填写手机号"}
]

# 异常用例 -密码不正确
PasswordError_data = [{"username": "13724765586", "password": "qaz", "check": "用户名或密码错误"}]

# 注册
Registered_data = {"username": "75684964234", "code": "666666", "invite_people": "13724765586"}

#找回密码
RetrievePassword_data = [{"username":"13724765586", "code":"191115", "password":"qaz123","check": "手机号格式错误"}]
