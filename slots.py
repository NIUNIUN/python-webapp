#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

# 正常情况下，我们可以给实例绑定属性，也可以个实例绑定方法
# 但是，绑定的属性和方法只对当前实例有效，如果有要为所有实例绑定属性和方法，则可以为类绑定属性和方法
# __slots__ 可以限定绑定的属性
# __slots__ 只对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__，这时候子类运行绑定的属性就是父类+子类的__slots__

class Student(object):
    def __init__(self):
        pass


# 以下是给实例动态绑定属性和方法，只对当前实例起作用，不对Student其他实例有效
TomStudent = Student()

TomStudent.name = "tony"    # 动态绑定属性
print("name = ",TomStudent.name)


def print_info(self,student):
    print("print_info = ",self.name," class_name= ",student.__class__.__name__)

# 动态绑定方法
TomStudent.printf = MethodType(print_info,TomStudent)
TomStudent.printf(TomStudent)

# 验证print_info()，其他实例是否能调用
BobStudent = Student()
BobStudent.name = "bob"
# BobStudent.print()      # 不能调用，因为没有改方法


# 给所有实例绑定属性和方法，那就是对类进行绑定
Student.print = print_info

BobStudent.print(BobStudent)      # 对类进行绑定方法后，能够调用

class AStudent(Student):
    def __init__(self):
        pass

# 验证类绑定后的方法，子类是否能调用。
# 验证结果：子类能成功调用
AStudent = Student()
AStudent.name = 'A'
AStudent.print(AStudent)



# 限制实例属性 ，使用 __slots__
class Teacher(object):
    __slots__ = ('name','age')   # 允许被绑定的属性

ATeacher = Teacher()
ATeacher.name = "aTeacher"
# ATeacher.address = "xxx省xxx市"
print('ATeacher.name = ',ATeacher.name)
# print("ATeacher.address = ",ATeacher.address) # address不在允许属性范围内，报错


class BTeacher(Teacher):
    def __init__(self):
        pass

bTeacher = BTeacher()
bTeacher.name = "bTeacher"
bTeacher.address = "xxx省xxx市"
print('\nbTeacher.name = ',bTeacher.name)
print("bTeacher.address = ",bTeacher.address)
# 因为__slots__ ，只对当前实例起作用，对子类没有限制，还是可以绑定其他属性



# 作用：使用__slots__对子类也起作用，那么在子类中也定义__slots__
class CTeacher(Teacher):
    __slots__ = ('address')
    def __init__(self):
        pass

cTeacher = CTeacher()
cTeacher.name = 'cTeacher'
cTeacher.address ='xx省xx市'
# cTeacher.email = "123456789@qq.com"
print('\ncTeacher.name = ',cTeacher.name)
print("cTeacher.address = ",cTeacher.address)
# print("cTeacher.email = ",cTeacher.email)
# 因为子类也使用了__slots__，子类的__slots__ = 父类的__slots__ + 子类的__slots__



