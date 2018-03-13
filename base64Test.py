#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64编码：将3个字节的二进制数据编码为4字节的文本数据，长度增加33%

# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64,re
base = base64.b64encode(b'binary\x00string')
print('编码' , base)
print('解码',base64.b64decode(base))

# 标准的Base64编码后可能会出现+和/，在URL中不能直接作为参数,
# 使用urlsafe，将+和/变成- 和 _
base2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
urlBase = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print('\n编码：',base2)
print('url编码：',urlBase)
print('url解码',base64.urlsafe_b64decode(urlBase))



# 练习：请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    # 判断传入参数的类型
    if type(s) is bytes:
        s = str(s,encoding='utf-8')

    # 字符串的长度变为4的倍数
        s = s + str((-len(s) % 4)*'=')
        print('s=',s)
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# safe_base64_decode(b'YWJjZ===')  为什么补三个=就报错呢
print('\nok')

# 编码前是3的倍数，编码后是4的倍数
