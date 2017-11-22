# Python connect MySQL
#_*_ coding:utf8_*_
import sys
import pymysql

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn
    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise(e)
        
    def check_acct_available(self, acctid):
        cur = self.conn.cursor()
        try:
            sql = "select * from bankaccount where acctid=%s" % acctid
            cur.execute(sql)
            print("check_acct_available: " + sql)
            data = cur.fetchall()
            if len(data) != 1:
                
                raise Exception("账号%s不存在" % acctid)
        finally:
            cur.close()

    def has_enough_money(self, acctid, money):
        cur = self.conn.cursor()
        try:
            sql = "select * from bankaccount where acctid=%s and money>%s" % (acctid, money)
            cur.execute(sql)
            print("has_enough_money: " + sql)
            data = cur.fetchall()
            if len(data) != 1:
                raise Exception("账号%s没有足够的钱" % acctid)
        finally:
            cur.close()
            
    def reduce_money(self, acctid, money):
        cur = self.conn.cursor()
        try:
            sql = "UPDATE bankaccount SET money = money-%s WHERE acctid = %s " % (money, acctid)
            cur.execute(sql)
            print("reduce_money: " + sql)
            data = cur.fetchall()
            if cur.rowcount != 1:
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cur.close()
            
    def add_money(self, acctid, money):
        cur = self.conn.cursor()
        try:
            sql = "UPDATE bankaccount set money = money+%s WHERE acctid = %s " % (money, acctid)
            cur.execute(sql)
            print("reduce_money: " + sql)
            
            data = cur.fetchall()
            if cur.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cur.close()
        pass
    

if __name__ =="__main__":
    #source_acctid = sys.argv[1]
    #target_acctid = sys.argv[2]
    #money = sys.argv[3]
    source_acctid = int(input("source_acctid: "))
    target_acctid = int(input("target_acctid: "))
    money = int(input("money: "))

    conn = pymysql.connect(host = 'localhost',  port = 3306,
                           user = 'root',       passwd = '666nicai',
                           charset = 'utf8',
                           db = 'mooc'
                           #db = 'python',#db = 'classb'
                           )
    tr_money = TransferMoney(conn)
    cur = conn.cursor()

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print(e)
    finally:
        conn.close()

'''       
sql = "SELECT name,number FROM members"
cur.execute(sql)
data = cur.fetchmany(20)
for dd in data:
    print("姓名：%s\t  学号：%s" % dd)

    
try:
    sql_insert = "INSERT INTO members(Number, Name) VALUES('17215XXX','Loren')"
    sql_update = "UPDATE members set Name='James' WHERE Number='17215XXX'"
    sql_delete = "ELETE FROM members WHERE Name='James'"
    cur.execute(sql_insert); print(cur.rowcount)
    cur.execute(sql_update); print(cur.rowcount)
    cur.execute(sql_delete); print(cur.rowcount)

    conn.commit()
except Exception as e:
    print("==========失败==========")
    print(e)
    conn.rollback()
'''
#================================================
'''
sql = "CREATE TABLE pydb( id TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, username varchar(20) NOT NULL, password varchar(20))"
cur.execute(sql)
print(cur.fetchone())
sql = "INSERT INTO pydb VALUES(NULL, 'loren', '6666')"
cur.execute(sql)
print(cur.fetchone())
'''
#============== classb.members =======================
'''
sql = "SELECT * FROM members"
cur.execute(sql)
print(cur.rowcount)

data = cur.fetchone()
print("%s \t%s \t%s \t%s \t%s \t%s \t%s" % data)

data = cur.fetchmany(10)
for dd in data:
    print("%s \t%s \t%s \t%s \t%s \t%s \t%s" % dd)

data = cur.fetchall()
for dd in data:
    print("%s \t%s \t%s \t%s \t%s \t%s \t%s" % dd)
'''

#print(conn)
#print(cur)
#cur.close()
#conn.close()

