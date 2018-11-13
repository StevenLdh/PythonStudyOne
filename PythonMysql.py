#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# 引入数据库驱动
import mysql.connector
# 创建数据实体
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="cc_erp"  # 数据库名称
)
# 查询数据库表中数据
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM bas_account")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)

"""
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "qwert", "world")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM city")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print(data)

# 关闭数据库连接
db.close()

