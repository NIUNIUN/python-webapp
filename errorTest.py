#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pdb
logging.basicConfig(level=logging.INFO)

#  错误处理
# 捕获错误:
#         try ... except ... finally
try:
    print('try....')
    r = 10 / 0
    print('result = ',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally')
print('end\n')



#  抛出异常：
#           raise
def fun(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value = %s' )
    return 10 / n

def barr(s):
   try:
       fun(s) *3
   except ValueError as e:
       print("except=")
       raise
barr(1)

#  记录错误：
#          logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return  foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        # logging.exception(e)
        logging.info(e)   # 输出错误信息，前提需要制定logging的级别，否则不会输出 ：logging.basicConfig(level=logging.INFO)
    finally:
        print('finally')

main()
print('end\n')
#  打印异常栈信息（红色信息），正常退出。（和捕获异常方法差不多，只是多了异常栈信息）


#  使用pdb，以单步方式进行运行，查看运行状态
# -m pdb ： 启动
# l ： 查看代码
# p 变量名： 查看变量对应的值
# q : 退出程序

#  使用pdb.set_trace() ,相当于设置了一个断点
pdb.set_trace()  #程序运行到这条语句时会暂停


# 调试总结
#  调试的方式：
#     1、用print()把可能有问题的变量打印出来看看
#     2、使用assert(断言)  ：启动Python解释器时可以用-O参数来关闭assert：
#     3、使用logging(日志)，logging不会抛出错误，而且可以输出到文件。
#     4、pdb（Python的调试器），让程序以单步的方式运行
#     5、pdb.set_trace()