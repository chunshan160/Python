#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/7/25 12:30
# @Author :春衫
# @File :upload.py

import win32gui
import win32con


def upload_file(filepath):
    # 一级窗口
    dialog = win32gui.FindWindow("#32770", "打开")
    # 二级窗口
    comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    # 三级窗口
    combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
    # 四级窗口 文本输入框
    edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
    # 打开按钮 二级窗口
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开")

    # 输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
    # 点击打开按钮 上传文件
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

upload_file("E:\图片.jpg")
