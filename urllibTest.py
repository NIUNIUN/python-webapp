#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import json


# 利用urllib读取JSON，然后将JSON解析为Python对象：

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
def fetch_data(url):
    js = request.urlopen(URL).read()
    return json.loads(js)

data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')


# urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。


