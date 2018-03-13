#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 解析XMl：DOS、SAX
# DOS：DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX：流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# 优先考虑SAX，因为DOM实在太占内存。
from base64 import encode
from urllib import request
from xml.parsers.expat import ParserCreate

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self,name):
        print('sax:end_element: %s' % name)

    def chart_data(self,text):
        print('sax:char_data: %s' % text)

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.chart_data
parser.Parse(xml)


# 生成XML：拼接字符串
def xml_join():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(encode('some & data'))
    L.append(r'</root>')
    return ''.join(L)

# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。


'''  练习
请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：

https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml

参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
'''
res = {'city':'','forecast':[]}
class DefaultSaxHandler2(object):
    def start_element(self,name,attrs):
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if 'location' in name:
            res['city'] = attrs['city']
        if 'forecast' in name:
            res['forecast'].append({'date':attrs['date'],'high':attrs['high'],'low':attrs['low']})

    def end_element(self,name):
        pass
        # print('sax:end_element: %s' % name)

    def chart_data(self,text):
        pass
        # print('sax:char_data: %s' % text)

def parseXml(xml_str):
    print('\n\n',xml_str)
    print('\n\n')
    handler = DefaultSaxHandler2()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.chart_data
    parser.Parse(xml_str)
    return  res

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print('ok! result= %s ' % result)