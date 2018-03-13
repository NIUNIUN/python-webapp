#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文档测试：不仅可以用来测试，还可以作为示例代码

#  写了个函数，或者写了个类，具体要怎么使用，可以在注释中说明，然后写个文档测试放在里面，在直接运行命令的时候，执行文档测试

# 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
# 所以，不必担心doctest会在非测试环境下执行。

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。