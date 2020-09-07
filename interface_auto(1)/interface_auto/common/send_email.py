#!usr/bin/env python
#-*- coding:utf-8 -*-

import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from interface_auto.common.read_config import ReadConfig

class SendEmail:
    """封装发送邮件的方法"""
    @staticmethod
    def send_mail(file_path=None):
        """
        :param file_path: 附件的路径
        """
        smtp_server = ReadConfig().read_config('EMAIL','server')
        port = eval(ReadConfig().read_config('EMAIL','port'))
        sender = ReadConfig().read_config('EMAIL','sender')
        password = ReadConfig().read_config('EMAIL','password')
        receivers = ReadConfig().read_config('EMAIL','receivers')
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        #第一步：连接到服务器
        smtp = smtplib.SMTP(smtp_server,port,timeout=30)
        smtp.login(sender,password)

        #第二步：构建邮件
        message = MIMEMultipart()
        #文字内容
        text_message = MIMEText('接口自动化测试结果，请查收！')
        message.attach(text_message)
        #附件内容(一个附件)
        if file_path:
            file_message = MIMEApplication(open(file_path,'rb').read())
            file_message.add_header('content-disposition','attachment',filename=file_path)
            message.attach(file_message)
        else:
            pass
        #邮件主题
        message['Subject'] = now + '自动化测试报告'
        #发件人
        message['From'] = sender
        #收件人
        message['To'] = receivers

        #第三步：发送邮件并关闭连接
        smtp.sendmail(sender,receivers,message.as_string())
        smtp.close()

if __name__ == '__main__':
    from interface_auto.common.project_path import project_path
    file_path = os.path.join(project_path,'image.jpg')
    SendEmail.send_mail(file_path)