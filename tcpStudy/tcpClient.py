#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 客户端
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9980))
print('Client revc:',s.recv(1024).decode('utf-8'))

s.send('python-1'.encode('utf-8'))
# print('Client revc:',s.recv(1024).decode('utf-8'))
s.send('python-2'.encode('utf-8'))
print('Client revc:',s.recv(1024).decode('utf-8'))

# 为啥发送一条数据，接收一条数据和发送多条数据再接收数据，打印出来的不一样
#

s.send('exit'.encode('utf-8'))  # 以便服务端关闭连接
s.close()

