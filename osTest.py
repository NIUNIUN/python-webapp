#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,shutil
from datetime import datetime

# 操作文件和目录

#  操作系统名
print('os.name = %s\n' % os.name)
#  posix -- Linux、Unix、Mac OS X    nt--windows

# 详细的系统信息
try:
    print('detailInfo = %s' % os.uname())
except Exception as e:
    print(e)
# windows 不提供uname函数

# 环境变量
print("\n环境变量= %s \n" % os.environ)
# 获取指定环境变量的值
print('jave-path value= %s \n' % os.environ.get('JAVA_HOME'))

# 操作文件和目录函数：一部分在os中，一部分在os.path

# 查看绝对路径
print('当前目录的绝对路径 = %s ' % os.path.abspath('.'))

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数,避免路径分隔符
tempPath = os.path.join('D:\\','testdir')
# os.rmdir('D:\\testdir') # 删除目录。如果目录是空的，则不能删除
# os.mkdir(tempPath)  # 创建目录。如果文件目录已存在，则不能创建，并报错


#  拆分路径 ,os.path.split()
splitPath = os.path.split('D:\Python_workspace\first.py')
print('拆分路径=',splitPath)

# os.rename('E:\新建文本文档 (2).txt','E:\error.txt')  #重命名

# os.remove('E:\新建文本文档.txt')  # 删除文件


# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
print('复制文件= %s' % shutil.copyfile('D:\遇到的错误.txt','e:\遇到的错误.txt'))


#  过滤文件
fi = [os.path.join('.',x) for x in os.listdir('.') if os.path.isdir(x)]
print('目录列表：%s \n' % fi)

#  练习：
# 利用os模块编写一个能实现dir -l输出的程序。
rootPath = 'D:/workspace'
for t in os.listdir(rootPath):
    fname = os.path.join(rootPath,t)  # t-- 只是文件名，不带路径。所以直接使用t，会找不到文件
    fsize = os.path.getsize(fname)
    fmtime = str(datetime.fromtimestamp(os.path.getmtime(fname))).split('.')[0]
    flag = '/' if os.path.isdir(fname) else ''
    print('%10d   %s   %s%s' % (fsize, fmtime, fname, flag))

print('\n')
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def find(keyword,path='.'):
    if not isinstance(keyword,str) or not os.path.exists(path):
        return None
    for t in os.listdir(path):
        filepath = os.path.join(path,t)
        if os.path.isdir(filepath):
            find(keyword,filepath)

        if keyword in t:
            print(filepath)
if __name__ == '__main__':
    find('keystore','D:/workspace')

print('\n判断是否存在：%s\n' % os.path.exists('D:/workspace'))




