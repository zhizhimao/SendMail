#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Aug 10 11:21:36 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：send_mail.py

发送邮件两种发送方式：
send1: 定义  subject = '邮件标题'
             content = '邮件内容'
send2：已设置好，自动发送
"""

import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 构造邮件对象

msg_from = 'xxxxxx@sina.com'  # 从该邮箱发送，填写自己邮箱
from_pass = 'xxxxxx'  # 登录密码
msg_to = 'xxxxxx@sina.com'  # 发送到该邮箱
smtp_sever = 'smtp.sina.com'  # 新浪邮箱的smtp Sever地址
smtp_port = '25'  # 开放的端口


def send1(subject, content):
    # msg = MIMEText(content, 'html', 'utf-8')    # 构造MIMEText对象，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    msg = MIMEText(content)    # 构造MIMEText对象
    msg['Subject'] = subject  # 邮件标题
    msg['From'] = msg_from    # 发送者账号
    msg['To'] = msg_to    # 收件人账号
    try:
        smtp = smtplib.SMTP(smtp_sever)  # 新浪邮箱的smtp Sever地址
        smtp.login(msg_from, from_pass)   # 发送者的邮箱账号，密码
        smtp.sendmail(msg_from, msg_to, msg.as_string())  # 参数分别是发送者，接收者，邮件内容转换字符串形式
        smtp.quit()  # 发送完毕后退出smtp
        print('发送成功')
    except Exception as e:
        print("发送失败" + str(e))


def send2():
    import email.mime.multipart
    msg = email.mime.multipart.MIMEMultipart()  # 生成包括多个部分的邮件体
    msg['from'] = msg_from  # 从该邮箱发送
    msg['to'] = msg_to  # 发送到邮箱
    msg['subject'] = 'send2发送的Python3自动发送邮件'  # 标题
    content = '''
    你好:
        send2这是一封python3发送的邮件！
    '''  # 邮件内容
    txt = MIMEText(content)
    msg.attach(txt)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_sever, smtp_port)  # 连接邮件服务器，端口
        smtp.login(msg_from, from_pass)  # 登录发送邮件服务器，登录密码
        smtp.sendmail(msg_from, msg_to, msg.as_string())  # 参数分别是发送者，接收者，邮件内容转换字符串形式
        smtp.quit()  # 退出
        print('发送成功')
    except Exception as e:
        print("发送失败" + str(e))


subject = '测试'
content = '''
你好：
    测试邮件！
'''
send1(subject, content)  # 调用发送邮箱的函数
send2()
