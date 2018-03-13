#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 防止黑客反推原始口令
# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
# Hmac算法：所有哈希算法都通用，MD5、SHA-1等。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

import hmac
import random

message = 'how do you do!'.encode('utf-8')  # 必须指定编码格式
key = b'hello'             # key：必须是二进制，不能是str
h = hmac.new(key,message,digestmod='MD5')
sha = hmac.new(key,message,digestmod='sha1')
h = h.hexdigest()
sha = sha.hexdigest()
print('md5- hexdigest=%s , len=%d' % (h,len(h)))
print('sha1 - hexdigest=%s , len=%d' % (sha,len(sha)))


# 可见使用hmac和普通hash算法非常类似。
# hmac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。


# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
# 使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。


# 练习 将上一节的salt改为标准的hmac算法，验证用户口令：

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('\nok')
