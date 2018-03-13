#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

# 知识点：多态
# “开闭”原则：
#           对扩展开放：允许新增子类
#           对修改封闭：不需要修改依赖父类的函数
# 函数的：必选参数、默认参数、可变参数、关键字参数、命名关键字参数
class Animal(object):
    def __init__(self,name = '',score=''):
        self.name = name
        self.score = score
    def run2(self):
        print("Animal is running...  name = %s ,score = %s " % (self.name,self.score))
    def __test2(self):
        pass

class Dog(Animal):
    def run(self):
        print("Animal is running...  name = %s ,score = %s " % (self.name, self.score))

class Cat(Animal):
    def run(self):
        print("Animal is running...  name = %s ,score = %s " % (self.name, self.score))

def run_twice(ani):
    ani.run()
    ani.run()

animal = Animal()
dog = Dog('580',789)
cat = Cat('qwe',123)

animal.run2()
# dog.run()
# cat.run()

run_twice(dog)
# java是静态语言，公共方法必须是父类或子类
# pythoon：动态语言（不要求严格的继承体系），只要对象有公共方法，不用管是否是继承同一个类


# type : 获取对象信息
t = abs
print("\nt的类型：",type(t))
print(" dog的类型：",type(dog))

def fn():
    if(__name__ == '__main__'):
        print("函数")

fn()
# % 代表格式化
# types ： 判断是否是函数 isinstance：判断是否是类的对象
print("\n判断是否是函数：%s" % (type(fn)==types.FunctionType))

# dir ：获取对象的所有属性和方法
#  与反射相似
print("\n\nobject对象的所有属性和方法：",dir(object))
print("\nabs对象的所有属性和方法：",dir(t))
print("\nanimal对象的所有属性和方法：",dir(animal))
print("\ncat对象的所有属性和方法：",dir(cat))

print('\nhasattr:是否有某个属性或方法',hasattr(dog,'age'))
print('setattr:设置某属性值或方法',setattr(dog,'name','dogdog'))
print('getattr：获取某属性值或方法 ',getattr(dog,'name',))
print('getattr：获取某属性值(属性不存在时返回默认值) 或方法',getattr(dog,'age',999))

print('\nhasattr:是否有某个属性或方法',hasattr(dog,'run'))
print('getattr：获取某方法',getattr(dog,'run'))
print('getattr：获取某方法(属性不存在时返回默认值)',getattr(dog,'runner','notmethond'))
print('setter:',setattr(dog,'runner2','runn2'))
print('getattr:',getattr(dog,'runner2'))
print('dog =',dog.runner2)


