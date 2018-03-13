#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

#  单元测试
# 练习： 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过

#  修改前的代码
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 60:
#             return 'B'
#         if self.score >= 80:
#             return 'A'
#         return 'C'

# 修改后的代码（粗略修改）
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError('test_invalid')

        if self.score >= 80:
            return 'A'

        if self.score >= 60:
            return 'B'
        return 'C'

class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart',80)
        s2 = Student('Lisa',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart',-1)
        s2 = Student('Lisa',101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

#  判断是否在主函数中运行
if __name__ == '__main__':
    unittest.main()



#单元测试中写两个特殊的方法setUp,setDown,这两个方法会分别在没调用一个测试方法的前后分别执行
# 比如我们要测试一个跟数据库有关的程序时，就可以在setUp中链接数据库，在setDown中关闭数据库


