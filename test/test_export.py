# coding=utf-8
__author__ = 'hexiaoyu'
import MySQLdb
import database
db = database.Connection(host='localhost',database='test',user='root',password='')

_db = {
    'flyphp': database.Connection(host='192.168.30.239',database='flyphp',user='dev_query',password='OWl32ud0zW8uGLENcNu_'),
    'local': database.Connection(host='localhost',database='test',user='root',password='')
}

result = [[0 for a in range(2)] for b in range(10)]
for i in range(0,10):
    sex = i % 2
    result[i][0]=i
    result[i][1]=sex
    print result[i]

d = _db['local'].query("SELECT VERSION()")  #测试连接上了。。
print d

_db['local'].query("DROP TABLE IF EXISTS customer_sex") #创建数据表，如果已经存在删除表。
sql = """CREATE TABLE customer_sex (
         customer_id  int,
         sex  int )"""
d = _db['local'].query(sql)

for row in result:#将数据插入数据库
    print "row[0],row[1]:",row[0],row[1]
    sql = """INSERT INTO customer_sex
         (customer_id,sex)
         VALUES ('%d','%d')""" % ( row[0],row[1] )
    d = _db['local'].query(sql)




