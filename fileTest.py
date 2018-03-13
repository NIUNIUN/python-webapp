#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  io import StringIO,BytesIO

# IO编程
# 可能产生IOError，需要try... finally
f = ()
try:
    f = open('D:\日志.txt','r')
    s = f.read()
    # print('content = ',s)
finally:
    if f:
        f.close()

# 以上写法可使用with代替，自动调用close
with open('D:\日志.txt','r') as f:
# with open('D:\tangxueqing\7934336_银河.PNG','r') as f:   # 不能使用‘r’模式读取图片，因为是二进制文件
    line = f.readlines()
    for content in line:
        # print(content)     # 每输出一行，都会添加换行符
        print(content.strip())     # 可以使用strip(),去除"\n"
    # print("\nwith语法：",f.read())

# 读取文件内容，可使用：
# read()会一次性读取文件的全部内容，
# read[size]-每次读取size个字节，
# readline()-每次读取一行，
# readlines()-读取全部内容并返回list，每输出一行，都会添加换行符


# file-like Object：像open()函数返回的这种有个read()方法的对象。例：file，内存流、网络流、自定义流等
# StringIO：临时缓冲流，内存中创建的file-like Object

# 读取二进制文件（图片、视频、音频），使用‘rb’
with open('D:/tangxueqing/7934336_银河.PNG','rb') as f:
    pass
    # print("二进制文件：",f.read())

    # line = f.readlines()
    # for i in line:
    #     print(i.strip())

# 字符编码
# 忽略由于编码格式不同导致的错误 error='ignore'
with open('D:/遇到的错误.txt','r',encoding='gbk') as f:
    print("\n指定编码格式：",f.read())

# 写文件
# 模式：w/wb 文本文件/二进制文件 --- 会覆盖之前的内容
# with open('D:/遇到的错误.txt','w',encoding='gbk') as f:
#     f.write("hdjkfsd")

# 模式：a -- 追加
with open('D:/遇到的错误.txt','a',encoding='gbk') as f:
    a = ['中国','英国','法国','日本']
    for k in a:
        f.write(k)
# write() 返回值为：写入字符格式



######### 字符流（缓冲流） StringIO  #########
# 写入内存中
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print('缓冲流：',f.getvalue())   # 使用getvalue,获取写入的值

# 读文件
f = StringIO('hello world ')
while True:
    s = f.readline()
    if s == '':  # 读取到最后
        break
    print('content =',s)

sio = StringIO()
sio.write('fsdfsdfsdfsdfsdfsd')
sio.seek(0,2)
print(sio.tell())

# 这就涉及到了两个方法seek 和 tell
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦


######### 字节流 BytesIO  #########
# 写入数据
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 因为是字节流，写入的是二进制，所以要转换编码格式
print('字节流=',f.getvalue())

# 读取数据
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
con = f.read()
print('解码=',con.decode('utf-8'))