#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'正则表达式'
import re

# 切分字符串
str = 'a b   c'.split(' ')
print('分割=',str)

str = re.split(r'[\s\,]+','a,b, f cd g')
print('分割=',str)


# 分组 使用()表示要提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$','010-1245')
print('分组',m)
print('分组后-原始数据=',m.group(0))  # 修正，应该是贪婪匹配的最大长度
print('分组后',m.group(1))

m = re.match(r'(\d*)','010-123')
print('\n分组后，group(0)为贪婪的最大长度',m.group(0))



t='00:00:59'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print('\n提取子串',m.groups())


# 贪婪匹配（默认）
str = re.match(r'^(\d+)(0*)$','1302000')
print('\n贪婪匹配',str.groups())

str = re.match(r'^(\d+?)(0*)$','1203000')
print('非贪婪匹配',str.groups())

# \d+ 采用贪婪匹配
# \d+? 加个？让\d+采用非贪婪匹配


# 编译，re模块内部干两件事：
# 1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2、用编译后的正则表达式去匹配字符串。


# **********  预编译 ************
# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
re_phone = re_telephone.match('010-12345').groups()
print('\n预编译',re_phone)

# 练习一
re_email = re.compile(r'^\w+[0-9a-zA-Z\.]*@\w+\.\w{3}$')
def is_valid_email(addr):
    if re_email.match(addr):
        return True
    else:
        return False
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok\n')


# 练习二 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

def name_of_email(addr):
    m = re.match(r'.+?(\w*[\w\s]*).+?([\s\w]*)@([0-9a-zA-Z]*)\.(\w+)$',addr)
    # m = re.match(r'(\w+)@(\w+)\.(\w+)$',addr)
    if m != None:
        return m.group(1)

    return None
    # a = re.match(r'^\<?([\w\s\.\_]+)\>?\s*?[\w\.\_]*?@\w+\.\w+$', addr)
    # return a.group(1)

assert name_of_email('[Tom Paris] tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

# addr = 'tom@voyager.org'
# m = re.match(r'(\w+)@(\w+)\.(\w+)$',addr)
# print(m.group(1))