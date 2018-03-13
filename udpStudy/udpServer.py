#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# SOCK_DGRAM--UDP  SOCK_STREAM--TCP

# 绑定IP、端口号
server.bind(('127.0.0.1',8890))


# 无需listen()，直接接收来自任何客户端的数据

print('Bind UDP on 8890...')
while True:
    # udp,addr = server.accept()  UDP没有创建连接，不用accept()

    # 直接接收数据
    data,addr = server.recvfrom(1024)
    print('Received from %s:%s' % addr)

    # 回复客户端
    server.sendto(b'hello, %s!' % data,addr)

#