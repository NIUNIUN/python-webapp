#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 服务端
import socket,threading,time

# 创建Stock
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定 IP地址，端口号
s.bind(('127.0.0.1',9980))

# 监听。参数：等待连接的最大数量
s.listen(5)
print('Wating for connetion...')

def tcpLink(sock,addr):
    print('\nAccept new connection from %s : < %s >...' % (sock,addr))
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('\nConnection from %s:%s closed.' % addr)

# 接受客户端的连接
while True:
    sock,addr = s.accept()
    # 创建线程处理TCP连接
    thread = threading.Thread(target=tcpLink,args=(sock,addr))
    thread.start()

