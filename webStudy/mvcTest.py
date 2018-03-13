#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MVC模型：Model-View-Controller，中文名“模型-视图-控制器”。
'''
Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

例子中，Model就是一个dict：
{ 'name': 'Michael' }
只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。
'''

# 把 webTest例子改写成MVC模式

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('signin-form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username =  request.form['username']
    pwd = request.form['password']
    if username == 'admin' and pwd == 'password':
        return render_template('signin-ok.html',userName = username)
    else:
        return render_template('signin-form.html',message='Bad username or password',userNAME = username)

if __name__ == '__main__':
    app.run()


# ******
#    目录名必须为templates。  最后，一定要把模板放到正确的templates目录下，templates和app.py在同级目录下：


# Flask通过render_template()函数来实现模板的渲染。
# 和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2