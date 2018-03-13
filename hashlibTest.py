#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'摘要算法：MD5、SHA1等'

# MD5： 128bit,32位的16进制
# SHA1：160bit,40位的16进制
import hashlib


md5 = hashlib.md5()
# md5.update('how do you do')    # 必须指定编码格式
md5.update('how do you do?'.encode('utf-8'))
hex = md5.hexdigest()
print('md5.hexdigest =%s len=%d' % (hex,len(hex)))


sha1 = hashlib.sha1()
sha1.update('how do you do?'.encode('utf-8'))    #必须指定编码格式
sha = sha1.hexdigest()
print('\nsha1.hexdigest =%s len=%d' % (sha,len(sha)))


# 练习： 根据用户输入的口令，计算出存储在数据库中的MD5口令：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_md5(password):
    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()

def login(user, password):
    if user == None or password == None:
        return None
    pwd = calc_md5(password)
    if db[user] == pwd:
        return True
    else:
        return False

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
# 但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
