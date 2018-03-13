#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# WSGI：Web Server Gateway Interface
#      只要求Web开发者实现一个函数，就可以响应HTTP请求。

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])  # 注意是()，不是{}
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Python Web')
    return [body.encode('utf-8')]
'''
    application()：符合WSGI标准的一个HTTP处理函数，
    第一个参数：一个包含所有HTTP请求信息的dict对象 ；第二个参数：一个发送HTTP响应的函数
    
    注意：Header只能发送一次，start_response只能调用一次。
    start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    
    函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。
'''

'''
application()函数必须由WSGI服务器调用
'''
