#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 客户端

import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in [b'Michael',b'Tracy',b'Sarch']:
    # 发送数据
    s.sendto(data,('127.0.0.1',8890))
    # 接收数据
    da = s.recv(1024)
    print('client recv %s from Server' % da.decode('utf-8'))

s.close()