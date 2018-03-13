#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'contextlib 上下文管理'

from contextlib import contextmanager,closing
from urllib.request import urlopen

with open('D:\遇到的错误.txt','r') as f:
    print(f.read())

# 任何对象，只要正确实现了上下文管理，就可以使用with语句

# 自定义实现上下文管理（__enter__、__exit__）
class Student(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('\nBegin2')
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

student = Student('Tom')
student.query()

with Student('Tony') as student:
    student.query()


# __enter__、__exit__两个方法太繁琐，使用@contextmanager
class Teach(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('\nBegin')
    teach = Teach(name)
    yield teach
    print('End')

with create_query('Teach') as te:
    te.query()


# 在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print('\n<Begin - %s>' % name)
    yield
    print('<End - %s>\n' % name)

with tag('Hello') as t:
    print('world')
    print('!')

# 遇到yield会暂停往下继续执行，返回到函数被调用的地方，然后再执行yield之后的语句


# @closing ：把对象变成上下文对象
with closing(urlopen('https://www.baidu.com/')) as page:
    for line in page:
        print(line)


def tag2(name):
    print('\n<Begin - %s>' % name)
    yield
    print('<End - %s>\n' % name)

with closing(tag2('Hello')) as t:
    print('\npython')
    print('!')

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
# 作用: 把任意对象变为上下文对象，并支持with语句。

# http://www.cnblogs.com/nnnkkk/p/4309275.html

# *********** 小结******
# 例如with context_expression [as target(s)]:
#     with-body，

   # 它的执行顺序是这样的

# 1.执行 context_expression，生成上下文管理器 context_manager

# 2.调用上下文管理器的 enter() 方法；如果使用了 as 子句，则将 enter() 方法的返回值赋值给 as 子句中的 target(s)

# 3.执行语句体 with-body

# 4.不管是否执行过程中是否发生了异常，执行上下文管理器的 exit() 方法，exit() 方法负责执行“清理”工作，如释放资源等。
# 如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，则以 None 作为参数调用 exit(None, None, None) ；如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用 exit(exc_type, exc_value, exc_traceback)

# 5.出现异常时，如果 exit(type, value, traceback) 返回 False，则会重新抛出异常，让with 之外的语句逻辑来处理异常，这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理



