#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python实例属性、类属性

# 实例属性和类属性使用相同的名字时：
#      因为相同名称的实例属性将屏蔽掉类属性，
#      但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

class Teacher(object):
    # 类属性 （java中类变量、static变量），无论创建多少个对象、类属性只有一个，对象共享类属性
    count = 0;

    def __init__(self,name='null'):
        Teacher.count = Teacher.count + 1
        self.name = name   # name 为实例变量（java中成员变量），每一个对象有一个

    def print_count(self):
        print('老师个数为：',Teacher.count)

TomTeacher = Teacher()
TomTeacher.print_count()

TonyTeacher = Teacher('Tony')
TonyTeacher.print_count()

BobTeacher = Teacher('Bob')
BobTeacher.print_count()



