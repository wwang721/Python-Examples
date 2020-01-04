#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Created by WW on Dec. 22.
# All rights reserved.
#

import pymysql

# 定义数据库的连接信息
HOST = '127.0.0.1'  # MySQL 的 ip 地址, 不用 localhost 而是 127.0.0.1
USER = "wwang"  # 用户名
PASSWD = "w1998w0721"  # 密码
DATABASE = 'wwang'	# 数据库名称
PORT = 3306	# MySQL 数据库通用端口号 (默认ok)

print("连接 MySQL 数据库...")
# 建立与数据库的连接
mydb = pymysql.connect(HOST, USER, PASSWD, DATABASE, PORT, charset='utf8')

print("Link Successfully!\n")

print("用户名: " + USER)
print("选择数据库: USE " + DATABASE + "; MySQL --> Database changed ...\n")


TABLE = 'table_users'	# 数据表名称

# 新建查询页面
mycursor = mydb.cursor()


query =  'SELECT * FROM ' + TABLE
# 执行SQL查询语句
mycursor.execute(query)
print("执行: " + query + "\n结果:")

# 查看结果
# result = cursor.fetchone() #用于返回单条数据
results = mycursor.fetchall() #用于返回多条数据
print(results)


print("以表格形式展示:")
print("数组维度: " + str(mycursor.rowcount) + "*" + str(len(results[0]))) # 获取数组维度

print("# | ", end = "")
for row in mycursor.description:	# 通过 cursor.description 获得所有字段名并输出
	print(row[0], end = " | ")	# cursor.description 每行第一个元素即为字段名
print()

for index, row in enumerate(results):
	#print(results.index(row) + 1, end = " | ")	# 获取每行的序号
	print(index + 1, end = " | ") # 获取每行的序号
	for val in row:
		print(val, end = " | ")	# 输出所有值
	print()
print()


query = "SELECT user_name FROM " + TABLE
# 执行SQL查询语句
mycursor.execute(query)
print("执行: " + query + "\n结果:")
results = mycursor.fetchall() #用于返回多条数据
print(results)
print()


query = "SELECT Count(user_name) AS total_user_number FROM " + TABLE;
# 执行SQL查询语句
mycursor.execute(query)
print("执行: " + query + "\n结果:")
results = mycursor.fetchall() #用于返回多条数据
print(results)
print()


query = "SELECT user_name, password, phone FROM " + TABLE + " WHERE user_type <> 'root'";
# 执行SQL查询语句
mycursor.execute(query)
print("执行: " + query + "\n结果:")
results = mycursor.fetchall() #用于返回多条数据
print(results)
print()


# 关闭查询页面
mycursor.close()

# 关闭与数据库连接
mydb.close()


print("MySQL 测试成功!\n")










