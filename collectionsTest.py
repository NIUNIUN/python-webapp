#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# collections：集合类
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# namedtuple ('名称',[属性list]):
# 创建自定义tuple对象，规定tuple元素个数，使用属性引用tuple中元素（不是索引）
P = namedtuple('Point',('x','y'))
# P.x = 1
# P.y = 6
Point = P(6,19)
print('(x,y) = ',P.x,P.y)

print('',isinstance(Point,P),'',Point.x,Point.y)

Circle = namedtuple('Circle',['x','y','r'])
c = Circle(5,5,10)
print('圆：',c.x,c.y,c.r)




#deque：高效实现插入和删除的双向列表，适于“队列”，“栈”
q = deque([1,2,3])  #deque([1,2,3])
print('\n',q)
q.append('x')
q.appendleft('Y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)
# deque 中pop不能带参数？


# defaultdict : dict中key不存时，返回默认值
#             默认值由函数返回
dfd = defaultdict(lambda : 'no key')
dfd['address'] = 'xxx省'
# dfd = {'df':1,'d':2,'c':4}   # 使用defaultdict，就不能使用直接赋值
print('\n',dfd['address'],dfd['name'])


# OrderedDict：使dict中有序
# dict：key是无序
d = dict( {'a': 1, 'b': 2, 'c': 3})
t = dict([('name','bob'),('address','xxx省'),('age',18)])
print('\n',d)   #为何输入时有序的呢(⊙o⊙)？
print(t)
od = OrderedDict({'name':'Tom','ID':123456789,'Email':'22@qq.com'})
od['address'] = 'fsd'
print(od,'\n')


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey == self._capacity:     # 使用>=报错
        # if len(self) == self._capacity and containsKey == 0:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


last = LastUpdatedOrderedDict('nono')
last.__setitem__('d',3)
last.__setitem__('d',38)
print(last)

# Counter：计数器
counter = Counter()
for ch in 'fsdfafageklajgeae13agfaeag':
    counter[ch] = counter[ch] +1

print('\nCounter计数器\n',counter)