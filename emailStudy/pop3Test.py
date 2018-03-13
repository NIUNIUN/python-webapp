#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
POP3协议：收取的是邮件的原始文本
SMTP: 发送的是经过编码后的一大段文本
要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

收取邮件分两步：
    1、使用poplib把邮件的原始文本下载到本地
    2、用emali解析原始文本，还原为邮件对象
'''

import poplib
from email.parser import Parser
from email.header import Header, decode_header
from email.utils import parseaddr

email = input('Email:')
pwd = input('Password:')
# POP3服务器地址
pop3_server = input('POP3 server:')

# 连接POP3服务
server = poplib.POP3(pop3_server)
# 打开或关闭调试信息
server.set_debuglevel(1)
# POP3服务器的欢迎文字
print('\n',server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(pwd)

#stat()返回邮件数量和占用空间
print('\nMessage: %s. Size: %s\n' % server.stat())

# list()所有的邮件的编号
resp,mails,octets = server.list()
print(mails,'\n\n')

# 获取最新一封邮件，索引从1开始
# retr() 获取邮件
index = len(mails)
resp,lines,octets = server.retr(index)

print('\nresp = %s\n lines= %s \noctets = %s\n' % (resp,lines,octets))

# lines存储了邮件的原始文本的每一行
# 获取整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')

# 解析邮件: 把邮件内容解析为Message对象
# Message对象：可能是MIMEMultipart、MIMEBase，嵌套
msg = Parser().parsestr(msg_content)

# 根据索引号直接删除邮件
# server.dele(index)
server.quit()

# 递归打印Message对象的层次结构
def print_info(msg,indent=0):
    if indent == 0:
        for headr in ['From','To','Subject']:
            value = msg.get(headr,'')
            if value:
                if headr == 'Subject':
                    value = decode_str(value)
                else:
                    hdr,addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name,addr)
            print('%s%s: %s' % (' ' * indent,headr,value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n,part in enumerate(parts):
            print('%spart %s' % (' '* indent,n))
            print('%s------------' % (' ' * indent))
            print_info(part,indent+1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode = True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sTest: %s' % (' '* indent,content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent,content_type))

# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
def decode_str(s):
    value,charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。
# 上面的代码只取了第一个元素。

# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type','').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset


# qq邮箱不成功，163邮箱成功
# qq邮箱pop3得使用SSL安全连接
# 所以使用POP3_SSL（）函数

print(msg)
print_info(msg)