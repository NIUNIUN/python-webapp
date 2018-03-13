#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用@property ,节省get、set方法
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int) and value > 0:
            raise ValueError('score must be an integer!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value, int) and value > 0:
            raise ValueError('score must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


s = Screen()
s.width = 10
s.height = 76
print('resolution =', s.resolution)
if s.resolution == 760:
    print('测试通过!')
else:
    print('测试失败!')

# 属性名和方法名相同时，需加下划线进行区分，否则会报错（否则会超出递归上限报错）