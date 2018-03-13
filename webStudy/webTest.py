#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Web框架
'''
如何处理HTTP请求不是问题，问题是如何处理100个不同的URL:
def application(environ,start_respone):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ,start_respone)
    if method == 'POST' and path =='/signin':
        return handle_signin(environ,start_respone)
    ...
'''

'''
本例：处理3个URL，分别是：
•GET /：首页，返回Home；
•GET /signin：登录页，显示登录表单；
•POST /signin：处理登录表单，显示登录结果。
'''

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def home():
    return '<h1>Python Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''
    <form actio="/signin" method='post' >
    <p><input name="username"></p>
    <p><input name="pwd"></p>
    <p><button type="submit" >Sign In</button></p>
    </form>
    '''
@app.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['pwd'] == 'password':
        return '<h2>Hello，admin！</h2>'
    else:
        return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()


'''
小结
有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。

'''