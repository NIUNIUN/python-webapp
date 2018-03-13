#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
SMTP :发送邮件协议，可发送纯文本、HTML邮件以及带附件的邮件
  email：负责构造邮件、smtplib：负责发送邮件

'''
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# 构造对象
msg = MIMEText('hello, send by python...','plain','utf-8')
#  第一个参数：邮件正文 第二个参数：MIME的subtype，“plain”--纯文本，最终是‘text/plain’

# Email地址和密码
# from_addr = input('From:')
# password = input('Password:')

# 收件人地址
# to_addr = input('To:')
# SMTP服务器地址
# smtp_server = input('SMTP server:')

# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 发送邮件
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)   #打印出和SMTP服务器交互的所有信息

# 登陆SMTP服务器
# server.login(from_addr,password)

# server.sendmail(from_addr,[to_addr],msg.as_string())
# sendmail：可以一次发给多人，所以传入一个list
#  as_string ：把MIMEText对象变成str

# server.quit()

# 163提供的SMTP服务器地址：smtp.163.com
# qq提供的SMTP服务器地址：smtp.qq.com

# 以上方法不能成功发送邮件
# 这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
# 所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：

# ****************************  发送完整的邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib


def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
    # 包含中文，需要通过Header对象进行编码

from_addr = input('From:')
password = input('Password:')

# 收件人地址
to_addr = input('To:')
# SMTP服务器地址
smtp_server = input('SMTP server:')

msg = MIMEText('hello,send by python...','plain','utf-8')   # 纯文本
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')    # html

# *******  发送附件
msg = MIMEMultipart()
# 邮件正文是纯文本
msg.attach(MIMEText('send with file...','plain','utf-8'))

# 发送图片
#    :要把图片嵌入到邮件正文中。 按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

# 附件
with open('D:/blur.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','png',filename='test.png')
    # 必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    # 添加附件
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>','html','utf-8'))

# 同时支持HTML和Plain格式
#     :在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
#     利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
msg = MIMEMultipart('alternative')
msg.attach(MIMEText('hello python', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>hello python</h1></body></html>', 'html', 'utf-8'))


msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)    #邮件服务商在显示邮件时会把收件人名字自动替换为用户注册时的名字
msg['Subject'] = Header('来自SMTP的问候。。。','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

# 添加主题、发件人、收件人信息后，163发给qq能成功，但是qq发给163不成功
# 使用附件发送，垃圾信箱中
# Emial的原始内容，经过编码的邮件头
'''
经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本:

From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <15675478641@163.com>\r\n
To: =?utf-8?b?566h55CG5ZGY?= <1750772354@qq.com>\r\n
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeOAguOAguOAgg==?=\r\n
'''


# 加密SMTP
'''
标准的25端口连接时使用的是明文传输
加密SMTP会话：先创建SSL安全连接，然后再使用SMTP协议发送邮件
'''

# Gmail SMTP端口：587  必须要加密传输
smtp_server ='smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样。


'''
小结
使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，
构造一个MIMEText对象，就表示一个文本邮件对象，
构造一个MIMEImage对象，就表示一个作为附件的图片，
要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。
它们的继承关系如下：
        Message
        +- MIMEBase
            +- MIMEMultipart
            +- MIMENonMultipart
                +- MIMEMessage
                +- MIMEText
                +- MIMEImage

'''

'''
•554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；

•554 DT:SUM 信封发件人和信头发件人不匹配；

•554 IP is rejected, smtp auth error limit exceed 该IP验证失败次数过多，被临时禁止连接。请检查验证信息设置；

•554 HL:IHU 发信IP因发送垃圾邮件或存在异常的连接行为，被暂时挂起。请检测发信IP在历史上的发信情况和发信程序是否存在异常；

•554 HL:IPB 该IP不在网易允许的发送地址列表里；

•554 MI:STC 发件人当天内累计邮件数量超过限制，当天不再接受该发件人的投信。请降低发信频率；

•554 MI:SPB 此用户不在网易允许的发信用户列表里；

•554 IP in blacklist 该IP不在网易允许的发送地址列表里。

'''