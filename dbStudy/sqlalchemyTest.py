#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
ORM：Object-Relational Mapping
Python 中 ORM框架: SQLAlchemy
'''

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 1、创建对象的基类
Base = declarative_base()

# 2、定义User对象
class UserTest(Base):
    # 表名
    __tablename__ = 'user'   # 固定值：__tablename__

    # 表结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    # 一对多
    books = relationship('Book')

# 一对多
class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20),ForeignKey('user.id'))

# 3、初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456789@localhost:3306/test')
# 4、创建DBSession类型
DBSession = sessionmaker(bind=engine)

# create_engine()：初始化数据库连接。
# 连接信息： '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 有了ORM，向数据库中插入一条数据
def insertInto_User():
    # 1、创建session对象
    session = DBSession()
    # 2、创建新User对象
    new_user = UserTest(id='3',name='Bob3')
    new_user2 = UserTest(id='4',name='Tom4')
    # 3、添加到session中
    session.add(new_user)
    session.add(new_user2)
    # 提交并保存到数据库
    session.commit()
    session.close()

def inserInto_Book():
    session = DBSession()
    new_book = Book(id ='10',name='数据结构',user_id ='1')
    new_book2 = Book(id ='11',name='汇编语言',user_id='2')
    new_book3 = Book(id ='12',name='软件工程',user_id='1')
    session.add(new_book)
    session.add(new_book2)
    session.add(new_book3)

    session.commit()
    session.close()

# insertInto_User()
# 需要提前创建book表.并设置外键
# inserInto_Book()

# 查询
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(UserTest).filter(UserTest.id == '1')
print('type:',type(user))
print('\n直接输出:',user)
''' 直接输出 一下是不加one()、all()返回   
name: SELECT user.id AS user_id, user.name AS user_name 
FROM user 
WHERE user.id = %(id_1)s
'''
print('\nname:',user.name)
print('\nbook:',user.book)

session.close()

'''
查询语句：如果最后不加one()或all()，返回的是sql语句
         one()：返回一个对象
         all(): 返回所有对象
'''

'''
    小结：ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换
'''
