#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
# 注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。

# 执行INSERT等操作后要调用commit()提交事务；

# MySQL的SQL占位符是%s

# 导入MySQL驱动
import mysql.connector

# 连接数据库
conn = mysql.connector.connect(user="root", password="123456789", database="test")
cursor = conn.cursor()

# cursor.execute('create table book(id VARCHAR(20) PRIMARY KEY ,NAME VARCHAR(20),user_id VARCHAR(20),FOREIGN KEY(user_id) REFERENCES USER(id)) ')
# 建表
# cursor.execute("create table mysql_user (id varchar(20) primary key , name varchar(20))")
# 添加数据
# for x in range(3):
#     cursor.execute("insert into mysql_user (id, name) values (%s, %s)", [str(x), "TaoYuan"+str(x)])
# print(cursor.rowcount)


# 提交事务
conn.commit()
cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute("select * from mysql_user")

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()