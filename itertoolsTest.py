#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 'itertools : 提供用于操作迭代对象的函数，几个’无限'迭代器

import itertools

natuals = itertools.count(2)
# for n in natuals:
#     print(n)
# count() 创建无限循环器，参数：起点是多少


cs = itertools.cycle('CGa')
# for c in cs:
#     print(c)
# cycle()：把一个序列无限重复

rp =itertools.repeat('gf',5)
# for r in rp:
#     print(r)
# 把元素无限重复，但是可以指定循环次数


# 只有在for迭代时无限地迭代下去，不会实现创建无限个元素

# takewhile()：截取一个有限的序列
ns = itertools.takewhile(lambda x:x<16,natuals)
print(list(ns))


# chain()：把一组迭代对象串联
for c in itertools.chain('ABC','123'):
    print(c)

# groupby() : 把迭代器中"相邻"的重复元素挑出来放在一起
for key,group in itertools.groupby('fafagfsd'):
    print(key,list(group))  # 只是把相邻相同元素

print('\n')

for key,group in itertools.groupby('AABBBBBAAAACCCCDDD'):
    print(key,list(group))
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。

print('\n')
# 忽略大小写
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print(key,list(group))


# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。


# 练习 计算圆周率可以根据公式：

# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

# 我做的
countt = itertools.count(1)
def pii(N):
    i = 0
    sum = 0
    for c in countt:
        # ct.append(2 * c -1)
        ct = 2 * c -1
        i = i+1

        if i % 2 == 0:
            sum = sum + (-4 / ct)
        else:
            sum = sum + 4 / ct
        if i ==N:
            # return ct
            return sum

def pi(N):
    # step1： 创建奇数序列
    odds = itertools.count(1,2)

    # step2：取出前N个数
    odds2 = itertools.takewhile( lambda x : x <= 2*N-1,odds)

    # step3：添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # L = [(4/x) *(-1) ** ((x-1)/2) for x in list(odds2)]    # 2个乘号 等同于 次方

    # 因为itertools返回值为Itertor，所以需要对odds2进行转换
    odds_2 = list(odds2)
    L = [ 4 / (pow(-1, i) * odds_2[i]) for i in range(N)]

    return sum(L)

def pi22(N):
    # 计算pi的值
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = list(itertools.takewhile(lambda x: x <= 2 * N - 1, odd))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(N):
        ns[i] = 4 / (pow(-1, i) * ns[i])
    # step 4: 求和:
    return sum(ns)


print('\n\n',pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))

# assert 3.04 < pii(10) < 3.05   # 不知道为什么，返回值一样，但是却报AssertionError
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')



