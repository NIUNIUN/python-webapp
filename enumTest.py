#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum,unique


#  枚举类型
Month = Enum('Month3',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

# Month类型的枚举类
for name,member in Month.__members__.items():
    print(name,'>=',member,',',member.value)
    # value属性：自动赋给成员的int常量，默认从1开始

print("\nJan = %s \n" % Month.Jan)


# 自定义枚举类
#  @unique 装饰器：检查保证没有重复值(重复的成员名，重复的.value值)
# @unique
class Weekday(Enum):
    Sun = 0  # 如果不赋值，默认值为1
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print('day1 =',day1)
# print('day2 =',Weekday[2])  # 写法错误
print('day2 =',Weekday['Tue'])
print('day3 =',Weekday(6))    # 此时，0是成员名的.value值

# 结论：既可以用成员名称引用枚举常量，也可以直接根据value的值获得枚举常量
#      成员名不能重复，成员名对应的value可以重复，当value重复时，取第一个
#      Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。



# 练习：把Student的gender属性改造为枚举类型，可以避免使用字符串
Gender = Enum('Gender2',('Male','Female'))

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def print_info(self):
        print('\n[name = %s , gender = %s ]' % (self.name,self.gender))

Bob = Student('bob',Gender.Male)
print(Bob.print_info())
print('name = ',Bob.name,' gender =',Bob.gender.value)