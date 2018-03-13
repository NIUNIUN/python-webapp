#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# chardet 字符编码
import chardet

en = chardet.detect(b'hello,world!')
print(en)
# 结果：confidence-检测的概率1.0(100%)  language-检测的的语言

data = '中国'.encode('gbk')
print("\n",chardet.detect(data))

data = '的设计费了卡机oem快乐就凶恶诞生了空间额'.encode('gbk')
print("\n",chardet.detect(data))
# Russian 俄罗斯

data = '的设计费了卡机oem快乐就凶恶诞生了空间额'.encode('utf-8')
print("\n",chardet.detect(data))


data = '最新の主要ニュース'.encode('euc-jp')
print("\n",chardet.detect(data))


# 使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。