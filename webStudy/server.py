#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python内置了一个WSGI服务器，这个模块叫wsgiref,它是用纯Python编写的WSGI服务器的参考实现。

所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
'''

# 从wsgi模块导入
from wsgiref.simple_server import make_server
from study.webStudy.wsgiTest import application

# def application(environ,start_response):
#     body = 'Hello Python!'
#     start_response('200 OK',[('Content-Type','text/html')])
#     # 从environ里读取PATH_INFO
#     body = '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
#
#     return [body.encode('utf-8')]

# 创建一个服务器，IP为空，端口是8890，处理函数为application
httpd = make_server('',8890,application)
print('Server HTTP on port 8890...')
# 监听HTTP请求
httpd.serve_forever()


'''
小结
无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。

'''