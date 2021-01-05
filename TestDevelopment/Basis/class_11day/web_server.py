#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2020/12/25 15:19
# @Author :春衫
# @File :web_server.py

import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    return "hello python"

if __name__ == '__main__':
    app.run(debug=True)