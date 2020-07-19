# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 21:37
# @Author  : 春衫
# @Email   : 1605936478@qq.com
# @File    : Commom_Data.py
# @Software: PyCharm

def url(surroundings):
    global H5_Login_url, H5_home_url

    if surroundings == "test":
        H5_Login_url = "http://m.test.hobay.com.cn//vuespa/index.html#/pwdLogin"
        H5_home_url = "http://m.test.hobay.com.cn/vuespa/index.html#/index"
    elif surroundings == "mtest":
        H5_Login_url = "http://m.mtest.hobay.com.cn//vuespa/index.html#/pwdLogin"
        H5_home_url = "http://m.mtest.hobay.com.cn/vuespa/index.html#/index"
    elif surroundings == "dev1":
        H5_Login_url = "http://m.dev1.hobay.com.cn//vuespa/index.html#/pwdLogin"
        H5_home_url = "http://m.dev1.hobay.com.cn/vuespa/index.html#/index"

    return H5_Login_url, H5_home_url
