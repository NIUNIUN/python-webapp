# 导入math模块，使用PI常量
import math
# 导入函数 规则： from 文件名 import 函数名
from collections import Iterable

# he = input("请输入身体:")
# we = input("请输入体重")
# height = float(he)
# weight = float(we)
# bmi = weight / (height * height)
# print('bmi = %s' % bmi)
#
# if bmi > 32:
#     print("严重肥胖")
# elif bmi > 28:
#     print("肥胖")
# elif bmi > 25:
#     print('过重')
# elif bmi > 18.5:
#     print('正常')
# else:
#     print('过轻')
# print("测试")
#
#
# #定义函数
# def area_of_circle(i):
#     for j in i:
#       area = math.pi*j*j
#       print(area)
#
# src = [12,13,14]  #初始化传入半径
# area_of_circle(src)#调用函数
#
#
# # 定义函数
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else :
#         return -x
#
# my_abs(25)
#
#
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s *x
#         return s
#
# # def power(x):
# #     s = 1
# #     s = x * x
# #     return s
#
# print('power = ',power(25))

#  *可变参数  ** 关键字参数  命名关键字参数
def product(*x):
    i = 0
    sum = 0
    for i in x:
        sum += i
    return sum

# print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

#  函数调用通过 栈 实现
#  递归函数注意栈溢出
def fact(n):
    if n ==1 :
        return n
    return n * fact(n-1)

# print("fact(5) = " , fact(5))
# print("fact(100) = ", fact(100))

# range() 范围函数 range(a,b) 区间
i = 0
for i in range( -15,-150,-2 ):
    print(" i = ",i)

    # range(5,10)

def move(n,a,b,c):
    if n == 1 :
        print(a," --> ", c)
    else :
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')

# Python 中使用缩进来控制循环体
# Python 切片 使用负数来取倒数
L = []
K = []
for i in range(10):
    L.append( i )
    K.append( i )

# print("python切片：",K[0:3])

# print("python切片：",L[0:7])
# print("K[]倒数第二个数 ",K[-2])

T = tuple(range(5,12))
T = K[ : ]
# print(" T = ",T)

# 使用切片，去除首尾空格
def trim(s):
    while s[0:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return s

print(" 去除空格:", trim("       hjkjk hjk   ! hjkhkj    "),"@")


# 迭代
d = {"name":'Bob',"age": 18,"address":'上海'}
print(" d = ",d)
#  dict默认迭代key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 同时迭代
for key,value in d.items():
    print("key = ",key,", value = ",value)

# 判断是否为迭代对象
print("是否为迭代对象： ",isinstance("ABC",Iterable))

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L == []:
        print("不能为空")
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if( max < i):
                max = i
            if( min > i):
                min = i
        print(max,min)

findMinAndMax([7, 1, 3, 9, 5])
findMinAndMax([])

s = "a"
s.upper()

d = ['x','Y','D',"MUdI",13,d]

[s.upper() if isinstance(s,str) else s for s in d ]

# print('BMI指数测试')
# name=str(input('请输入名字：'))
# ht=float(input('请输入%s的身高(m)：'% name))
# wt=float(input('请输入%s的体重(kg)：'% name))
# BMI=wt/ht/ht
# if BMI<18.5:
#     print('BMI指数为%.1f，%s体型过轻！'%(BMI,name))
# elif BMI<25:
#     print('BMI指数为%.1f，%s体型正常！'%(BMI,name))
# elif BMI<28:
#     print('BMI指数为%.1f，%s体型过重！'%(BMI,name))
# elif BMI<32:
#     print('BMI指数为%.1f，%s体型肥胖！'%(BMI,name))
# else:
#     print('BMI指数为%.1f，%s严重肥胖！'%(BMI,name))


# 素数
# 构造一个从3开始的序列
def _odd_iter():
    n = 1
    while True :
        n = n +2
        yield n
# 定义筛选器：
def _not_divisible(n):
    return lambda x: x % n > 0
# 定义生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)  #构造新的序列
# 打印1000以内所有素数
# for i in primes():
#     if( i < 1000 ):
#         print(i)
#     else:
#         break

# od = _odd_iter()   这两句在这里没什作用，只是记知识点
# od.send(None)  启动生成器  od.send() 切换到_odd_iter()执行
'''
http://blog.csdn.net/hedan2013/article/details/56293173
send方法和next方法唯一的区别是在执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定，从而实现与生成器方法的交互。
但是需要注意，在一个生成器对象没有执行next方法之前，由于没有yield语句被挂起，所以执行send方法会报错

因为当send方法的参数为None时，它与next方法完全等价。但是注意，虽然上面的代码可以接受，但是不规范。
所以，在调用send方法之前，还是先调用一次next方法为好。 
http://blog.csdn.net/iPenX/article/details/78096180
'''

# 回文数字
def _not_palindrome(n):
    return int(str(n)[::-1]) == n

def is_palindrome(n):
   return list(filter(_not_palindrome,range(1, 200)))

print("is_palindrome = ",is_palindrome(1234))

# def is_palindrome(n):
#     return int(str(n)[::-1])==n

# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 保留奇数
def is_odd(n):
    return n % 2 == 1

print(" is_odd = ",list( filter(is_odd,range(1,100)) ))

# 把序列中的空字符串删除
# strip() : 取出字符串首尾空格或指定字符串
# lstrip(): 只删除头部 rstrip()：只删除尾部
def trim(s):
    print("strip =",s.strip(" "))
    return s and s.strip()
print(" not_empty =",list(filter(trim,[" a df fd ",' dsfs            dsfd ',' fsdd','      '])))

str='       fdg'
print(" str.strip =",str.strip())

# sorted 排序算法 、高阶函数
#  接收一个key函数实现自定义排序 第二个参数
#  反向排序：第三个参数：reverse=True

# 按照名字排序
def by_name(t):
    # L = [i for i in t.key]
    # print(" = ", L)
    return t[0]

def by_score(t):
    return t.values()

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print("sorted by_name = ",sorted(L,key=by_name))
print("sorted by_score= ",sorted(L,key=by_score))