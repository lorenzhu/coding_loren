#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import pymysql
import getpass

# 打开数据库连接
username = input("MySQL username: ")
# 注意：密码不回显，IDEL直接运行会报错，使用 cmd 会好些
password = getpass.getpass("password: ") 
database = input("database name: ")
#username = "root"
#password = "666nicai"
#database = "testdb"
#db = pymysql.connect("localhost", username, database, database)
db = pymysql.connect("localhost", username, password, database)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

cursor.execute("SELECT VERSION()")  # 使用 execute() 方法执行 SQL 查询
data = cursor.fetchone()            # 使用 fetchone() 方法获取单条数据
print("Database Version: %s " % data)



# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
 
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

cursor.execute("SHOW TABLES")
data = cursor.fetchone()
print("Database Tables: %s " % data)



# =============插入操作===================================================
# sql = """INSERT INTO EMPLOYEE Values("Mac", "Mohan", 20, "M", "2000")"""
sql = "INSERT INTO EMPLOYEE \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

try:
    cursor.execute(sql)
    db.commit() # 提交到数据库执行
except:
    db.rollback() # 如果发生错误则回滚

cursor.execute("Select * from employee")
data = cursor.fetchone()
print("Data: %s  %s  %d  %s  %s " % data)


#=========================查询操作==================================================
print("\n查询操作")
sql = "select * from employee where INCOME> %d " % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        #pass
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % row)
except:
    print("Error: unable to fetch data")

#==========================更新操作==================================================
print("\n更新操作")
sql = "update employee set AGE = AGE + 1 \
        Where SEX = 'M' "
try:
    cursor.execute(sql)
    sql = "select * from employee"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        #pass
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % row)
    db.commit()
except:
    db.rollback()

#==========================删除操作=================================================
print("\n删除操作")
sql = "delete from employee where age>20 "
try:
    cursor.execute(sql)
    sql = "select * from employee"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        #pass
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % row)
    db.commit()
except:
    db.rollback()
    

db.close()  # 关闭数据库连接
