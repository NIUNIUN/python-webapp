#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Http 解析
HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

'''

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen
import re

class MyHTMLParser(HTMLParser):

    # 标签
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    # 单标签
    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    # 内容
    def handle_data(self, data):
        print(data)

    # 注释
    def handle_comment(self, data):
        print('<!--', data, '-->')

    # 特殊字符 英文表示
    def handle_entityref(self, name):
        print('&%s;' % name)

    # 特殊字符 中文表示
    def handle_charref(self, name):
        print('&#%s;' % name)

    def handle_decl(self, decl):
        print('decl= %s;' % decl)

    def handle_pi(self, data):
        print('data = %s;' % data)

content = '''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''

parser = MyHTMLParser()
# parser.feed(content)


'''  小结
feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
利用HTMLParser，可以把网页中的文本、图像等解析出来。
'''

'''
练习
找一个网页，例如https://www.python.org/events/python-events/，
用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
'''
class DefaultHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    # 标签
    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
           for attr in attrs:
               if re.match(r'list-recent-events', attr[1]):
                   self.flag = 1

        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'address'


    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    # 内容
    def handle_data(self, data):
        if self.flag == 1 and self.is_get_data :
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data:data})
            else:
                self.res[len(self.res)-1][self.is_get_data] = data
        self.is_get_data = None


URL = 'https://www.python.org/events/python-events/'
with urlopen(URL,timeout=1) as open:
    data =open.read().decode('utf-8')

parser = DefaultHTMLParser()
parser.feed(data)
for item in DefaultHTMLParser.res:
    print('--------------------')
    for key,value in item.items():
        print('%s : %s' % (key,value))
# print(data)

'''
res是一个list，存储所有会议
list的元素是dict
每个dict表示一个会议

获得title,即会议名时，给res添加一个新dict：
self.res.append({self.is_get_data: data})
res 由[] 变为 [{'title':'PyCascades 2018'}]

获得addr，time这样的其它属性时,先把最后一个dict（即当前处理的dict）取出：
即self.res[len(self.res) - 1]
再把新属性加入：
self.res[len(self.res) - 1][self.is_get_data] = data
 [{'title':'PyCascades 2018','time':'22 Jan. – 24 Jan.'}]

'''