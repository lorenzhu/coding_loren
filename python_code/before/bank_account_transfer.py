# 两个账户转账操作
#_*_ coding:utf8_*_

import sys
import pymysql

#=======================================================================

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn
        
    def check_acct_available(self, acctid):
        cur = self.conn.cursor()
        try:
            sql = "SELECT * FROM bankaccount WHERE acctid=%s" % acctid
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
            sql = "SELECT * FROM bankaccount WHERE acctid=%s AND money>%s" % (acctid, money)
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
            sql = "UPDATE bankaccount SET money = money+%s WHERE acctid = %s " % (money, acctid)
            cur.execute(sql)
            print("reduce_money: " + sql)
            data = cur.fetchall()
            if cur.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cur.close()
    
  #================================================================
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
        
#=================================================================================
        
if __name__  == "__main__":     # 脚本执行入口
    #source_acctid = sys.argv[1]
    #target_acctid = sys.argv[2]
    #money = sys.argv[3]
    source_acctid = int(input("source_acctid: ")) # 付款人账号id
    target_acctid = int(input("target_acctid: ")) # 收款人账号id
    money = int(input("money: "))                 # 转帐金额

    conn = pymysql.connect(host = 'localhost',  port = 3306,    # 创建connection
                           user = 'root',       passwd = '666nicai',
                           db = 'mooc',         charset = 'utf8')
    
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print("出现问题： " + str(e))
    finally:
        conn.close()
