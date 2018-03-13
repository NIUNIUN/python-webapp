#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'知识点：类 学生类'

# 类名后的括号，括号中表示基础哪个类，默认为object
# 类的方法：第一个参数必须是self
class Student(object):
    # 第一个参数self，表示实例本身

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def toString(self):
        return "[name = "+self.__name+",score = "+str(self.__score)+"]"


#     访问修饰符：
#               私有（private）： 在名称前添加2个下划线
#               保护（protected）： 一个下划线
bar = Student("fs",189)
# bar = Student()
# bar.name =  'djkddddddddljkl'
# bar.score = 180
# print("score = %s " %bar.get_score())
print("toString = %s " % bar.toString())
print("name = %s " % bar.get_name())
print("name = %s ,score = %s " % (bar.get_name(),bar.get_score()))

