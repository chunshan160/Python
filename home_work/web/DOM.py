#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/6/26 20:27
#@Author :春衫
#@File :DOM.py

# 查找元素

# 两个顶级节点:
# window:表示当前打开的浏览器窗口
# document:表示窗口中显示的当前

# Document对象是Window对象的一部
# window.document属性对其进行访问。

# 元素的id属性:
# document.getElementByld("")

# 元素的class属性:
# document.getElementsByClassName()

# 元素的标签名:
# document.getElementsByTagName()

# 元素的name属性:
# document.getElementsByName()

# css选择器:
# document.querySelector(css)


# 元素的属性
# 改变属性
# document.getElementByXXX("").属性名=属性值

# 获取属性2:
# document.getElementByXXX("").getAttribute(属性名)

# 改变元素的内容:，
# 包含html元素标签--有后代:
# document.getElementByXXX("").innerHTML=new HTML

# 不包含html标签，纯文字:
# document.getElementByXXX("").innerText=new text


# 样式
# 改变样式
# document.getElementByXXX("").style.样式名=样式值
# 例:
# 元素的可见性
# document.getElementByXXX("").style.visibility = 'hidden'
# 元素的颜色
# document.getElementByXXX("").style.color='red'


# 事件.
# 浏览器和用户事件-触发-执行js代码带来不同的页面响应。
# 例如:点击事件、输入事件、鼠标事件等。
# #页面加载完成事件
# window.onload = function(){
# alert("everything is ready!!")
# #点击事件
# document.findElementByld(XXX).onclick = function(){
# alert( "哈哈，点我了呀!”)}

