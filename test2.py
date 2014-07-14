# coding=utf-8
__author__ = 'hexiaoyu'
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='192.168.30.239',user='dev_query',passwd='OWl32ud0zW8uGLENcNu_',db='flyphp',port=3306,charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data

def GetCustomerCount():
    sql = """select TABLE_ROWS from information_schema.TABLES
        where information_schema.TABLES.TABLE_SCHEMA = 'flyphp'
        and information_schema.TABLES.TABLE_NAME = 'fly_customer'"""
    try:
       cursor.execute(sql)
       data = cursor.fetchone()
       print data
       print "count is %s " % data[0]

    except:
       print "Error: unable to fecth data"

    return data[0]


sql1 = """SELECT DISTINCT customer_id FROM fly_customer_address WHERE realname LIKE '%%小姐%%' OR realname LIKE '%%女士%%'"""
try:
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    print data1
    print type(data1)


except:
    print "Error: unable to Female"

CusCount=GetCustomerCount()
print "customer count is %s " % CusCount



db.close()