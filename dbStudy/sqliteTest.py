#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
SQLite：使用C语言编写
'''
import sqlite3,os

# 1、连接到SQLite数据库
# 如果db文件不存在，会自动创建
conn = sqlite3.connect('D:/Python_workspace/test.db')

# 2、创建Cursor
cursor = conn.cursor()

# 3、执行SQL语句
# 创建表
# cursor.execute('CREATE TABLE user(id varchar(20) primary KEY ,name varchar(20))')

# 插入
# sql = 'insert into USER (id,NAME ) VALUES (\'2\',\'Tony\')'
# sql = 'insert into USER (id,NAME ) VALUES (\'1\',\'Tony\')'
# cursor.execute(sql)

# 获取插入的行数。没有插入数据时，值为-1
count = cursor.rowcount
print('插入的行数：',count)

# 查询
sql = 'select * from USER '
cursor.execute(sql)

# 获取查询结果集
values = cursor.fetchall()
print('查询结果：',values)

# SQL语句带参数，使用？占位符
sql2 = 'select * from USER WHERE  id =? '
cursor.execute(sql2,('1',))
values2 = cursor.fetchall()
print('有条件查询：',values2)

# 4、关闭Cursor
cursor.close()

# 提交事务
conn.commit()
# 关闭Connection
conn.close()

'''
Connection、Cursor对象，打开后一定要关闭
使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

'''


''' 练习
请编写函数，在Sqlite中根据分数段查找指定的名字：
'''
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
    conn = None
    cursor = None
    try:
        '返回指定分数区间的名字，按分数从低到高排序'
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        sql = 'select name from USER WHERE score BETWEEN ? AND ? ORDER BY score ASC'
        cursor.execute(sql,(low,high))
        values = cursor.fetchall()
        # values 值为 [(),()]
    except Exception as e:
        print(e)
    finally:
        if cursor == None :
            conn.close()
            cursor.close()
        pass
    return [x[0] for x in values]


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
