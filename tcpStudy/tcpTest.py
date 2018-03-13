#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    TCP连接 客户端：主动发起连接   服务器：被动响应连接
'''
import socket

# 创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.AF_INET--IPV4  AF_INET6--IPV6
# SOCK_STREAM：指定使用面向流的

# 创建连接（IP地址，端口号）
s.connect(('www.sina.com.cn',80))
'''
端口号 80--Web服务的标准端口  SMTP--25  FTP--21
<1024是Internet标准服务的端口   >1024，可以任意使用
'''

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 文本格式：符合HTPP标准


# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = buffer
# 关闭连接
s.close()
print(data)
print('d=',b''.join(data))

# 分离http头和网页
header , html =b''.join(data).split(b'\r\n\r\n')
print('\n',header.decode('utf-8'))
print('\n',html)

# 保存在本地
with open('D:\sina.html','wb') as f:
    f.write(html)


'''
 用TCP协议进行Socket编程在Python中十分简单
对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，
然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。

同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。

'''