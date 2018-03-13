#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
图形界面第三方库：Tk、wxWidgets、Qt、GTK等

Python自带的库支持：Tk的TKinter

Tkinter
我们来梳理一下概念：

我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

所以，我们的代码只需要调用Tkinter提供的接口就可以了。

'''

# import tkinter
from tkinter import *
import tkinter.messagebox as messagebox

class Application2(Frame):
    def __init__(self,master=None):
        # 调用父类的init方法
        super(Application2, self).__init__()   # 与下面语句相同
        # Frame.__init__(self,master)


        self.pack()   # 把Widget添加到父容器中
        self.createWidgets()
        self.crateWidgets2()

    def createWidgets(self):
        self.helloLabel = Label(self,text ='Hello World!')
        self.helloLabel.pack()
        self.quitButton = Button(self,text ='Quit',command=self.quit)   # 当Button被点击时，触发self.quit()使程序退出
        self.quitButton.pack()

    def crateWidgets2(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command = self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'   # or 后面是默认值
        messagebox.showinfo('Message','Hello, %s' % name)

# 第三步，实例化，并启动消息循环
app = Application2()
# 设置窗口标题
app.master.title('第一个图形界面')
# 主消息循环
app.mainloop()   # 主线程

'''
    pack()：把Widget添加到父容器中，并实现布局。 (最简单)
    grid()：复杂的布局
'''


# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写

'''
问题：
我用self.quit不好使，环境是3.6.4

通过百度这么解决的
增加以下代码

 import tkinter as tk

**root=tk.Tk()****        
app = Application(master=root)

 self.quitButton=Button(self,text='Quit',command=root.destroy)



'''