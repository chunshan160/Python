#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/3/21 16:50
# @Author :春衫
# @File :jiekou.py

import requests

# 接口的分类
# ●外部内部广泛的分类
# ●按照不同的请求协议http webservice dubbo socket
# 学习的思路-方法很重要。
# ●接口的本质: 登录接口注册的接口  获取某个省份天气预报的接口
# #类:函数/方法->就是测试类里面的方法
# #Apache tomcat 中间件容器服务-->URL地址
# #参数(数据)逻辑
# http协议的接口
# http请求分为哪几种:get post delete update head option


# 1:剖析http request
# 一个http request (http请求) 指从客户端到服务端的请求消息，包括了以下信息:
# ●请求地址uri
# ●请求方法: HEAD、GET、POST、PUT、OPTIONS、QELETE、PATCH
# ●HTTP协议/版本:大家可以自己打开浏览器按F12去仔细查看
# 请求网址: https://csdnimg. cn/search/baidu_ search-1.1.2.jsPvu 2018020710568autorunstrue&it
# 请求方法: GET
# 远程地址: 124.232. 170.85:443
# 状态码: 200⑦编乐和重发 原始头
# 版本: HTTP/2.0
# ●请求头: https://jingyan.baidu. com/article/375c8e19770f0e25f2a22900.html
# ●请求正文:也就是我们说的请求参数



# 2:剖析http response
# ●状态码: 标记响应状态的-一个标识，200-成功，404- 资源找不到，500服务器异
# 常，302-重定向等，自行去拓展。-->常见的HTTP状态码有哪些?
# ●响应头:
# ●响应正文: 针对请求从服务响应回来的数据，比如html、xml、json等
# 常见http返回状态码:
# 200(正常):表示--切正常,到了服务器,并且服务器正常的响应了你的请求。
# 302 (临时重定向) : 指出被请求的文档已被临时移动到别处,此文档的新的URL在
# Location响应头中给出。
# 304 (未修改) :表示客户机缓存的版本是最新的,客户机应该继续使用它,比如说
# 前端js
# 403(禁止) : 服务器理解客户端请求,但拒绝处理它。通常由于服务器上文件或目
# 录的权限设置所致。
# 404 (找不到)服务器上不存在客户机所请求的资源。
# 500 (内部服务器错误) :服务器端的CGI、ASP、 JSP等程序发生错误。
# 504:超时。


# 3:剖析cookie session
# ●cookie: 在客户端存储用户的一些数据比如说用户名啥的浏览记录啥的
# ●session: 在服务器端，记录用户的请求状态，一般默认时间是30min。


# 会员卡机制。
# session_ id会存在cookie中，每次请求cookie中的所有信息都会传送给服务器，服务
# 器通过session_ jid来 识别是否是同-一个用户的请求。不是同一个用户的话，就会要求
# 用户重新登录。
# 为什么会有这种机制?因为http请求是无状态的。
# 参考博文: https://www.cnblogs. com/nickjiang/p/9148136.html


# 4:剖析访问授权
# ●
# 鉴权:访问的接口是否正常，是否是非法访问，绕过前端访问。token
# ●
# 授权:是否具有访问接口的权限。key
# - -般来说:是唯一的，全局的，动态的，具备一定特征
# 具体可以参考这个:
# htts://blog.csdn.net/sjy8207380/article/details/79232644
# 如果遇到接口不会处理怎么办?
# http://docs. python-requests.org/zh_ CN/latest/



login_url = 'http://8.129.65.165:8080/futureloan/mvc/api/member/login'
login_data = {"mobilephone": "13724765586", "pwd": "123456"}

recharge_url = "http://8.129.65.165:8080/futureloan/mvc/api/member/recharge"
recharge_data = {"mobilephone": "13724765586", "amount": "1000"}


#session 会话
s=requests.session()#创建了一个会话
login_res=s.get(login_url,params=login_data)#记住用params  保持会话所以不用cookies
recharge_res=s.post(recharge_url,recharge_data)
print("充值结果是：", recharge_res.json())